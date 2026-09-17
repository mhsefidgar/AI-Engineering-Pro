# 09 — Medical/Clinical AI and Responsible Engineering

This repository can demonstrate engineering patterns for high-stakes AI, but a public tutorial is not a substitute for clinical validation, organizational governance, legal review, privacy review, or regulatory assessment.

## Core principles

### Data minimization

Use only the information required for the task. Avoid copying sensitive source material into development environments when synthetic or de-identified alternatives are sufficient.

### Human oversight

Define where qualified humans review, approve, override, or escalate model outputs. The model should not silently become the final authority for a high-stakes decision.

### Traceability

For each output, where applicable record:

- Model/version
- Prompt/template version
- Retrieval sources
- Adapter version
- Relevant input identifiers that are safe to log
- Timestamp
- Evaluation/validation status

Avoid logging sensitive payloads merely for convenience.

### Uncertainty

A polished answer is not evidence of correctness. Design the system so uncertainty, missing evidence, and unsupported claims can be surfaced.

## Bias/fairness testing

Evaluate important population or workflow slices relevant to the intended use. Document sample sizes and limitations. Avoid claiming fairness from a single aggregate metric.

## Safety cases

Create explicit tests for:

- Missing information
- Contradictory information
- Ambiguous terminology
- Rare conditions/tasks
- Unsupported requests
- Unsafe recommendations
- Prompt injection/tool misuse
- Overconfident output
- Incorrect structured extraction

## Model card

Document:

```text
Intended use
Out-of-scope use
Base model
Adaptation method
Training data description
Evaluation data
Known limitations
Safety evaluation
Bias/fairness evaluation
Privacy/security controls
Deployment constraints
Human oversight
Version history
```

## Security

Treat model-serving infrastructure as an application security surface. Apply authentication, authorization, secret management, network controls, dependency scanning, image scanning, audit logging, and least privilege.

## Regulatory terminology

HIPAA and GDPR are not interchangeable checklists. Applicability depends on the organization, jurisdiction, role, processing activity, contracts, and data involved. The engineering documentation should identify the controls being implemented without making unsupported legal-compliance claims.

## Responsible AI reference

Use the NIST AI Risk Management Framework and its Generative AI Profile as governance references, then map controls to the actual organization's requirements.
