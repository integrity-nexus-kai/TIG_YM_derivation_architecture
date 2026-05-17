# Theorem Dependency Graph

## Purpose

This document defines the logical dependency structure of the TIG3 vacuum-sector framework.

Its purpose is:

- theorem-chain transparency,
- dependency tracking,
- proof-architecture stabilization,
- and prevention of hidden logical jumps.

This document is part of the TIG3 publication-hardening layer.

---

# Core Principle

The TIG3 framework is constructed as:

```text
a layered conditional perturbative theorem architecture.
```

Each theorem layer depends explicitly on previous assumptions and constructions.

No theorem should be interpreted independently of its dependency chain.

---

# Global Dependency Structure

The current TIG3 vacuum-sector program follows the dependency hierarchy:

```text
TIG2 branch structure
    ↓
representative geometry
    ↓
bounded curvature sector
    ↓
perturbative reduction
    ↓
effective radial operator
    ↓
quadratic form
    ↓
self-adjoint realization
    ↓
spectral admissibility
    ↓
bounded linear evolution
```

Each layer inherits assumptions from all previous layers.

---

# Level 0 — TIG2 Structural Foundation

## Core Input

The foundational structural relation is

```text
x^3 - x^2 + beta^3 = 0.
```

Associated structures include:

- branch geometry,
- discriminant structure,
- critical point,
- and saddle-node transition behavior.

---

## Dependency Role

TIG2 provides:

```text
the admissible branch architecture
```

used throughout TIG3.

Without TIG2:

- no branch merger structure,
- no critical geometry,
- and no admissible horizon hierarchy exist.

---

# Level 1 — Representative Geometry

## Geometry Layer

The representative metric ansatz is

```text
F(r)
=
1 - 2Mr^2/(r^3+r_c^3).
```

This layer defines:

- regulated core structure,
- Schwarzschild asymptotics,
- and bounded representative curvature.

---

## Dependency

This layer depends on:

```text
TIG2 admissible branch structure.
```

The geometry is interpreted as compatible with the TIG2 structural sector.

---

# Level 2 — Curvature Structure

## Curvature Layer

Curvature invariants are analyzed on the representative geometry.

Near the core:

```text
F(r)
approx
1 - (2M/r_c^3) r^2.
```

This yields finite representative curvature invariants.

---

## Dependency

Curvature boundedness depends on:

- the representative metric,
- and the regulated-core structure.

Without the representative geometry, the bounded-curvature statements collapse.

---

# Level 3 — Perturbative Reduction

## Perturbation Layer

Perturbations are introduced via

```text
g_ab -> g_ab + h_ab.
```

Linearization yields a reduced radial perturbation sector.

---

## Dependency

Perturbative reduction depends on:

- the representative background geometry,
- spherical symmetry,
- harmonic decomposition,
- and gauge reduction assumptions.

---

# Level 4 — Effective Radial Operator

## Operator Layer

The reduced perturbative dynamics are modeled by

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r).
```

This creates the operator-theoretic structure of TIG3.

---

## Dependency

The operator layer depends on:

- perturbative reduction,
- effective radial projection,
- and candidate potential structure.

If the perturbative reduction fails, the operator program fails.

---

# Level 5 — Quadratic Form Program

## Functional-Analytic Layer

The quadratic form is

```text
Q[psi]
=
int
(
|partial_r_* psi|^2
+
V_eff |psi|^2
)
dr_*
```

This introduces:

- symmetry structure,
- lower-bound analysis,
- and closability questions.

---

## Dependency

The quadratic form depends on:

- existence of the radial operator,
- admissible perturbation domain,
- and endpoint structure.

---

# Level 6 — Self-Adjoint Realization

## Friedrichs Layer

The self-adjoint realization program constructs:

```text
L_TIG^F.
```

This enables:

- real spectrum,
- spectral theorem applicability,
- and controlled evolution theory.

---

## Dependency

Self-adjoint realization depends on:

- quadratic-form closability,
- lower boundedness,
- and endpoint classification.

Without these, the self-adjoint framework is invalid.

---

# Level 7 — Spectral Admissibility

## Spectral Layer

The central condition is

```text
sigma(L_TIG^F)
subset
[0,infinity).
```

This excludes negative spectral modes.

---

## Dependency

Spectral admissibility depends on:

- existence of the self-adjoint operator,
- and nonnegativity of the quadratic form.

Without self-adjointness, spectral statements lose mathematical meaning.

---

# Level 8 — Bounded Linear Evolution

## Evolution Layer

The perturbative evolution equation is

```text
partial_t^2 Psi
+
L_TIG^F Psi
=
0.
```

This yields bounded linear perturbative evolution under spectral nonnegativity assumptions.

---

## Dependency

Bounded linear evolution depends on:

- self-adjoint realization,
- spectral nonnegativity,
- and finite-energy initial data.

If negative spectral modes exist, bounded evolution fails.

---

# Near-Critical Dependency Sector

## Critical Regime

Near

```text
beta approx beta_c,
```

additional structures may emerge:

- throat elongation,
- resonance accumulation,
- spectral compression,
- and metastable sectors.

These affect multiple theorem layers simultaneously.

---

## Dependency Sensitivity

The near-critical sector is especially sensitive because it simultaneously impacts:

- geometry,
- endpoint structure,
- spectral estimates,
- and perturbative evolution.

This regime remains partially unresolved.

---

# Conditionality Structure

The TIG3 framework possesses the following logical structure:

```text
geometry
→ perturbation theory
→ operator structure
→ quadratic form
→ self-adjointness
→ spectral admissibility
→ bounded evolution
```

The later layers are mathematically meaningless without the earlier layers.

---

# Failure Propagation Principle

Failure of a lower theorem layer propagates upward.

Examples:

| Failure | Consequence |
|---|---|
| invalid perturbative reduction | operator program collapses |
| non-closable quadratic form | no self-adjoint realization |
| negative spectrum | exponential instability possible |
| invalid endpoint classification | domain ambiguity |

This dependency structure must remain explicit.

---

# Canonical Scientific Interpretation

The current TIG3 framework should be interpreted as:

```text
a layered conditional perturbative theorem architecture
```

rather than a monolithic completed proof.

---

# Publication Interpretation

The theorem chain is strongest when presented explicitly as:

```text
a conditional operator-theoretic admissibility hierarchy.
```

This avoids hidden assumptions and stabilizes publication clarity.

---

# Final Status

This document establishes the theorem dependency structure for the TIG3 publication-hardening program.