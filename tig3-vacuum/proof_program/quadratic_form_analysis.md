# Quadratic Form Analysis

## Purpose

This document develops the quadratic-form framework associated with the TIG3 radial stability operator.

The objective is to determine whether the perturbative operator admits a mathematically admissible energy structure suitable for:

- self-adjoint realization,
- bounded spectral analysis,
- and perturbative stability investigations.

This document is part of the six-file TIG3 proof-closing sequence.

It follows the endpoint-classification framework and prepares the self-adjoint realization program.

---

# Starting Point

The formal TIG3 radial operator is

```text
L_TIG
=
-
d^2/dr_*^2
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

The tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

The perturbative spectral problem is

```text
L_TIG psi = omega^2 psi.
```

---

# Goal of Quadratic Form Analysis

The objective is to define the quadratic form associated with

```text
L_TIG
```

and determine whether it is:

| Property | Purpose |
|---|---|
| densely defined | operator construction |
| symmetric | admissibility |
| closable | self-adjoint extension |
| bounded from below | spectral control |
| nonnegative | perturbative stability |

---

# Candidate Hilbert Space

The natural perturbative Hilbert space is

```text
H_TIG = L^2(I,dr_*),
```

where:

- \(I\) is the admissible tortoise interval,
- and endpoint behavior is determined by the classification program.

---

# Minimal Operator Domain

The minimal operator is initially defined on

```text
D(L_min)
=
C_c^\infty(I).
```

This ensures:

- smoothness,
- compact support,
- and avoidance of boundary ambiguities.

---

# Quadratic Form Definition

The associated quadratic form is

```text
Q[psi]
=
int
(
|d psi/dr_*|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

This form is formally associated with:

```text
L_TIG.
```

---

# Symmetry Structure

If

```text
V_eff(r)
```

is real-valued, then:

```text
Q[psi]
```

is formally symmetric.

The current candidate potential satisfies this property within the representative TIG3 sector.

---

# Near-Core Analysis

For

```text
r << r_c,
```

the potential behaves as

```text
V_eff(r)
~
ell(ell+1)/r^2
+
O(1).
```

Thus:

| Sector | Near-core structure |
|---|---|
| \(ell=0\) | finite |
| \(ell>0\) | inverse-square singularity |

---

# Inverse-Square Structure

The inverse-square term is critical for functional analysis.

Operators of the form

```text
-d^2/dr^2 + c/r^2
```

can exhibit:

- essential self-adjointness,
- deficiency subspaces,
- or instability,

depending on the coefficient \(c\).

---

# Angular Sector Coefficient

In the TIG3 potential,

```text
c = ell(ell+1).
```

Since:

```text
ell(ell+1) >= 0,
```

the angular barrier is nonnegative.

This strongly suggests absence of attractive inverse-square instability.

---

# S-Wave Sector

For

```text
ell = 0,
```

the singular angular contribution vanishes.

Near the core:

```text
V_eff(r)
≈ constant.
```

Thus the s-wave sector is expected to admit a regular quadratic-form structure.

---

# Horizon Behavior

At simple horizons,

```text
F(r_H)=0.
```

Since:

```text
V_eff(r)
=
F(r)[...],
```

the effective potential vanishes at the horizon if the bracket remains finite.

Thus the horizon contributes asymptotically free-wave behavior.

---

# Asymptotic Infinity

For

```text
r -> infinity,
```

the potential behaves as

```text
V_eff(r)
~
ell(ell+1)/r^2
+
O(r^-3).
```

This decay is sufficiently mild to suggest standard asymptotically admissible behavior.

---

# Lower-Boundedness Question

The key functional-analytic question is whether

```text
Q[psi]
>=
-C ||psi||^2
```

for some finite constant \(C\).

This is required for:

- closability,
- Friedrichs extension,
- and spectral control.

---

# Candidate Positivity Structure

The gradient term

```text
int |d psi/dr_*|^2 dr_*
```

is manifestly nonnegative.

The main issue is therefore the sign structure of:

```text
V_eff(r).
```

---

# Geometric Contribution Sign

The correction term

```text
F'(r)/r
=
2M(r^3-2r_c^3)/(r^3+r_c^3)^2
```

changes sign near:

```text
r^3 = 2r_c^3.
```

Therefore the geometric sector is not manifestly positive everywhere.

However:

- the correction remains finite,
- localized,
- and asymptotically decaying.

This suggests possible bounded-below behavior.

---

# Candidate Bounded-Below Statement

The current evidence suggests the conjectural estimate

```text
Q[psi]
>=
-C ||psi||^2
```

for admissible perturbations.

This is not yet proven.

---

# Closability Question

A second major issue is whether the quadratic form is closable on the admissible perturbation domain.

Closability is required before constructing a closed self-adjoint operator associated with:

```text
Q[psi].
```

This remains open.

---

# Friedrichs Extension Program

If the quadratic form is:

- densely defined,
- symmetric,
- closable,
- and bounded from below,

then the Friedrichs construction yields a canonical self-adjoint operator.

This is the central next objective.

---

# Near-Critical Regime

Near

```text
beta ≈ beta_c,
```

additional difficulties may arise:

- flattened potential regions,
- near-zero trapping sectors,
- resonance accumulation,
- and slow spectral decay.

These effects may complicate lower-bound estimates.

---

# Candidate Admissibility Structure

The current perturbative framework suggests the following admissibility hierarchy:

| Property | Status |
|---|---|
| finite perturbative energy | plausible |
| lower-bounded quadratic form | plausible |
| nonnegative spectrum | unresolved |
| essential self-adjointness | unresolved |
| bounded evolution | unresolved |

---

# Relation to Existing TIG3 Structure

This file connects:

```text
endpoint classification
→ quadratic form
→ Friedrichs extension
→ self-adjoint realization
→ spectral admissibility.
```

It therefore acts as the functional-analytic bridge toward rigorous operator construction.

---

# Current Limitations

This document does not yet prove:

- lower boundedness,
- closability,
- self-adjointness,
- spectral positivity,
- or perturbative stability.

It establishes the quadratic-form analysis program only.

---

# Next Required Step

The next mathematical step is:

```text
self_adjoint_realization.md
```

This will attempt to construct a mathematically admissible self-adjoint operator associated with the TIG3 perturbation problem.

---

# Status

This document establishes the quadratic-form analysis framework for the TIG3 radial operator program.