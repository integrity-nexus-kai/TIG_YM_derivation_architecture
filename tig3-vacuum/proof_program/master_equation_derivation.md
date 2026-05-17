# Master Equation Derivation

## Purpose

This document defines the derivation framework for the reduced TIG3 perturbation master equation.

The objective is to derive a radial Schrödinger-type perturbation equation from the gauge-reduced TIG3 perturbative system.

This equation is intended to provide the mathematical bridge between:

- perturbative geometry,
- effective potential structure,
- radial operator theory,
- and spectral admissibility analysis.

This document establishes the derivation structure but does not yet provide a complete rigorous reduction.

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

The geometry is:

| Property | Status |
|---|---|
| static | yes |
| spherically symmetric | yes |
| asymptotically Schwarzschild | yes |
| regulated core | yes |

---

# Perturbative Starting Point

The perturbative expansion is

```text
g_{ab}
\rightarrow
g_{ab}+h_{ab},
```

with

```text
|h_{ab}| \ll 1.
```

The perturbations are decomposed into:

| Sector | Parity |
|---|---|
| axial | odd |
| polar | even |

Gauge reduction is assumed to have been performed.

---

# Central Reduction Objective

The master-equation program seeks a reduced perturbative variable

```text
\Psi(t,r),
```

satisfying an equation of the form

```text
\partial_t^2\Psi
-
\partial_{r_*}^2\Psi
+
V_{eff}(r)\Psi
=
0.
```

This is the central perturbative target of the TIG3 vacuum program.

---

# Tortoise Coordinate

Introduce the tortoise coordinate

```text
dr_*/dr = 1/F(r).
```

The coordinate transformation is intended to:

- regularize radial wave propagation,
- simplify horizon behavior,
- and reduce the perturbation system into Schrödinger form.

The global structure of

```text
r_*
```

depends on admissible branch geometry.

---

# Separation Ansatz

Introduce the mode decomposition

```text
\Psi(t,r,\theta,\phi)
=
e^{-i\omega t}
Y_{\ell m}(\theta,\phi)
\psi(r).
```

This separates:

| Variable | Sector |
|---|---|
| time | oscillatory dynamics |
| angular sector | tensor harmonics |
| radial sector | operator structure |

The resulting radial equation becomes the central object of analysis.

---

# Radial Reduction Structure

After gauge reduction and angular decomposition, the perturbative equations are expected to reduce schematically to

```text
\frac{d^2\psi}{dr_*^2}
+
\left(
\omega^2
-
V_{eff}(r)
\right)\psi
=
0.
```

This is structurally analogous to Regge–Wheeler/Zerilli systems.

The explicit derivation remains open.

---

# Effective Potential Structure

The candidate effective potential takes the schematic form

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

The correction structure

```text
U(r)
```

is expected to encode:

- radial curvature structure,
- near-core regularization,
- and near-critical deformation effects.

---

# Expected Potential Contributions

The effective potential is expected to contain contributions from:

| Contribution | Role |
|---|---|
| angular barrier | centrifugal structure |
| radial curvature | background geometry |
| core regularization | bounded continuation |
| branch deformation | TIG2 critical structure |

The explicit coefficient structure remains unresolved.

---

# Near-Core Reduction

For

```text
r \ll r_c,
```

the lapse behaves approximately as

```text
F(r)
\approx
1 - (2M/r_c^3)r^2.
```

Thus the near-core perturbation equation is expected to resemble a regulated de Sitter-type wave equation.

Key questions include:

- regularity of solutions,
- boundedness of effective potential,
- admissible boundary behavior,
- and spectral regularity.

---

# Asymptotic Reduction

For

```text
r \to \infty,
```

the geometry approaches Schwarzschild asymptotics.

The master equation should therefore asymptotically reduce to standard black-hole perturbative structure.

This acts as a consistency requirement.

---

# Near-Critical Reduction

Near

```text
\beta \approx \beta_c,
```

the radial structure may exhibit:

- tortoise stretching,
- potential flattening,
- slow perturbative decay,
- metastable trapping,
- and resonance compression.

This regime likely requires separate asymptotic treatment.

---

# Radial Operator Construction

The reduced radial equation defines the formal operator

```text
L_{TIG}
=
- \frac{d^2}{dr_*^2}
+
V_{eff}(r).
```

This operator forms the basis for:

- spectral analysis,
- self-adjointness studies,
- quadratic-form analysis,
- and bounded-evolution investigations.

---

# Perturbative Energy Structure

The associated perturbative energy functional is expected to take the form

```text
E[\Psi]
=
\frac12
\int
\left(
|\partial_t\Psi|^2
+
|\partial_{r_*}\Psi|^2
+
V_{eff}(r)|\Psi|^2
\right)
dr_*.
```

Admissibility requires finite perturbative energy.

---

# Candidate Spectral Problem

The radial reduction produces the spectral problem

```text
L_{TIG}\psi
=
\omega^2\psi.
```

The central spectral admissibility question becomes:

```text
\sigma(L_{TIG})
\subset
[0,\infty)?
```

This remains unresolved.

---

# Expected Mathematical Obstacles

The derivation program faces several major open problems:

| Problem | Status |
|---|---|
| exact field equations absent | unresolved |
| explicit gauge reduction | incomplete |
| polar-sector coupling | open |
| explicit \(V_{eff}\) coefficients | open |
| endpoint regularity | open |
| spectral positivity | open |

---

# Conservative Mathematical Position

The current derivation framework does not establish:

- rigorous master-equation uniqueness,
- exact effective-potential structure,
- spectral stability,
- nonlinear perturbative control,
- or complete vacuum stability.

The framework remains a perturbative admissibility program.

---

# Strategic Interpretation

The master-equation derivation represents the transition from:

```text
gauge-reduced perturbations
```

to:

```text
operator-theoretic radial dynamics.
```

This is the central mathematical bridge of the TIG3 perturbative framework.

---

# Relation to Existing TIG3 Structure

This document connects:

```text
linear perturbations
→ gauge reduction
→ master equation
→ effective potential
→ radial operator theory
→ spectral analysis.
```

It therefore defines the entry point into rigorous perturbative operator analysis.

---

# Next Required Step

The next mathematical target is:

```text
explicit effective potential structure.
```

This is required before self-adjointness and spectral positivity can be rigorously investigated.

---

# Status

This document establishes the master-equation derivation framework for the TIG3 vacuum-sector perturbation program.