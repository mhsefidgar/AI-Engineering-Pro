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

## Terms & Phrases Explained

| Term | Plain-English meaning |
|---|---|
| High-stakes AI | An AI system whose errors can have significant consequences for people, organizations, safety, or rights. |
| Data minimization | Collecting, processing, and retaining only the information needed for the intended purpose. |
| Human oversight | Defined points where qualified people review, approve, override, or escalate model behavior. |
| Traceability | The ability to identify relevant versions, inputs, evidence, and processing steps behind an output. |
| Uncertainty | Information indicating that the system may lack sufficient evidence or confidence for a reliable answer. |
| Bias | A systematic difference in model behavior or error rates that may disadvantage particular groups or contexts. |
| Fairness | A family of approaches for assessing and managing disparate performance or treatment across relevant groups. |
| Safety case | Structured evidence and arguments showing that identified safety risks have been addressed to a defined standard. |
| Model card | Documentation describing a model's intended use, limitations, evaluation, risks, and operational considerations. |
| PHI | Protected Health Information under applicable U.S. HIPAA rules. |
| PII | Personally Identifiable Information; the exact definition depends on the applicable legal or organizational framework. |
| HIPAA | U.S. federal requirements governing certain covered entities' and business associates' handling of protected health information. |
| GDPR | European Union data-protection regulation governing processing of personal data within its scope. |
| Authentication | Verifying who or what is requesting access to a system. |
| Authorization | Determining what an authenticated user or service is permitted to access or do. |
| Least privilege | Giving users and services only the access required for their legitimate tasks. |
| Prompt injection | An attempt to manipulate model instructions through untrusted input or retrieved content. |
| Audit logging | Recording security- or governance-relevant events so activity can be reviewed later. |
| Clinical validation | Evidence that a system performs acceptably for its intended clinical use under an appropriate validation process. |
| Governance | The policies, roles, processes, and controls used to manage AI risks and accountability. |
