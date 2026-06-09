# MVP Contactless Rotation Validation Protocol v1.4.2

**Protocol ID:** SEG-MVP-ROT-001  
**Version:** 1.4.2  
**Purpose:** Test whether a conditioned ring magnet behaves measurably differently than control magnets near a spinning copper rotor.

Use `protocols/MVP_Contactless_Rotation_Operator_Checklist_v1.4.2.md` during execution.

## 1. Test Question

> Under identical conditions, does a conditioned ring magnet rotate, accelerate, brake, or otherwise move differently than unconditioned and sham-conditioned controls near a spinning copper rotor?

## 2. Scope

This protocol tests only a contactless motion claim. It does not test energy generation, cooling, weight loss, antigravity, flight, propulsion, or self-sustaining operation.

## 3. Test Article Groups

Use three groups when possible:

| Group | Description | Purpose |
|---|---|---|
| A | Unconditioned control magnet | Baseline |
| B | Sham-conditioned magnet | Handling and expectation control |
| C | Conditioned magnet | Test article |

All magnets should be as similar as practical in batch, geometry, material, mass, magnetization orientation, storage, and handling.

## 4. Required Instrumentation

Minimum:

- Rotor RPM measurement.
- Magnet motion measurement by tachometer, optical tracking, or timestamped video.
- Fixed nonmagnetic gap jig.
- Rotor input power measurement.
- Temperature measurement near rotor and magnet.
- Before and after field maps.
- Timestamped video record.

Recommended:

- High-speed camera.
- 3-axis magnetometer or scan rig.
- Current and voltage logger.
- Vibration sensor.
- Ambient temperature and airflow log.

## 5. Required Controls

- Randomized trial order.
- Blind or masked magnet identity where practical.
- Reversed rotor direction.
- Static copper control.
- Nonconductive rotor control.
- Fixed gap measured by jig.
- Rotor runout measurement.
- Same motor warm-up time.
- Same starting angle and orientation.
- Magnet holder friction characterization.
- No hand-held magnet trials as formal evidence.

## 6. Predefined Metrics

Choose metrics before testing. Recommended primary metric:

- Mean magnet RPM during the steady-state observation window.

Recommended secondary metrics:

- Start latency.
- Maximum magnet RPM.
- Direction of rotation.
- Motion/no-motion outcome.
- Rotor input power.
- Rotor and magnet temperature.

## 7. Minimum Trial Set

Recommended starting set:

- At least 5 valid trials per group.
- At least 1 static copper control block.
- At least 1 reversed-direction block.
- More trials are required before strong statistical claims.

## 8. Success Threshold

Before testing, define the threshold in the trial plan. Default first-gate threshold:

- Conditioned group differs from both control and sham groups by a repeatable margin across randomized trials, and
- field-map evidence supports that conditioned magnets were measurably different before the motion test, and
- artifacts such as airflow, vibration, friction, runout, heating, and operator influence are not sufficient explanations.

This threshold supports only a contactless-rotation conditioning claim. It does not support energy, cooling, weight, or propulsion claims.

## 9. Trial Procedure

1. Complete build sheet.
2. Complete conditioning sheet.
3. Assign blind codes where practical.
4. Record field maps before formal trials.
5. Confirm safety controls.
6. Confirm rotor guard and exclusion zone.
7. Confirm fixed gap.
8. Run motor warm-up.
9. Execute randomized trial order.
10. Record video and data for each trial.
11. Log anomalies immediately.
12. Do not interpret results during the trial block.
13. Analyze only after all trials are complete.
14. Complete evidence manifest and file hashes.
15. Obtain reviewer signoff before updating claim status.

## 10. Exclusion Rule

Excluded trials must be justified before outcome analysis where practical. Record the reason in the trial log. Do not exclude trials only because the result is inconvenient.

## 11. Evidence Package

Place completed evidence in:

```text
results/runs/RUN-YYYYMMDD-001/
```

Required items:

- completed trial log,
- completed build sheet,
- completed conditioning sheet,
- field maps,
- videos or motion files,
- instrument configuration notes,
- calibration notes,
- evidence manifest,
- hashes,
- reviewer signoff.

## 12. Interpretation Boundary

A successful MVP may justify moving C-005B upward only within the contactless-rotation lane. It does not validate the full SEG device or any extraordinary claim.
