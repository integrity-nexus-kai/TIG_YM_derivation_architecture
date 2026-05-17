# Self-Adjoint Realization

## Purpose

This document defines the self-adjoint realization framework for the TIG3 radial stability operator.

The objective is to move from the formal operator

```text
L_TIG = -d^2/dr_*^2 + V_eff(r)
```

to a mathematically controlled self-adjoint operator on an admissible Hilbert space.

This document is part of the six-file TIG3 proof-closing sequence.

It follows the quadratic-form analysis and prepares the spectral nonnegativity analysis.

---

# Starting Point

The current TIG3 radial operator is

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r),
```

with candidate effective potential

```text
V_eff(r)
=
F(r)
[
ell(ell+1)/r^2
+
F'(r)/r
].
```

The Hilbert space is

```text
H_TIG = L^2(I,dr_*),
```

where \(I\) is the admissible tortoise-coordinate interval.

---

# Minimal Operator

Define the minimal operator

```text
L_min psi = -d^2 psi/dr_*^2 + V_eff(r) psi
```

on

```text
D(L_min) = C_c^\infty(I).
```

If \(V_eff(r)\) is real-valued, then \(L_min\) is symmetric.

This provides the starting point for self-adjoint realization.

---

# Need for Self-Adjointness

A symmetric operator is not automatically self-adjoint.

Self-adjointness is required for:

- real spectrum,
- unitary or energy-controlled linear evolution,
- spectral theorem applicability,
- and rigorous stability analysis.

Without a self-adjoint realization, spectral statements remain formal.

---

# Quadratic Form Route

The associated quadratic form is

```text
Q[psi]
=
int_I
(
|d psi/dr_*|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

The Friedrichs construction applies if this form is:

1. densely defined,
2. symmetric,
3. closable,
4. bounded from below.

---

# Friedrichs Realization

If

```text
Q[psi] >= -C ||psi||^2
```

for some finite constant \(C\), then there exists a canonical self-adjoint operator associated with the closure of \(Q\).

This operator is the Friedrichs realization of the TIG3 radial operator.

We denote it by

```text
L_TIG^F.
```

---

# Candidate Definition

The TIG3 self-adjoint realization is therefore defined as:

```text
L_TIG^F
=
Friedrichs extension of L_min
associated with Q.
```

This definition is conditional on the lower-boundedness and closability of \(Q\).

---

# Domain of the Realized Operator

The domain

```text
D(L_TIG^F)
```

is determined by the closed quadratic form and admissible endpoint behavior.

It is not necessarily equal to

```text
C_c^\infty(I).
```

Rather, it is the operator domain induced by the closed form.

---

# Endpoint Input

The endpoint-classification program supplies the boundary data needed for the self-adjoint domain.

Expected endpoint behavior:

| Endpoint | Expected role |
|---|---|
| core, ell=0 | regular boundary |
| core, ell>0 | inverse-square singular analysis |
| simple horizon | limit-point expected |
| infinity | limit-point expected |
| critical branch merger | delicate / open |

The final operator domain depends on this classification.

---

# Core Sector

For the s-wave sector

```text
ell = 0,
```

the potential is expected to be finite near the regulated core.

This suggests a regular endpoint structure and a natural admissible boundary condition such as:

```text
psi finite at r=0
```

or

```text
d psi/dr_* = 0 at r=0.
```

The precise condition must be fixed by the domain construction.

---

# Higher Angular Modes

For

```text
ell > 0,
```

the potential contains the nonnegative inverse-square term

```text
ell(ell+1)/r^2.
```

Since this term is repulsive rather than attractive, it does not by itself generate inverse-square collapse.

However, rigorous endpoint classification is still required.

---

# Horizon and Infinity

At simple horizons, the potential is expected to vanish as

```text
F(r) -> 0.
```

At spatial infinity, the potential decays as

```text
V_eff(r) ~ ell(ell+1)/r^2 + O(r^-3).
```

Both are expected to be compatible with standard limit-point behavior.

These expectations remain theorem targets.

---

# Near-Critical Sector

At

```text
beta approx beta_c,
```

the branch merger may create:

- extended tortoise-coordinate regions,
- effective-potential flattening,
- resonance accumulation,
- and slow relaxation.

The self-adjoint realization may remain valid, but spectral estimates may become delicate.

This regime requires separate analysis.

---

# Preliminary Proposition

## Proposition — Conditional Self-Adjoint Realization

Assume:

1. \(V_eff(r)\) is real-valued and locally integrable on the admissible interval \(I\),
2. the associated quadratic form \(Q\) is densely defined,
3. \(Q\) is closable,
4. \(Q\) is bounded from below.

Then the TIG3 radial operator admits a canonical self-adjoint Friedrichs realization

```text
L_TIG^F.
```

This proposition is conditional and remains dependent on the proof of the assumptions.

---

# Consequence

Once \(L_TIG^F\) is constructed, the spectral problem

```text
L_TIG^F psi = omega^2 psi
```

becomes mathematically meaningful.

The spectrum is real, and spectral-admissibility questions can be posed rigorously.

---

# Remaining Open Questions

The following items remain unresolved:

| Question | Status |
|---|---|
| proof of lower boundedness | open |
| proof of closability | open |
| full endpoint classification | open |
| uniqueness of self-adjoint extension | open |
| spectral nonnegativity | open |
| near-critical domain stability | open |

---

# Relation to TIG3 Proof Chain

This file connects:

```text
quadratic form analysis
→ Friedrichs realization
→ self-adjoint operator
→ spectral nonnegativity
→ bounded linear evolution.
```

It therefore marks the transition from formal perturbation theory to rigorous spectral analysis.

---

# Current Limitations

This document does not yet prove:

- spectral positivity,
- bounded evolution,
- nonlinear stability,
- complete vacuum regularity,
- or uniqueness of the full perturbation theory.

It defines the conditional self-adjoint realization of the radial operator.

---

# Next Required Step

The next mathematical step is:

```text
spectral_nonnegativity_conditions.md
```

This will analyze the conditions under which the self-adjoint radial operator has nonnegative spectrum.

---

# Status

This document establishes the conditional self-adjoint realization framework for the TIG3 radial operator.