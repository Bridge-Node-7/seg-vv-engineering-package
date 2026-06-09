# High-Voltage and Lab Safety Risk Register

This repository is not a high-voltage construction guide. It does not provide circuit diagrams, capacitor charging instructions, discharge procedures, or DIY lethal-energy methods.

Any hazardous electrical, rotating, magnetic, machining, or RF work must be performed only by qualified personnel using appropriate lab controls, local rules, interlocks, PPE, guarding, and emergency procedures.

## Major Hazards

| ID | Hazard | Severity | Likelihood | Required Control | Status |
|---|---|---|---|---|---|
| S-001 | Stored electrical energy | Critical | Medium | Qualified lab controls, lockout, discharge verification, interlocks | Mandatory |
| S-002 | Arc flash or electrical shock | Critical | Medium | Enclosures, barriers, PPE, one-hand rule where applicable, trained operator | Mandatory |
| S-003 | Residual charge after shutdown | Critical | Medium | Verified discharge, posted wait times, measurement before touch | Mandatory |
| S-004 | Rotor or magnet fly-off | High | Medium | Rotor guard, exclusion zone, speed limits, remote operation | Mandatory |
| S-005 | Magnet pinch or crush injury | Medium | Medium | Handling tools, gloves where appropriate, spacing controls | Required |
| S-006 | Rare-earth dust or machining fire | High | Medium | Wet machining, dust control, appropriate fire readiness | Required |
| S-007 | Rotor heating | Medium | Medium | Temperature monitoring, duty-cycle limits, shutdown threshold | Required |
| S-008 | RF exposure or interference | High | Low-Medium | RF safety review, enclosure, monitoring, low-power start | Future phase only |
| S-009 | Instrument damage from strong fields or pulses | Medium | Medium | Distance, shielding, calibration checks, sacrificial sensors | Required |
| S-010 | Data contamination from vibration, airflow, or operator contact | Medium | High | Fixed fixture, environmental log, video, blind controls | Required |
| S-011 | False positive weight readings | High | Medium | Vibration isolation, airflow control, EM controls, dummy mass | Future phase only |
| S-012 | False positive energy readings | High | Medium | True power measurement, thermal accounting, control loads | Future phase only |

## MVP Safety Checklist

- [ ] Test objective is documented.
- [ ] Protocol ID is assigned.
- [ ] Safety owner is named.
- [ ] Rotating parts are guarded.
- [ ] Emergency stop exists and is tested.
- [ ] Instruments are outside hazard zones.
- [ ] No loose ferromagnetic objects are near magnets.
- [ ] Operators know stop conditions.
- [ ] Video recording does not require entering the hazard zone.
- [ ] High-voltage systems are absent from the MVP motion test unless separately approved by qualified safety review.

## Stop Conditions

Stop immediately if:

- rotor vibration increases unexpectedly,
- magnet contacts the rotor,
- magnet holder shifts,
- temperature exceeds safe limits,
- instrument readings become unstable due to interference,
- a person enters the exclusion zone,
- any unexpected electrical sound, smell, arcing, smoke, or unsafe motion occurs.

## Documentation Requirement

Log every safety anomaly, even if no injury or damage occurs.
