# 03 — SFT, LoRA, and QLoRA

## SFT

Supervised fine-tuning trains the model on examples of desired behavior. The quality of the instruction/input/output distribution matters as much as the training configuration.

Conceptually:

```text
Base model
   +
Task examples
   ↓
Supervised loss
   ↓
Adapted model
```

## LoRA

LoRA freezes the base weights and learns low-rank update matrices for selected modules. This reduces the number of trainable parameters and makes adapter artifacts much smaller than full model checkpoints.

The engineering questions are:

- Which modules should receive adapters?
- What rank is sufficient?
- How much training data is available?
- Does the adapter generalize outside the training distribution?
- Is the serving stack compatible with the adapter?

## QLoRA

QLoRA combines low-rank adaptation with low-bit loading of the base model to reduce training memory requirements. It is particularly useful when full-precision loading is too expensive for the available GPU.

Do not assume that lower memory automatically means lower total cost. Measure training throughput, checkpoint size, stability, and final inference requirements.

## Starting experiment

Use a small model and a small, clean dataset first. Verify the entire pipeline before scaling.

Example configuration categories:

```yaml
method: lora
rank: 16
alpha: 32
dropout: 0.05
learning_rate: 2e-4
num_epochs: 2
max_seq_length: 2048
per_device_batch_size: 1
gradient_accumulation_steps: 16
warmup_ratio: 0.05
```

These are experiment starting points, not universal defaults. Tune them against the dataset and model.

## Memory accounting

Approximate training memory is affected by:

```text
model weights
+ gradients
+ optimizer states
+ activations
+ temporary tensors
+ KV-cache-related buffers
+ framework overhead
```

QLoRA primarily changes the memory footprint of the frozen base model; activations and other training components can still dominate.

## Common failure modes

### Out of memory

Try, in order:

1. Reduce sequence length.
2. Reduce micro-batch size.
3. Increase gradient accumulation to preserve effective batch size.
4. Enable activation/gradient checkpointing where supported.
5. Use a memory-efficient attention implementation where compatible.
6. Use QLoRA/quantized loading where appropriate.
7. Reduce adapter/model size.

### Training loss decreases but quality gets worse

Investigate:

- Data leakage
- Overfitting
- Label/template errors
- Evaluation mismatch
- Catastrophic forgetting
- Too many epochs
- Excessively high learning rate

### Adapter works in training but not serving

Check:

- Base model exact revision
- Tokenizer and chat template
- Adapter target modules
- Adapter format
- Merge behavior
- Serving engine compatibility
- Quantization configuration

## Reproducibility requirements

Log:

- Base model ID and revision
- Dataset version/hash
- Tokenizer
- Chat template
- Random seeds
- Python/package versions
- CUDA/GPU information
- Training arguments
- Adapter configuration
- Git commit
- Evaluation-set version

## Recommended practical lab

Train the same task using:

1. Prompt-only baseline
2. SFT
3. LoRA
4. QLoRA

Compare quality, GPU memory, training time, artifact size, inference latency, and failure modes.

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| SFT | Supervised Fine-Tuning; training a model on examples of desired behavior. |
| LoRA | Low-Rank Adaptation; learns small trainable update matrices while most base-model weights remain frozen. |
| QLoRA | LoRA plus low-bit loading of the base model to reduce training memory. |
| Adapter | A small set of learned parameters that modifies a frozen base model's behavior. |
| Base model | The original pretrained model before task-specific adaptation. |
| Trainable parameters | Model values that are updated during training. |
| Low-rank | A mathematical structure that represents an update using fewer independent values than a full matrix. |
| Quantization | Representing numerical model values with fewer bits, such as 4-bit or 8-bit formats. |
| Checkpoint | A saved snapshot of training state or model/adapter weights. |
| Activation | Intermediate values produced while the model processes inputs; they consume training memory. |
| Gradient | A signal indicating how model parameters should change to reduce the training loss. |
| Optimizer state | Extra values maintained by an optimizer to determine parameter updates. |
| Gradient accumulation | Combining gradients across multiple micro-batches before performing an optimizer update. |
| Gradient checkpointing | Saving fewer intermediate activations and recomputing them later to reduce memory usage. |
| Sequence length | The number of tokens processed in one training example or context. |
| Chat template | The formatting convention used to turn messages such as system/user/assistant turns into model input tokens. |
| Catastrophic forgetting | Loss of previously useful capabilities after narrow fine-tuning. |
| Generalization | Performance on unseen examples rather than only the training examples. |
| Effective batch size | The amount of data represented by an optimizer update after accounting for device batches and gradient accumulation. |
