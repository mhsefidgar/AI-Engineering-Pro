# LLM Fine-Tuning & Adaptation

A practical, production-oriented guide to adapting large language models for domain-specific applications, with a strong emphasis on medical/clinical AI, parameter-efficient fine-tuning, evaluation, deployment, MLOps, and responsible AI.

This section is designed around the **AI/ML Engineer — LLM fine-tuning and adaptation** role described in the project brief. It is intentionally more than a collection of training snippets: the goal is to show how to move from a raw domain dataset to a validated, monitored, deployable model.

## What this covers

- Choosing between prompting, RAG, SFT, LoRA/QLoRA, preference optimization, and continued pretraining
- Data acquisition, normalization, de-identification, deduplication, leakage prevention, and train/validation/test design
- Instruction tuning and supervised fine-tuning with Hugging Face Transformers/TRL/PEFT
- LoRA and QLoRA, quantization, memory planning, checkpointing, and reproducibility
- Evaluation: task metrics, calibration, factuality, robustness, safety, bias/fairness, and human/domain-expert review
- Model exploration across open-weight families such as Llama, Mistral, Gemma, and other compatible architectures
- RAG + fine-tuning boundaries and hybrid architectures
- Inference with vLLM and adapter serving
- MLOps: experiment tracking, model/data versioning, CI/CD, monitoring, drift, rollback, and auditability
- Distributed training and GPU optimization
- Medical/clinical data controls, PHI handling, privacy, security, and responsible AI
- Failure modes, bottlenecks, debugging playbooks, and production checklists

## Learning sequence

```text
01 Foundations & adaptation strategy
          ↓
02 Data engineering + privacy
          ↓
03 SFT + LoRA/QLoRA
          ↓
04 Evaluation + benchmarking
          ↓
05 Inference + deployment
          ↓
06 MLOps + monitoring
          ↓
07 Medical/regulated AI + governance
          ↓
08 Bottlenecks + production troubleshooting
```

## Practical capstone

The intended capstone is a **clinical-note transformation service** using synthetic/de-identified data. The project should support one or more of:

- clinical summarization
- structured information extraction
- classification
- terminology normalization
- evidence-grounded question answering

The implementation should compare a baseline prompting/RAG system against a LoRA/QLoRA-adapted model and document when fine-tuning is actually justified.

> **Important:** Never place real patient records, PHI, credentials, or proprietary clinical data in this public repository. Use synthetic or appropriately de-identified data and follow the applicable organizational/legal controls.

## Primary references

- Hugging Face PEFT / LoRA: https://huggingface.co/docs/peft/main/package_reference/lora
- Hugging Face TRL: https://huggingface.co/docs/trl/
- vLLM serving: https://docs.vllm.ai/en/stable/cli/serve/
- NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Generative AI Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- HHS HIPAA de-identification guidance: https://www.hhs.gov/hipaa/for-professionals/special-topics/de-identification/index.html
