# Self-Adjointness Program

## Purpose

This document defines the preliminary self-adjointness program for the TIG3 radial stability operator.

The objective is to convert the formal perturbative operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r)
```

from a symbolic stability expression into a mathematically controlled operator-theoretic object.

This is a prerequisite for rigorous spectral admissibility, bounded linear evolution, and metastable-mode analysis.

---

# Starting Point

The TIG3 perturbative framework introduced the radial equation

```text
partial_t^2 psi + L_TIG psi = 0
```

with

```text
L_TIG = - d^2/dr_*^2 + V_eff(r).
```

Here the tortoise coordinate is defined by

```text
dr_*/dr = 1/F(r),
```

where

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

The current task is to specify the operator domain and determine under what conditions L_TIG becomes self-adjoint.

---

# Candidate Hilbert Space

The preliminary Hilbert space is

```text
H_TIG = L^2(I, dr_*),
```

where I is the admissible radial interval expressed in the tortoise coordinate.

Depending on the branch sector, I may be:

```text
I = R
```

for a full exterior-type tortoise domain, or a restricted admissible interval determined by horizon/core boundary structure.

The inner product is

```text
<psi, phi>
=
integral_I psi^*(r_*) phi(r_*) dr_*.
```

---

# Minimal Operator Definition

Define the formal differential expression

```text
tau[psi]
=
- d^2 psi/dr_*^2 + V_eff(r) psi.
```

The minimal TIG3 operator is first defined on smooth compactly supported test functions:

```text
L_min psi = tau[psi],
D(L_min) = C_c^infinity(I).
```

This operator is symmetric if V_eff(r) is real-valued on the admissible interval.

---

# Symmetry Condition

For psi, phi in C_c^infinity(I),

```text
<psi, L_min phi> - <L_min psi, phi>
=
[ psi^* phi' - (psi^*)' phi ]_{boundary}.
```

Since compactly supported functions vanish at the boundary, the boundary form is zero.

Thus:

```text
L_min is symmetric
```

provided

```text
V_eff(r) real-valued.
```

---

# Self-Adjointness Problem

A symmetric operator is not necessarily self-adjoint.

The key mathematical problem is to determine whether:

```text
L_min = L_min^*
```

or whether one must choose a self-adjoint extension.

The TIG3 self-adjointness program therefore requires:

1. endpoint classification,
2. boundary condition analysis,
3. closure of the minimal operator,
4. deficiency-index calculation or equivalent criteria,
5. construction of admissible self-adjoint extensions.

---

# Endpoint Structure

The admissible endpoints may include:

1. regulated core endpoint,
2. horizon endpoints,
3. spatial infinity,
4. near-critical merged-horizon limits.

Each endpoint must be classified as:

```text
limit-point
```

or

```text
limit-circle
```

in the sense of one-dimensional Sturm-Liouville theory.

---

# Limit-Point / Limit-Circle Criterion

For operators of the form

```text
-d^2/dr_*^2 + V_eff(r),
```

self-adjointness depends on the behavior of solutions to

```text
L_TIG psi = lambda psi
```

near the endpoints.

If an endpoint is limit-point, no boundary condition is required there.

If an endpoint is limit-circle, one admissible boundary condition must be imposed.

The TIG3 admissibility program must determine which case occurs at:

- the regulated core,
- the exterior asymptotic region,
- and near-critical branch endpoints.

---

# Core Boundary Behavior

The bounded-curvature analysis suggests that the representative TIG3 core is geometrically regular for

```text
r_c > 0.
```

Therefore the core endpoint should admit regular perturbative boundary behavior.

Candidate admissibility conditions include:

```text
psi finite at the core,
```

and

```text
E[psi] < infinity.
```

A possible regularity boundary condition is:

```text
d psi/dr_* = 0
```

at the symmetry center, although this must be derived from the actual admissible radial interval.

This is not yet fixed.

---

# Asymptotic Boundary Behavior

For large radius,

```text
r -> infinity,
```

the representative TIG3 geometry approaches Schwarzschild-compatible asymptotics.

Admissible perturbations should therefore satisfy one of:

```text
psi in L^2(dr_*),
```

or outgoing/scattering boundary conditions depending on the spectral problem.

For stability theory, finite-energy conditions are primary.

---

# Quadratic Form

A natural quadratic form associated with the radial operator is

```text
Q[psi]
=
integral_I
(
|d psi/dr_*|^2
+
V_eff(r) |psi|^2
)
dr_*.
```

If the quadratic form is:

1. densely defined,
2. closed or closable,
3. bounded from below,

then it defines a self-adjoint Friedrichs extension.

This provides a possible rigorous route to spectral admissibility.

---

# Friedrichs Extension Route

If

```text
Q[psi] >= -C ||psi||^2
```

for some finite constant C, then the Friedrichs construction yields a self-adjoint operator associated with the closed form.

If additionally

```text
Q[psi] >= 0,
```

then the resulting operator is nonnegative.

This would imply:

```text
sigma(L_TIG) subset [0, infinity).
```

That would establish the desired linear spectral admissibility condition.

---

# Near-Critical Issues

The regime

```text
beta approx beta_c
```

may cause:

- effective-potential flattening,
- horizon-branch merger,
- long tortoise-coordinate stretching,
- slow relaxation,
- and possible resonance-like sectors.

These effects may complicate self-adjointness and spectral estimates.

The near-critical case should therefore be treated separately.

---

# Preliminary Proposition Target

## Proposition - Self-Adjointness Candidate

If V_eff(r) is real-valued, locally integrable on the admissible radial interval, and the associated quadratic form is closed and bounded from below on the chosen admissible domain, then L_TIG admits a self-adjoint realization.

If the quadratic form is nonnegative, the corresponding spectrum is nonnegative.

This remains a theorem target.

---

# Current Mathematical Obstacles

The TIG3 program must still determine:

1. explicit V_eff(r),
2. exact admissible radial interval,
3. endpoint classification,
4. boundary conditions,
5. Friedrichs-extension applicability,
6. spectral lower bounds,
7. near-critical spectral behavior.

---

# Structural Interpretation

Self-adjointness is the mathematical condition that turns the TIG3 radial stability operator into a legitimate spectral object.

Without self-adjointness, claims about:

- stable modes,
- resonance sectors,
- spectral admissibility,
- and bounded perturbative evolution

remain formal only.

---

# Explicit Restrictions

This document does not prove:

- self-adjointness,
- spectral nonnegativity,
- nonlinear stability,
- resonance existence,
- or bounded evolution.

It defines the required operator-theoretic program.

---

# Status

This document establishes the self-adjointness roadmap for the TIG3 radial stability operator.