# Spectral Admissibility Conditions

## Purpose

This document defines the preliminary spectral admissibility conditions of the TIG3 perturbative stability framework.

The objective is to formulate mathematically controlled conditions under which perturbative spectra associated with the representative TIG3 metric sector remain dynamically admissible.

This extends:

```text
bounded curvature
-> radial stability operator
-> metastable core modes
-> effective potential structure
-> spectral admissibility.
```

The present framework remains preliminary and theorem-oriented.

---

# Starting Point

The TIG3 perturbative framework introduced the radial operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r),
```

acting on admissible perturbation modes

```text
psi(r).
```

The key mathematical question is:

```text
Which spectral sectors correspond to admissible bounded perturbative dynamics?
```

---

# Candidate Hilbert Space

A preliminary admissible perturbation space is

```text
H_TIG = L^2(dr_*),
```

where

```text
dr_*/dr = 1/F(r)
```

defines the tortoise coordinate associated with the representative TIG3 metric sector.

The inner product is formally given by

```text
<psi_1, psi_2>
=
integral psi_1^*(r_*) psi_2(r_*) dr_*.
```

The exact functional setting remains open.

---

# Admissible Perturbation Domain

A candidate admissible domain

```text
D(L_TIG)
```

should satisfy:

1. finite perturbative norm,
2. regularity at the regulated core,
3. asymptotic decay,
4. compatibility with bounded curvature,
5. finite perturbative energy.

Thus admissible perturbations satisfy:

```text
||psi||_L2 < infinity.
```

---

# Energy Admissibility

A candidate perturbative energy functional is

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

The admissibility condition becomes

```text
E[psi] < infinity.
```

Finite-energy perturbations therefore define the admissible spectral sector.

---

# Spectral Stability Criterion

The central spectral admissibility requirement is:

```text
sigma(L_TIG) subset [0, infinity).
```

If this holds, then:

- no exponentially growing linear modes occur,
- perturbative amplitudes remain bounded,
- and admissible relaxation behavior becomes possible.

This is the central TIG3 spectral-stability target.

---

# Exclusion of Instability Modes

Suppose

```text
L_TIG phi = lambda phi.
```

If

```text
lambda < 0,
```

then perturbative solutions behave as

```text
psi(t,r) ~ exp(sqrt(|lambda|) t),
```

which produces exponential instability.

Therefore admissibility requires exclusion of negative spectral sectors.

---

# Continuous and Resonance Sectors

The representative TIG3 operator may admit:

1. continuous scattering spectrum,
2. localized bounded modes,
3. resonance-like metastable sectors,
4. near-critical quasi-bound modes.

Admissibility does not require purely discrete spectrum.

It requires bounded perturbative evolution.

---

# Near-Critical Spectral Effects

The near-critical regime

```text
beta approx beta_c
```

may produce:

- spectral compression,
- effective-potential flattening,
- long-lived resonances,
- delayed relaxation,
- and enhanced metastability.

These effects are expected to occur without curvature divergence in the representative TIG3 geometry.

---

# Relation to Bounded Curvature

The bounded-curvature sector ensures that the background geometry itself remains finite.

Spectral admissibility then asks:

```text
Do perturbations around the bounded background remain dynamically controlled?
```

This completes the transition from geometric admissibility to perturbative admissibility.

---

# Preliminary Spectral Picture

The representative TIG3 geometry suggests the following qualitative structure:

- bounded curvature,
- regulated effective potential,
- admissible perturbative domain,
- nonnegative spectral sector,
- and near-critical metastable relaxation.

This defines the current TIG3 spectral-admissibility hypothesis.

---

# Preliminary Proposition Target

## Proposition — Spectral Admissibility Candidate

If the representative TIG3 radial operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r)
```

is self-adjoint and possesses nonnegative spectrum on an admissible finite-energy domain, then the corresponding perturbative sector admits bounded linear evolution without exponentially growing instability modes.

This remains a theorem target.

---

# Structural Interpretation

Spectral admissibility provides the first operator-theoretic formulation of TIG3 bounded relaxation.

The central idea is:

```text
bounded curvature
+
admissible spectrum
=
bounded perturbative continuation.
```

This is one of the central structural hypotheses of the TIG3 vacuum program.

---

# Current Limitations

This framework does not yet establish:

- self-adjointness proof,
- spectral gap,
- nonlinear stability,
- decay estimates,
- resonance existence,
- or observational predictions.

The present framework is structural and preparatory.

---

# Next Mathematical Steps

The next required steps are:

1. define explicit admissibility inequalities,
2. formulate proposition chains,
3. derive candidate theorem structure,
4. investigate spectral lower bounds,
5. study possible Yang-Mills-type operator analogies,
6. construct the TIG3 admissibility theorem architecture.

---

# Status

This document establishes the preliminary spectral admissibility framework of the TIG3 perturbative stability program.