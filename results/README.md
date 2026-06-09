# Results Folder

This folder is for completed evidence packages only.

## Do This First

Copy the layout from:

```text
results/runs/RUN-TEMPLATE/
```

Create a real run folder named like this:

```text
results/runs/RUN-YYYYMMDD-001/
```

## Required Structure

```text
results/
└── runs/
    └── RUN-YYYYMMDD-001/
        ├── README.md
        ├── completed_trial_log.csv
        ├── completed_build_sheet.md
        ├── completed_conditioning_sheet.md
        ├── instrument_calibration_notes.md
        ├── field_maps/
        ├── photos/
        ├── videos/
        ├── reviewer_signoff.md
        └── evidence_manifest.csv
```

## Required Rule

Do not update the Claim Separation Matrix until the run folder includes raw evidence, controls, hashes, manifests, and reviewer notes.

Use `data/evidence_manifest_template.csv` as the manifest template.
