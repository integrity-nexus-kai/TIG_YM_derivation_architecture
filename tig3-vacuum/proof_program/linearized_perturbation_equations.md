# Linearized Perturbation Equations

## Purpose

This document establishes the preliminary linear perturbation framework for the representative TIG3 vacuum-sector geometry.

The objective is to define the mathematical starting point for deriving:

- perturbative dynamics,
- radial master equations,
- effective potential structure,
- and spectral admissibility conditions.

This document does not yet derive the final perturbation equations.

It defines the perturbative structure and admissible reduction program.

---

# Background Geometry

The representative TIG3 metric sector is

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 d\Omega^2,
```

with lapse function

```text
F(r)
=
1 - \frac{2Mr^2}{r^3 + r_c^3}.
```

The background geometry is:

| Property | Status |
|---|---|
| static | yes |
| spherically symmetric | yes |
| asymptotically Schwarzschild | yes |
| regulated core | yes |
| exact field equations known | no |

The perturbation program therefore operates at the level of a representative admissible geometry.

---

# Perturbative Expansion

Introduce metric perturbations

```text
g_{ab}
\rightarrow
g_{ab} + h_{ab},
```

where

```text
|h_{ab}| \ll 1.
```

Only linear perturbations are considered.

Quadratic and nonlinear perturbative effects are outside the present scope.

---

# Linearization Principle

All equations are expanded to first order in

```text
h_{ab}.
```

Terms of order

```text
O(h^2)
```

are neglected.

The perturbative program therefore studies:

```text
linearized admissible vacuum dynamics.
```

---

# Coordinate Structure

Use coordinates

```text
(t,r,\theta,\phi).
```

The angular sector is represented by the unit two-sphere metric

```text
d\Omega^2
=
d\theta^2
+
\sin^2\theta\, d\phi^2.
```

The radial coordinate remains the areal radius.

---

# Perturbation Decomposition

The perturbations must be decomposed into tensor harmonics on the sphere.

The standard decomposition separates:

| Sector | Parity |
|---|---|
| axial sector | odd parity |
| polar sector | even parity |

This follows the Regge–Wheeler/Zerilli perturbative structure.

---

# Axial Perturbations

Axial perturbations transform with odd parity under

```text
(\theta,\phi)
\rightarrow
(\pi-\theta,\phi+\pi).
```

The axial sector is typically algebraically simpler and should be analyzed first.

Candidate perturbative components include:

```text
h_{t\phi},
h_{r\phi},
h_{t\theta},
h_{r\theta}.
```

after angular harmonic decomposition.

---

# Polar Perturbations

Polar perturbations transform with even parity.

Candidate perturbative components include:

```text
h_{tt},
h_{tr},
h_{rr},
h_{\theta\theta},
h_{\phi\phi}.
```

The polar sector is expected to be more complicated due to coupling structure.

---

# Gauge Structure

The perturbation system possesses gauge freedom under infinitesimal coordinate transformations

```text
x^a
\rightarrow
x^a + \xi^a.
```

Under such transformations,

```text
h_{ab}
\rightarrow
h_{ab}
-
\nabla_a \xi_b
-
\nabla_b \xi_a.
```

A gauge reduction procedure is therefore required.

---

# Candidate Gauge Approaches

Possible reduction strategies include:

| Method | Role |
|---|---|
| Regge–Wheeler gauge | classical reduction |
| gauge-invariant variables | coordinate-independent structure |
| admissible gauge fixing | TIG3-compatible reduction |

The exact reduction structure remains open.

---

# Linearized Geometric Quantities

The perturbation program requires computation of:

| Quantity | Role |
|---|---|
| linearized Christoffel symbols | connection perturbation |
| linearized Ricci tensor | curvature perturbation |
| linearized Ricci scalar | trace structure |
| linearized Einstein tensor | dynamical reduction candidate |

The exact governing field equations remain unspecified.

Therefore the perturbative reduction is currently geometric rather than fully covariant.

---

# Representative Reduction Strategy

The working reduction philosophy is:

```text
background geometry
→ perturbation decomposition
→ gauge reduction
→ radial master equation.
```

This is structurally analogous to classical black-hole perturbation theory.

---

# Tortoise Coordinate

Introduce the tortoise coordinate

```text
dr_*/dr = 1/F(r).
```

This coordinate is expected to simplify the radial perturbation structure and permit Schrödinger-type reduction.

The global structure of

```text
r_*
```

depends on admissible horizon branches.

---

# Candidate Master Equation Structure

The long-term reduction target is an equation of the form

```text
\partial_t^2\Psi
-
\partial_{r_*}^2\Psi
+
V_{eff}(r)\Psi
=
0.
```

The current document does not derive this equation.

It defines the perturbative pathway toward it.

---

# Near-Core Perturbative Structure

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

Thus the core geometry behaves approximately like a regulated de Sitter-type sector.

Key perturbative questions include:

- regularity of perturbation modes,
- boundedness of effective potential terms,
- admissible boundary behavior,
- and spectral regularity near the core.

---

# Asymptotic Structure

For

```text
r \to \infty,
```

the geometry approaches Schwarzschild-compatible asymptotics.

Therefore the perturbation equations should asymptotically reduce to standard black-hole perturbative structure.

This acts as a consistency requirement.

---

# Near-Critical Sector

The regime

```text
\beta \approx \beta_c
```

may produce:

- tortoise stretching,
- near-horizon branch merger,
- effective-potential flattening,
- and slow perturbative relaxation.

This regime likely requires separate asymptotic treatment.

---

# Admissibility Requirements

Candidate admissible perturbations should satisfy:

| Condition | Purpose |
|---|---|
| finite perturbation norm | spectral admissibility |
| finite energy | perturbative consistency |
| regularity at core | bounded continuation |
| asymptotic decay | GR compatibility |

These conditions remain preliminary.

---

# Expected Mathematical Obstacles

The perturbative program is expected to face several major difficulties:

| Problem | Status |
|---|---|
| exact field equations absent | unresolved |
| gauge reduction | open |
| polar-sector coupling | open |
| near-critical asymptotics | open |
| master-variable construction | open |
| spectral positivity | open |

---

# Explicit Non-Claims

This document does not establish:

- exact perturbation equations,
- gauge-invariant master variables,
- effective-potential uniqueness,
- spectral stability,
- nonlinear evolution,
- or singularity exclusion.

The framework remains preliminary.

---

# Strategic Interpretation

The perturbative program should be interpreted as:

```text
linearized admissible vacuum dynamics.
```

within a representative regulated gravitational vacuum sector.

It is not yet a complete gravitational field theory.

---

# Relation to Existing TIG3 Structure

This document connects:

```text
curvature admissibility
→ perturbative geometry
→ gauge reduction
→ radial operator structure.
```

It therefore marks the transition from geometric admissibility toward operator-theoretic dynamics.

---

# Next Required Step

The next mathematical step is:

```text
gauge reduction program.
```

This is required before the radial master equation can be rigorously constructed.

---

# Status

This document establishes the preliminary linear perturbation framework for the TIG3 vacuum-sector program.