# Explicit Effective Potential Structure

## Purpose

This document develops the explicit candidate structure of the TIG3 effective perturbation potential

```text
V_{eff}(r).
```

The objective is to move beyond the purely schematic perturbative framework and identify the geometric contributions expected to govern the reduced radial perturbation dynamics.

This document does not yet establish a unique rigorously derived potential.

It defines the current admissible candidate structure for the TIG3 vacuum-sector program.

---

# Background Geometry

The representative TIG3 vacuum-sector geometry is

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 d\Omega^2,
```

with

```text
F(r)
=
1 - \frac{2Mr^2}{r^3 + r_c^3}.
```

The geometry satisfies:

| Property | Status |
|---|---|
| static | yes |
| spherically symmetric | yes |
| asymptotically Schwarzschild | yes |
| bounded curvature sector | yes |

---

# Perturbative Reduction Target

The reduced perturbative equation is assumed to take the form

```text
\partial_t^2\Psi
-
\partial_{r_*}^2\Psi
+
V_{eff}(r)\Psi
=
0,
```

where the tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

The goal is to identify the explicit structure of

```text
V_{eff}(r).
```

---

# Structural Requirements

The effective potential must satisfy several consistency conditions.

---

# Requirement A — Asymptotic Schwarzschild Recovery

For

```text
r \to \infty,
```

the geometry approaches Schwarzschild form.

Therefore:

```text
V_{eff}(r)
\to
V_{Schwarzschild}(r).
```

This is a mandatory consistency condition.

---

# Requirement B — Near-Core Regularity

For

```text
r \ll r_c,
```

the potential must remain finite.

Specifically:

```text
|V_{eff}(r)| < \infty.
```

This excludes the singular Schwarzschild-type divergence at

```text
r = 0.
```

---

# Requirement C — Radial Admissibility

The potential should admit:

- finite perturbative energy,
- admissible Hilbert-space structure,
- and controlled radial evolution.

This constrains the admissible growth behavior of:

```text
V_{eff}(r).
```

---

# Requirement D — Near-Critical Regularity

Near

```text
\beta \approx \beta_c,
```

the potential should remain structurally controlled.

Potential flattening or branch deformation may occur, but curvature singularities should remain absent within the representative sector.

---

# Candidate Potential Structure

The current candidate structure is

```text
V_{eff}(r)
=
F(r)
\left[
\frac{\ell(\ell+1)}{r^2}
+
U(r)
\right].
```

The decomposition separates:

| Contribution | Interpretation |
|---|---|
| angular barrier | centrifugal structure |
| \(U(r)\) | geometric correction sector |

---

# Angular Barrier

The angular contribution is

```text
V_{ang}(r)
=
F(r)\frac{\ell(\ell+1)}{r^2}.
```

This reproduces the standard centrifugal structure of black-hole perturbation theory.

---

# Geometric Correction Sector

The correction term

```text
U(r)
```

encodes:

- radial curvature structure,
- near-core regularization,
- and TIG2 branch deformation effects.

---

# Candidate Radial Contribution

The simplest admissible radial contribution is expected to involve

```text
F'(r)/r.
```

Motivation:

| Quantity | Role |
|---|---|
| \(F'(r)\) | radial geometric variation |
| \(1/r\) | spherical reduction factor |

This mirrors classical Regge–Wheeler-type structure.

---

# Explicit Derivative Structure

For

```text
F(r)
=
1 - \frac{2Mr^2}{r^3+r_c^3},
```

one obtains

```text
F'(r)
=
\frac{2Mr(r^3-2r_c^3)}{(r^3+r_c^3)^2}.
```

This quantity remains finite for:

```text
r_c > 0.
```

---

# Preliminary Effective Potential

The resulting candidate potential becomes

```text
V_{eff}(r)
=
F(r)
\left[
\frac{\ell(\ell+1)}{r^2}
+
\frac{F'(r)}{r}
\right].
```

Equivalently,

```text
V_{eff}(r)
=
F(r)
\left[
\frac{\ell(\ell+1)}{r^2}
+
\frac{
2M(r^3-2r_c^3)
}{
(r^3+r_c^3)^2
}
\right].
```

This is currently the leading admissible candidate structure.

---

# Near-Core Expansion

For

```text
r \ll r_c,
```

the lapse satisfies

```text
F(r)
\approx
1 - (2M/r_c^3)r^2.
```

Then:

```text
F'(r)/r
\approx
-4M/r_c^3.
```

Thus the geometric contribution remains finite.

---

# Near-Core Potential Behavior

Near the regulated core:

```text
V_{eff}(r)
\sim
\frac{\ell(\ell+1)}{r^2}
+
O(1).
```

The angular sector remains singular for:

```text
\ell > 0,
```

but the radial geometric contribution itself remains finite.

The admissibility implications require further analysis.

---

# S-Wave Sector

For

```text
\ell = 0,
```

the angular barrier vanishes.

The potential reduces approximately to a finite constant near the core.

This sector is likely the most important for spectral admissibility analysis.

---

# Asymptotic Expansion

For

```text
r \to \infty,
```

one obtains

```text
F(r)
=
1 - 2M/r + O(r^{-4}),
```

and

```text
F'(r)/r
=
2M/r^3 + O(r^{-6}).
```

Thus:

```text
V_{eff}(r)
```

recovers Schwarzschild-compatible asymptotics.

---

# Near-Critical Structure

Near

```text
\beta \approx \beta_c,
```

the horizon structure may induce:

- effective-potential flattening,
- broadened barrier regions,
- slow radial propagation,
- and metastable trapping sectors.

These effects remain exploratory.

---

# Candidate Operator

The resulting formal radial operator is

```text
L_{TIG}
=
-
\frac{d^2}{dr_*^2}
+
V_{eff}(r).
```

This operator forms the basis for:

- endpoint classification,
- quadratic-form analysis,
- self-adjointness studies,
- and spectral admissibility.

---

# Important Limitation

The present effective potential is:

```text
candidate-level,
not uniquely derived.
```

The explicit perturbative reduction remains incomplete.

The current structure should therefore be interpreted as:

```text
leading admissible perturbative model.
```

---

# Expected Mathematical Questions

The following problems remain open:

| Problem | Status |
|---|---|
| uniqueness of \(V_{eff}\) | open |
| polar-sector corrections | open |
| near-critical asymptotics | open |
| positivity properties | open |
| endpoint regularity | open |
| resonance accumulation | open |

---

# Conservative Mathematical Position

This document does not establish:

- exact perturbative closure,
- unique effective dynamics,
- spectral positivity,
- nonlinear stability,
- or complete vacuum regularity.

The framework remains perturbative and representative.

---

# Strategic Interpretation

The explicit effective-potential structure represents the transition from:

```text
formal perturbative architecture
```

to:

```text
explicit radial operator analysis.
```

This is the first point where TIG3 acquires a concrete operator-theoretic structure.

---

# Relation to Existing TIG3 Structure

This document connects:

```text
master equation
→ effective potential
→ radial operator
→ spectral admissibility
→ bounded evolution.
```

It therefore acts as the mathematical entry point into rigorous spectral analysis.

---

# Next Required Step

The next mathematical step is:

```text
endpoint classification.
```

This is required before quadratic-form analysis and self-adjointness studies become rigorous.

---

# Status

This document establishes the explicit candidate effective-potential structure for the TIG3 vacuum-sector perturbation framework.