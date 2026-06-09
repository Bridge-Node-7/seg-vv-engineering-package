"""SEG V&V trial log analysis stub v1.4.2.

Usage:
    python analysis/trial_log_analysis_stub.py results/runs/RUN-ID/completed_trial_log.csv

This script performs basic data-completeness and summary checks only. It is not
formal validation and must not be used alone to upgrade claim status.
"""
from __future__ import annotations

import sys
from pathlib import Path
import pandas as pd

SCRIPT_VERSION = "1.4.2"

REQUIRED_COLUMNS = {
    "trial_id", "trial_order", "magnet_group", "rotor_material", "rotor_direction",
    "rotor_rpm_actual", "gap_mm", "magnet_rpm_mean", "motion_observed",
    "calibration_status", "field_map_before", "field_map_after", "video_file",
    "pass_fail", "reviewer_signoff"
}

NUMERIC_COLUMNS = [
    "trial_order", "rotor_rpm_actual", "gap_mm", "magnet_rpm_mean",
    "magnet_rpm_max", "input_power_w", "ambient_temp_c", "vibration_level"
]

EVIDENCE_COLUMNS = ["video_file", "field_map_before", "field_map_after", "calibration_status"]


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python analysis/trial_log_analysis_stub.py <trial_log.csv>")
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        return fail(f"Missing file: {path}")

    df = pd.read_csv(path)
    print(f"SEG trial log analysis stub v{SCRIPT_VERSION}")
    print(f"File: {path}")
    print(f"Rows: {len(df)}")

    if len(df) == 0:
        return fail("Trial log has no rows. Empty templates are not evidence.")

    missing = REQUIRED_COLUMNS.difference(df.columns)
    if missing:
        return fail("Missing required columns: " + ", ".join(sorted(missing)))

    for col in NUMERIC_COLUMNS:
        if col in df.columns:
            coerced = pd.to_numeric(df[col], errors="coerce")
            bad = df[col].notna() & coerced.isna()
            if bad.any():
                print(f"WARNING: non-numeric values found in numeric column {col}: {bad.sum()}")
            df[col] = coerced

    print("\nGroup counts:")
    print(df["magnet_group"].value_counts(dropna=False))

    if "trial_order" in df.columns and df["trial_order"].notna().any():
        print("\nTrial order range:", df["trial_order"].min(), "to", df["trial_order"].max())
        if df["trial_order"].is_monotonic_increasing:
            print("NOTE: trial_order is monotonic. Confirm randomized order was actually used if required.")

    print("\nEvidence completeness:")
    for col in EVIDENCE_COLUMNS:
        missing_count = df[col].isna().sum() + (df[col].astype(str).str.strip() == "").sum()
        print(f"- {col}: {len(df) - missing_count}/{len(df)} populated")

    print("\nMagnet RPM summary by group:")
    print(df.groupby("magnet_group")["magnet_rpm_mean"].describe())

    if "excluded_from_analysis_yes_no" in df.columns:
        print("\nExclusion counts:")
        print(df["excluded_from_analysis_yes_no"].value_counts(dropna=False))

    print("\nReminder: this summary is not validation. Attach raw data, field maps, videos, calibrations, manifests, hashes, and reviewer signoff before updating claims.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
