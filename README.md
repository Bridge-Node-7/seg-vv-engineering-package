# SEG V&V Engineering Package

**Version:** 1.4.2  
**Program:** SEG, Searl Effect Generator, verification and validation framework  
**Source subject:** Isaiah Ritchey  
**Status:** Public V&V framework, not experimental proof

> **Core doctrine:** Narrative confidence is not evidence. Only raw-data-backed evidence packages with reviewer signoff may move a claim upward.

## Why This Framework Exists

Unusual engineering claims can become confusing fast. This package exists to keep the work honest: separate one claim, run one controlled protocol, save raw evidence, hash the files, get reviewer signoff, and only then update the claim status.
## Do This First

1. Open `QUICKSTART.md`.
2. Read `AGENT_BRIEF.md`.
3. Read `START_HERE.md`.
4. Do not claim the SEG works.
5. Run only `SEG-MVP-ROT-001` first:
   - `protocols/MVP_Contactless_Rotation_Protocol_v1.4.2.md`
   - `protocols/MVP_Contactless_Rotation_Operator_Checklist_v1.4.2.md`
6. Save completed evidence under `results/runs/RUN-YYYYMMDD-001/`.
7. Update claim status only after raw data, hashes, manifest, and reviewer signoff exist.

## What This Is

This repository turns SEG-related frontier magnetics claims into controlled, documented, repeatable tests. It is built for a new reviewer, builder, or agent starting from zero context.

It provides:

- claim separation and Evidence Readiness Levels,
- one first-gate MVP protocol,
- an operator checklist,
- build, conditioning, trial-log, and evidence-manifest templates,
- safety boundaries,
- a lightweight analysis stub,
- a run-template folder for first evidence packaging.

## What This Is Not

- Not proof that the SEG works.
- Not proof of over-unity energy, ambient-energy extraction, self-running operation, cooling, weight loss, antigravity, flight, or anomalous propulsion.
- Not a high-voltage construction guide.
- Not a certified laboratory procedure.
- Not a substitute for qualified safety review.

## Current Evidence Status

| Area | Status |
|---|---|
| Framework | Ready |
| Raw experimental data | Not included |
| Independent replication | Not completed |
| Contactless rotation MVP | Ready to test |
| Energy generation claim | Not validated |
| Cooling claim | Not validated |
| Weight-loss claim | Not validated |
| Propulsion or flight claim | Not validated |

## Correct Terminology

- **SEG** means **Searl Effect Generator**.
- **Isaiah Ritchey** is the correct spelling used in this package.
- Prior nonstandard shorthand and incorrect name spellings are not used.

## First Test Gate

The first gate asks only:

> Under identical conditions, does a conditioned ring magnet behave measurably differently than unconditioned and sham-conditioned controls near a spinning copper rotor?

A positive result may support only the contactless-rotation conditioning claim. A null result is still useful evidence.

## Repository Map

```text
SEG_VV_Engineering_Package_v1.4.2/
├── README.md
├── QUICKSTART.md
├── START_HERE.md
├── AGENT_BRIEF.md
├── GLOSSARY.md
├── SOURCE_MATERIAL.md
├── PRIVACY_AND_SCOPE.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── VERSION
├── LICENSE.md
├── requirements.txt
├── MANIFEST.txt
├── SHA256SUMS
├── docs/
│   ├── Claim_Separation_Matrix.md
│   ├── Physics_Explanations.md
│   └── Evidence_Flow.md
├── protocols/
│   ├── MVP_Contactless_Rotation_Protocol_v1.4.2.md
│   └── MVP_Contactless_Rotation_Operator_Checklist_v1.4.2.md
├── templates/
│   ├── Build_Sheet_Template.md
│   └── Conditioning_Parameters_Sheet.md
├── safety/
│   └── High_Voltage_Risk_Register.md
├── roadmap/
│   └── Phased_Validation_Roadmap.md
├── data/
│   ├── Trial_Log_Template.csv
│   └── evidence_manifest_template.csv
├── results/
│   ├── README.md
│   ├── evidence_manifest.csv
│   └── runs/
│       ├── .gitkeep
│       └── RUN-TEMPLATE/
│           ├── README.md
│           ├── completed_trial_log.csv
│           ├── completed_build_sheet.md
│           ├── completed_conditioning_sheet.md
│           ├── instrument_calibration_notes.md
│           ├── reviewer_signoff.md
│           ├── evidence_manifest.csv
│           ├── field_maps/
│           ├── photos/
│           └── videos/
├── analysis/
│   └── trial_log_analysis_stub.py
└── assets/
    └── .gitkeep
```

## Operating Rule

One claim, one protocol, one evidence package.

Do not combine contactless rotation, energy generation, cooling, and weight-change claims into one test. Each claim must be isolated, baselined, instrumented, logged, reviewed, and replicated before its status changes.
