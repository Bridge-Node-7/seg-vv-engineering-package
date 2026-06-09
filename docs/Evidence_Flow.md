# Evidence Flow

This package uses one evidence path.

```text
Claim
  ↓
Protocol
  ↓
Controlled run
  ↓
Raw data
  ↓
Evidence manifest
  ↓
SHA-256 hashes
  ↓
Reviewer signoff
  ↓
Claim status update
```

## Rule

A claim does not move upward because a video looks interesting, a story sounds persuasive, or a source is confident.

A claim moves upward only when the matching protocol produces a completed evidence package.

## First Gate

```text
SEG-MVP-ROT-001
```

Question:

> Under identical conditions, does a conditioned ring magnet behave measurably differently than unconditioned and sham-conditioned controls near a spinning copper rotor?

## Claim Boundary

A successful contactless-rotation run does not validate energy generation, cooling, weight loss, antigravity, flight, propulsion, self-running operation, or over-unity operation.

Those claims require later protocols and stronger evidence.

## Where Evidence Goes

```text
results/runs/RUN-YYYYMMDD-001/
```

Use `results/runs/RUN-TEMPLATE/` as the folder model.
