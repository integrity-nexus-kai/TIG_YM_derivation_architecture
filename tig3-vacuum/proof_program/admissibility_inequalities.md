# TIG3 Admissibility Inequalities

## Purpose

This document collects the core admissibility inequalities required by the TIG3 vacuum-sector program.

The objective is to condense the current TIG3 framework into a compact set of mathematical conditions that can later serve as assumptions for lemmas, propositions, and theorem candidates.

This document does not prove the TIG3 vacuum program.

It defines the current admissibility inequality structure.

---

# 1. Structural Core Scale

The structural core scale must satisfy

```text
r_c > 0.
```

This condition ensures that the representative TIG3 metric sector does not collapse to the singular Schwarzschild core at the level of the regulated geometry.

---

# 2. Structural Control Parameter

The dimensionless TIG structural parameter is

```text
beta = r_c / (2M).
```

For

```text
M > 0
```

and

```text
r_c > 0,
```

one has

```text
beta > 0.
```

---

# 3. TIG2 Branch Admissibility

The TIG2 horizon branch equation is

```text
x^3 - x^2 + beta^3 = 0.
```

The critical value satisfies

```text
beta_c^3 = 4/27.
```

The branch-admissible subcritical sector is

```text
0 < beta < beta_c.
```

The critical merger occurs at

```text
beta = beta_c.
```

The discriminant is

```text
Delta(beta) = beta^3(4 - 27 beta^3).
```

Thus admissible horizon-branch structure requires

```text
Delta(beta) >= 0.
```

Equivalently,

```text
0 < beta <= beta_c.
```

within the horizon-branch sector.

---

# 4. Representative Metric Sector

The minimal representative TIG3 metric sector is defined by

```text
ds^2 = -F(r)dt^2 + dr^2/F(r) + r^2 dOmega^2
```

with

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

The basic admissibility assumptions are

```text
M > 0,
r_c > 0,
r >= 0.
```

---

# 5. Bounded Kretschmann Sector

The Kretschmann scalar satisfies

```text
K(0) = 96 M^2 / r_c^6.
```

Equivalently,

```text
K(0) = 3 / (2 beta^6 M^4).
```

Thus core boundedness requires

```text
0 < K(0) < infinity.
```

This holds whenever

```text
M > 0,
r_c > 0.
```

---

# 6. Bounded Ricci Scalar Sector

The Ricci scalar core value is

```text
R(0) = 24 M / r_c^3.
```

Equivalently,

```text
R(0) = 3 / (beta^3 M^2).
```

Thus Ricci-scalar admissibility requires

```text
0 < |R(0)| < infinity.
```

This holds whenever

```text
M > 0,
r_c > 0.
```

---

# 7. Bounded Ricci Contraction Sector

The Ricci contraction core value is

```text
R_ab R^ab(0) = 144 M^2 / r_c^6.
```

Equivalently,

```text
R_ab R^ab(0) = 9 / (4 beta^6 M^4).
```

Thus admissibility requires

```text
0 < R_ab R^ab(0) < infinity.
```

This holds whenever

```text
M > 0,
r_c > 0.
```

---

# 8. Combined Curvature Boundedness

The representative TIG3 metric sector satisfies the preliminary bounded-curvature admissibility condition if

```text
sup_r K(r) < infinity,
```

```text
sup_r |R(r)| < infinity,
```

and

```text
sup_r R_ab R^ab(r) < infinity.
```

For the representative metric sector, these conditions are satisfied for

```text
M > 0,
r_c > 0.
```

---

# 9. Critical Curvature Admissibility

At the TIG2 critical branch value

```text
beta_c^3 = 4/27,
```

the core invariants remain finite:

```text
K(0)|_crit = 2187 / (32 M^4),
```

```text
R(0)|_crit = 81 / (4 M^2),
```

and

```text
R_ab R^ab(0)|_crit = 6561 / (64 M^4).
```

Therefore the representative sector satisfies

```text
curvature finite at beta = beta_c.
```

This supports the structural distinction

```text
branch criticality != curvature singularity.
```

---

# 10. Asymptotic GR Conditions

For

```text
r -> infinity,
```

the lapse must satisfy

```text
F(r) = 1 - 2M/r + O(r^-4).
```

The curvature invariants satisfy

```text
K(r) ~ 48 M^2 / r^6,
```

```text
R(r) -> 0,
```

and

```text
R_ab R^ab(r) -> 0.
```

Thus the admissible asymptotic sector requires

```text
lim_{r -> infinity} R(r) = 0,
```

```text
lim_{r -> infinity} R_ab R^ab(r) = 0,
```

and Schwarzschild-compatible falloff.

---

# 11. Perturbative Energy Admissibility

For perturbation modes

```text
psi(t,r),
```

the candidate perturbative energy is

```text
E[psi]
=
1/2 integral
(
|partial_t psi|^2
+
|partial_r_* psi|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

Admissible perturbations require

```text
E[psi] < infinity.
```

---

# 12. Quadratic Form Admissibility

The radial operator quadratic form is

```text
Q[psi]
=
integral
(
|d psi/dr_*|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

A spectral admissibility target is

```text
Q[psi] >= 0
```

for all admissible perturbations

```text
psi in D(L_TIG).
```

This remains a theorem target.

---

# 13. Spectral Nonnegativity

The radial stability operator is

```text
L_TIG = - d^2/dr_*^2 + V_eff(r).
```

The central spectral admissibility condition is

```text
sigma(L_TIG) subset [0, infinity).
```

This excludes exponentially growing linear perturbation modes.

This condition remains unproven.

---

# 14. Self-Adjointness Requirement

The operator

```text
L_TIG
```

must admit a self-adjoint realization on an admissible domain:

```text
D(L_TIG) subset L^2(dr_*).
```

A sufficient route is the Friedrichs extension if the quadratic form is densely defined, closed or closable, and bounded from below.

This remains part of the TIG3 theorem program.

---

# 15. Near-Critical Admissibility

Near

```text
beta approx beta_c,
```

the admissibility sector must preserve:

```text
Delta(beta) >= 0,
```

```text
curvature invariants finite,
```

```text
E[psi] < infinity,
```

and

```text
Q[psi] >= 0
```

where applicable.

This defines the preliminary near-critical admissibility target.

---

# Consolidated TIG3 Inequality System

The current TIG3 admissibility framework is summarized by:

```text
M > 0,
r_c > 0,
beta = r_c/(2M),
0 < beta <= beta_c,
Delta(beta) >= 0,
sup_r K(r) < infinity,
sup_r |R(r)| < infinity,
sup_r R_ab R^ab(r) < infinity,
E[psi] < infinity,
Q[psi] >= 0,
sigma(L_TIG) subset [0, infinity).
```

The first seven conditions are established within the representative curvature sector.

The last three remain perturbative theorem targets.

---

# Explicit Non-Claims

These inequalities do not yet prove:

- nonlinear stability,
- complete singularity exclusion,
- full field equations,
- global causal completeness,
- or observational predictions.

They define the current mathematical admissibility target of TIG3.

---

# Status

This document establishes the current admissibility inequality structure of the TIG3 vacuum-sector program.