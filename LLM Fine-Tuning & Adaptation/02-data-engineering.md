# 02 — Data Engineering and Quality

Training quality is usually constrained by data quality before it is constrained by the optimizer.

## Canonical pipeline

```text
Raw source
  ↓
Access control / provenance
  ↓
Parsing + normalization
  ↓
Privacy and security checks
  ↓
Deduplication
  ↓
Quality filtering
  ↓
Task labeling / instruction construction
  ↓
Leakage checks
  ↓
Train / validation / test split
  ↓
Versioned dataset manifest
  ↓
Training
```

## Canonical SFT record

```json
{
  "id": "example-000001",
  "instruction": "Summarize the document.",
  "input": "...",
  "output": "...",
  "source_type": "synthetic",
  "domain": "clinical",
  "split": "train",
  "quality_flags": [],
  "provenance": "dataset-v1"
}
```

Use synthetic or appropriately de-identified examples for public demonstrations. Do not commit private records, credentials, or other restricted data.

## Split strategy

Random row-level splitting can create leakage when multiple records belong to the same entity, encounter, document family, or near-duplicate cluster. Use group-aware splitting where appropriate:

```text
Entity / document group
          ↓
     one split only
```

Treat the test set as a controlled asset. Do not repeatedly tune against it.

## Automated quality checks

Check for:

- Empty inputs/targets
- Excessively long sequences
- Invalid encoding
- Duplicates and near duplicates
- Contradictory labels
- Invalid JSON/schema outputs
- Repetitive or corrupted examples
- Template errors
- Train/test overlap
- Sensitive-data leakage

## Data cards

For every dataset version document:

- Source and ownership
- Intended use
- Excluded use
- Collection period
- Preprocessing
- Labeling process
- Known biases
- Known missingness
- Split strategy
- Version/hash
- Privacy/security controls
- Retention policy

## Medical/clinical projects

A real clinical deployment requires organization-specific privacy, security, legal, and governance review. For the portfolio project, demonstrate the engineering controls without putting real patient data into GitHub.

Document:

1. What data enters the pipeline.
2. What data is removed or transformed.
3. Who can access raw data.
4. Where processing occurs.
5. Whether external model APIs receive data.
6. How artifacts are retained and deleted.
7. How access and processing are audited.

## Data contamination risks

Watch for:

- Evaluation examples accidentally entering training
- Generated examples derived from benchmark answers
- Duplicate documents across splits
- Benchmark material present in upstream training data
- Synthetic examples that leak evaluation patterns

## Practical repository boundary

```text
data/raw/       → private/restricted; never committed
 data/processed/ → controlled/versioned artifacts
 data/eval/      → restricted test set
```

The public repository should contain schemas, validation code, synthetic examples, manifests, and documentation—not restricted source data.

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| Data engineering | Preparing, validating, transforming, versioning, and delivering data for reliable ML use. |
| Provenance | A record of where data came from and how it was transformed. |
| Normalization | Converting different source formats into a consistent representation. |
| Deduplication | Finding and removing repeated or near-repeated examples. |
| Leakage | Information crossing into training or model selection from data that should remain unseen. |
| Group-aware split | Splitting related records as a group so the same entity does not appear across train and test sets. |
| Train set | Examples used to update model parameters during training. |
| Validation set | Data used during development to compare configurations and monitor generalization. |
| Test set | Held-out data used for final or controlled evaluation. |
| Data card | Documentation describing a dataset's origin, intended use, limitations, and processing. |
| Synthetic data | Artificially generated data designed to resemble useful patterns without using the original sensitive records. |
| De-identification | Removing or transforming identifying information according to an applicable privacy standard. |
| PHI/PII | PHI is protected health information; PII is personally identifiable information. Their exact legal definitions depend on the applicable framework. |
| Data contamination | Unintended inclusion of benchmark, evaluation, or otherwise restricted information in a dataset. |
| Manifest | A versioned list describing exactly which data files or examples belong to a dataset release. |
| Retention policy | Rules defining how long data or artifacts are kept and when they are deleted. |
