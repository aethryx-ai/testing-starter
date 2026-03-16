# Aethryx AI Testing Starter

A lightweight open-source prototype demonstrating Aethryx-style AI assurance capabilities for enterprise GenAI applications.

## What this demo shows

This starter illustrates how an AI governance and testing platform can:

- run automated evaluations on GenAI outputs
- detect hallucination and grounding issues
- check unsafe content
- detect potential data leakage
- apply simple guardrails
- generate audit logs for traceability

## Risk categories covered

- Accuracy and completeness
- Hallucination and grounding
- Unsafe content
- Security and prompt injection indicators
- Inappropriate data disclosure
- Bias and fairness

## Archetypes covered

- Text-focused GenAI applications
- Retrieval-Augmented Generation (RAG)
- Multi-turn conversational AI
- Enterprise copilots
- Agentic workflows

## Run locally

```bash
python main.py
```

## Output

- Console summary of test results
- `audit_log.json` with structured evidence for review

## Positioning

Aethryx is building technical AI governance and testing infrastructure for enterprise GenAI systems and AI agents, including:

- automated evaluations
- adversarial testing
- runtime guardrails
- policy enforcement
- auditability and traceability
