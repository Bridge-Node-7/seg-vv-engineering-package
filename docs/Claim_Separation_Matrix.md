# SEG Claim Separation Matrix

**Purpose:** Keep every claim in its proper evidence lane. This prevents ordinary bench effects from being conflated with unverified extraordinary claims.

## Status Labels

- **Documented Claim:** Stated in source material, not independently verified.
- **Observed by Builder:** Reported as observed by the builder, not independently replicated.
- **Conventionally Plausible:** Compatible with known physics or ordinary engineering explanations.
- **Hypothesized:** Proposed mechanism or expectation, not demonstrated.
- **Extraordinary / Unverified:** Requires calibrated measurement, error analysis, and independent replication.
- **Replicated:** Independently repeated under controlled conditions with raw data.

## Evidence Readiness Levels

- **ERL-0:** Narrative claim only.
- **ERL-1:** Informal or builder-reported observation.
- **ERL-2:** Controlled internal test completed.
- **ERL-3:** Quantified internal repeatability with statistics and raw logs.
- **ERL-4:** Independent replication by another operator or lab.
- **ERL-5:** Multi-site validation with error budgets and external review.

## Matrix

| ID | Claim | Type | Current Status | ERL | Required Protocol | Evidence Required | Exit Criteria |
|---|---|---|---|---:|---|---|---|
| C-001 | Three-ring architecture uses 12 + 22 + 32 rollers, 66 total | Build architecture | Documented Claim | ERL-0 | Build Sheet | Photos, dimensions, BOM, assembly count | Verified by inspection |
| C-002 | Each roller uses segmented material layers | Build architecture | Documented Claim | ERL-0 | Build Sheet | Photos, CAD, material specs, weights | Verified by inspection |
| C-003 | Air gap improves ring stability | Stability engineering | Observed by Builder | ERL-1 | Stability Test Protocol TBD | Gap measurement, RPM, fly-off events, vibration data | Repeatable stable range identified |
| C-004 | Smooth operation occurs within a limited RPM band | Stability engineering | Observed by Builder | ERL-1 | Stability Test Protocol TBD | Tachometer logs, video, vibration, trial count | Repeatable across runs |
| C-005A | Magnet/conductor contactless interaction occurs near a spinning copper rotor | Motion / field interaction | Conventionally Plausible | ERL-1 | SEG-MVP-ROT-001 / MVP Contactless Rotation Protocol v1.4.2 | Rotor RPM, gap, video, magnet motion, baseline controls | Repeatable interaction under controlled setup |
| C-005B | Conditioned magnetic patterning produces statistically significant behavior difference versus control and sham-conditioned magnets | Conditioning effect | Hypothesized / observed by builder, not validated | ERL-0 | SEG-MVP-ROT-001 / MVP Contactless Rotation Protocol v1.4.2 | Conditioned vs unconditioned vs sham results, field maps, RPM logs, randomized order, reviewer signoff | Statistically clear difference attributable to conditioning |
| C-006 | Peak-valley field shaping affects contactless rotation | Magnetic conditioning | Hypothesized / partially observed | ERL-1 | SEG-MVP-ROT-001 / MVP Contactless Rotation Protocol v1.4.2 | Before/after field maps and behavior logs | Repeatable effect linked to field map |
| C-007 | Specific magnetic waveform counts alter behavior | Magnetic conditioning | Hypothesized | ERL-0 | Waveform Conditioning Protocol TBD | Field maps, motion metrics, controls | Count-specific behavior replicated |
| C-008 | Specific wire angle improves waveform patterns | Conditioning method | Hypothesized / builder observation | ERL-1 | Conditioning Comparison Protocol TBD | Same magnet type, different angles, field maps | Claimed angle outperforms controls |
| C-009 | Ceramic magnets show low-frequency mechanical resonance | Resonance | Observed by Builder | ERL-1 | Resonance Characterization Protocol TBD | Frequency sweep, sensor/accelerometer data | Resonance peak repeatable |
| C-010 | Neodymium magnets show low-frequency mechanical resonance | Resonance | Observed by Builder | ERL-1 | Resonance Characterization Protocol TBD | Frequency sweep, sensor/accelerometer data | Resonance peak repeatable |
| C-011 | Mechanical shock may disturb field impressions | Magnetic stability | Hypothesized / builder observation | ERL-1 | Shock Robustness Protocol TBD | Before/after field maps, controlled impact energies | Pattern degradation quantified |
| C-012 | Resonance may imprint magnetic patterns without high-voltage discharge | Magnetic conditioning | Hypothesized | ERL-0 | Resonance Conditioning Protocol TBD | Field maps before/after resonance exposure | Pattern emerges above baseline |
| C-013 | Dielectric/electret layer may retain charge after preparation | Materials / dielectric | Conventionally Plausible | ERL-1 | Electret Charge Retention Protocol TBD | Surface potential logs over time | Charge retention quantified |
| C-014 | SEG can generate useful excess electricity from ambient energy | Energy | Extraordinary / Unverified | ERL-0 | Energy Balance Protocol TBD | Precision input/output power, calorimetry, controls | Net output exceeds all inputs and uncertainty |
| C-015 | SEG produces measurable cooling or refrigeration | Thermal | Extraordinary / Unverified | ERL-0 | Thermal Balance Protocol TBD | Thermal probes, calorimetry, controls | Cooling exceeds ordinary losses and artifacts |
| C-016 | SEG produces measurable weight change | Mass / gravity | Extraordinary / Unverified | ERL-0 | Mass Metrology Protocol TBD | Isolated precision scale, vibration/airflow/EM controls | Repeatable signal above uncertainty |
| C-017 | SEG produces flight or anomalous propulsion | Propulsion | Extraordinary / Unverified | ERL-0 | Not eligible until earlier gates progress | Independent lab data | Independent replication |

## Operating Rule

A claim may only move upward when raw evidence is attached, reviewed, and traceable. Narrative confidence is not evidence.
