# Effective Potential Structure

## Purpose

This document defines the preliminary effective-potential structure associated with the TIG3 radial stability operator.

The objective is to provide the first explicit mathematical framework for:

- spectral analysis,
- perturbative stability,
- metastable relaxation,
- and near-critical mode behavior

within the representative TIG3 metric sector.

The present analysis remains preliminary and structural.

---

# Starting Point

The representative TIG3 metric sector is

```text
ds^2 = -F(r) dt^2 + dr^2/F(r) + r^2 dOmega^2
```

with lapse function

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

The radial perturbation framework introduced the operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r),
```

where the tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

The remaining task is to characterize the effective potential structure.

---

# Minimal Effective Potential Ansatz

A minimal admissible spherically symmetric stability potential takes the schematic form

```text
V_eff(r)
=
F(r)
[
l(l+1)/r^2
+
F'(r)/r
+
mu_eff(r)
].
```

Here:

- l denotes the angular mode index,
- F(r) is the TIG3 lapse function,
- mu_eff(r) is an effective structural correction sector.

This ansatz is motivated by standard black-hole perturbation structures but remains heuristic.

---

# TIG3 Structural Contribution

Using

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3),
```

one obtains

```text
F'(r)
=
2 M r (r^3 - 2 r_c^3)/(r^3 + r_c^3)^2.
```

Therefore the TIG3 geometry modifies the effective potential through:

1. regulated near-core geometry,
2. branch-sensitive deformation,
3. curvature-dependent flattening,
4. and near-critical amplification.

---

# Near-Core Structure

For

```text
r << r_c,
```

the lapse behaves approximately as

```text
F(r)
≈
1 - (2M/r_c^3) r^2.
```

Thus the near-core region resembles a regulated de Sitter-like sector.

Substitution into the effective potential gives

```text
V_eff(r)
≈
(1 - alpha r^2)
[
l(l+1)/r^2
- 2 alpha
+
mu_eff(r)
],
```

with

```text
alpha = 2M/r_c^3.
```

Hence the core sector does not exhibit the singular Schwarzschild divergence.

This is essential for bounded perturbative dynamics.

---

# Asymptotic Structure

For

```text
r -> infinity,
```

the lapse satisfies

```text
F(r)
≈
1 - 2M/r.
```

Thus the effective potential approaches the standard asymptotic Schwarzschild form:

```text
V_eff(r)
~
l(l+1)/r^2.
```

Therefore the representative TIG3 sector preserves asymptotic GR-compatible perturbation behavior.

---

# Near-Critical Flattening

The regime

```text
beta approx beta_c
```

may induce qualitative flattening of the effective potential.

Possible consequences include:

- weaker restoring force,
- longer-lived perturbative modes,
- metastable localization,
- and enhanced relaxation times.

This provides the first mathematical mechanism for TIG3 near-critical breathing behavior.

---

# Spectral Interpretation

The radial operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r)
```

may admit several possible spectral sectors:

1. continuous scattering spectrum,
2. localized bounded modes,
3. resonance-like metastable modes,
4. near-critical quasi-bound sectors.

The existence of such sectors remains unproven.

---

# Admissibility Conditions

A candidate admissible perturbation sector should satisfy:

1. finite energy,
2. regularity at the regulated core,
3. asymptotic decay,
4. bounded perturbative norm,
5. compatibility with the TIG2 branch structure.

Possible admissible states belong to

```text
L^2(dr_*).
```

The exact Hilbert-space structure remains open.

---

# Preliminary Stability Picture

The representative TIG3 geometry suggests the following qualitative structure:

- the core geometry remains bounded,
- the effective potential is regulated,
- near-critical flattening may enhance metastability,
- but no curvature singularity appears at the branch-critical point.

This supports the TIG3 admissibility interpretation of bounded high-curvature continuation.

---

# Preliminary Proposition Target

## Proposition — Regulated Effective Potential Sector

For the representative TIG3 metric sector, the effective radial perturbation potential remains finite in the regulated core region and asymptotically approaches the Schwarzschild perturbation structure.

Furthermore, near-critical branch deformation may induce effective-potential flattening associated with metastable relaxation behavior.

This is currently a structural theorem target.

---

# Relation to Previous Results

This document extends:

```text
bounded curvature
-> radial stability operator
-> metastable core modes
-> effective spectral structure.
```

The effective potential therefore acts as the central bridge between geometry and dynamics.

---

# Current Limitations

The present framework does not yet provide:

- exact perturbation derivation,
- self-adjoint spectral proof,
- resonance construction,
- nonlinear stability,
- decay estimates,
- or observational predictions.

The effective potential remains a preliminary structural model.

---

# Next Mathematical Steps

The next required steps are:

1. derive explicit perturbation equations,
2. compute candidate spectra numerically,
3. analyze near-critical resonance scaling,
4. study spectral lower bounds,
5. formulate admissibility inequalities,
6. investigate possible operator-theoretic links to Yang-Mills-type spectral structure.

---

# Status

This document establishes the first effective-potential framework of the TIG3 perturbative stability program.