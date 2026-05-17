# Discriminant–Curvature Relation

## Purpose

This document investigates the mathematical relation between the TIG2 branch discriminant and the TIG3 curvature sector.

The objective is to determine how the algebraic degeneration of the TIG2 branch structure influences the curvature amplification behavior of the representative TIG3 geometry.

This analysis extends the near-critical branch analysis.

---

# TIG2 Discriminant Structure

The TIG2 structural horizon equation is

```text
x^3 - x^2 + beta^3 = 0.
```

Its discriminant is

```text
Delta(beta)
=
beta^3 (4 - 27 beta^3).
```

The critical point occurs at

```text
Delta(beta_c) = 0,
```

with

```text
beta_c^3 = 4/27.
```

The discriminant therefore measures the algebraic separation of admissible horizon branches.

---

# Near-Critical Parameterization

Define

```text
beta^3 = beta_c^3 - delta
```

with

```text
delta > 0
```

small.

Substitution into the discriminant gives

```text
Delta(beta)
=
(beta_c^3 - delta)
(4 - 27(beta_c^3 - delta)).
```

Using

```text
27 beta_c^3 = 4,
```

one obtains

```text
Delta(beta)
=
27 delta (beta_c^3 - delta).
```

Thus, for sufficiently small delta,

```text
Delta(beta)
≈
27 beta_c^3 delta.
```

Since

```text
beta_c^3 = 4/27,
```

we obtain the leading-order scaling law

```text
Delta(beta)
≈
4 delta.
```

Therefore:

```text
delta
~
Delta(beta).
```

The discriminant vanishes linearly in the near-critical regime.

---

# Curvature Amplification

From the TIG3 near-critical curvature analysis:

```text
R(0)
≈
R_crit
[1 + delta/beta_c^3 + O(delta^2)],
```

and

```text
K(0)
≈
K_crit
[1 + 2 delta/beta_c^3 + O(delta^2)].
```

Similarly,

```text
R_ab R^ab(0)
≈
(R_ab R^ab)_crit
[1 + 2 delta/beta_c^3 + O(delta^2)].
```

Using

```text
delta ~ Delta(beta),
```

we obtain:

```text
R(0)
≈
R_crit
[1 + C_R Delta(beta)],
```

and

```text
K(0)
≈
K_crit
[1 + C_K Delta(beta)],
```

for suitable positive constants

```text
C_R, C_K.
```

Thus the curvature amplification scales directly with the discriminant collapse parameter.

---

# Critical Structural Observation

The discriminant collapses at the branch-critical point:

```text
Delta(beta_c) = 0.
```

However:

```text
K(0)|_crit < infinity,
R(0)|_crit < infinity,
R_ab R^ab(0)|_crit < infinity.
```

Therefore the representative TIG3 geometry exhibits:

```text
algebraic criticality
without
curvature divergence.
```

This separates TIG3 from geometries in which branch degeneration forces curvature blow-up.

---

# Scaling Interpretation

Near the critical point:

```text
Delta(beta) -> 0
```

controls:

- branch merger,
- curvature amplification,
- and admissibility sensitivity.

But the curvature sector remains bounded.

Thus the discriminant acts as a structural amplification parameter rather than a singularity generator.

---

# Structural Consequence

The representative TIG3 geometry suggests the following structural picture:

1. branch geometry becomes maximally sensitive near beta_c,
2. curvature invariants increase,
3. admissibility becomes increasingly restrictive,
4. but curvature invariants remain finite.

This supports the interpretation of the near-critical regime as a bounded but highly amplified geometric sector.

---

# Preliminary Proposition

## Proposition — Discriminant-Controlled Curvature Amplification

For the representative TIG3 metric sector,

the near-critical curvature amplification scales with the TIG2 discriminant-collapse parameter while remaining finite at branch criticality.

More precisely:

```text
Delta(beta) -> 0
```

implies amplified but bounded curvature invariants.

Thus the TIG2 branch degeneration does not force curvature singularity formation within the representative TIG3 admissibility sector.

---

# Interpretation

This analysis strengthens the central TIG3 admissibility hypothesis:

```text
branch criticality
does not necessarily imply
geometric singularity.
```

Instead, the discriminant controls the degree of structural amplification of an otherwise bounded curvature sector.

---

# Current Limitations

This result remains restricted to:

- the representative TIG3 metric sector,
- static spherical symmetry,
- and curvature-sector analysis.

The framework still lacks:

- dynamical evolution equations,
- stability operators,
- PDE control,
- and observational verification.

---

# Next Mathematical Steps

The next required steps are:

1. define a radial stability operator,
2. investigate perturbative dynamics,
3. analyze possible metastable relaxation modes,
4. derive admissibility inequalities,
5. formulate rigorous theorem candidates.

---

# Status

This document establishes the first explicit relation between the TIG2 branch discriminant and the TIG3 curvature amplification sector.