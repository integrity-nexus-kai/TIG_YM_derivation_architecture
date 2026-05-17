# Gauge Reduction Program

## Purpose

This document defines the gauge-reduction framework for the TIG3 linear perturbation program.

The objective is to reduce the raw metric perturbation system into a smaller set of admissible dynamical degrees of freedom suitable for:

- master-equation construction,
- effective-potential derivation,
- radial operator analysis,
- and spectral admissibility studies.

This document does not yet complete the reduction.

It establishes the mathematical reduction program.

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

The background geometry is:

| Property | Status |
|---|---|
| static | yes |
| spherically symmetric | yes |
| asymptotically Schwarzschild | yes |
| regulated core | yes |

The perturbation reduction therefore follows a Regge–Wheeler-type structural strategy.

---

# Perturbative Structure

The metric perturbation is

```text
g_{ab}
\rightarrow
g_{ab}+h_{ab},
```

with

```text
|h_{ab}| \ll 1.
```

The perturbative system initially contains redundant gauge degrees of freedom.

These must be removed before constructing physical perturbation dynamics.

---

# Gauge Freedom

Under infinitesimal coordinate transformations

```text
x^a
\rightarrow
x^a+\xi^a,
```

the perturbation transforms as

```text
h_{ab}
\rightarrow
h_{ab}
-
\nabla_a\xi_b
-
\nabla_b\xi_a.
```

Different perturbation tensors related by such transformations represent the same physical geometry.

---

# Central Goal

The gauge-reduction objective is:

```text
eliminate nonphysical perturbative degrees of freedom
while preserving admissible dynamical structure.
```

---

# Structural Reduction Strategy

The intended reduction chain is:

```text
metric perturbations
→ tensor harmonic decomposition
→ parity separation
→ gauge fixing
→ reduced dynamical variables
→ master equation.
```

---

# Tensor Harmonic Decomposition

Perturbations are decomposed into tensor harmonics on the sphere.

The perturbative sectors separate into:

| Sector | Parity |
|---|---|
| axial | odd parity |
| polar | even parity |

This separation is preserved by spherical symmetry.

---

# Axial Sector

The axial sector is expected to provide the cleanest initial reduction.

Typical perturbative components include:

```text
h_{t\phi},
h_{r\phi},
h_{t\theta} ,
h_{r\theta}.
```

The axial sector often admits direct reduction to a single master variable.

This should be the first TIG3 reduction target.

---

# Polar Sector

The polar sector contains:

```text
h_{tt},
h_{tr},
h_{rr},
h_{\theta\theta},
h_{\phi\phi}.
```

This sector is expected to involve:

- stronger coupling,
- gauge mixing,
- and more complicated radial structure.

The polar reduction program remains substantially open.

---

# Candidate Gauge Choices

Several gauge strategies are possible.

---

# Option A — Regge–Wheeler Gauge

The most conservative route is a generalized Regge–Wheeler gauge.

Advantages:

| Feature | Benefit |
|---|---|
| classical structure | known perturbative framework |
| parity separation | simplified equations |
| direct master reduction | operator construction |

Potential issue:

```text
near-critical TIG3 geometry
may deform standard Schwarzschild reduction structure.
```

---

# Option B — Gauge-Invariant Variables

An alternative approach introduces gauge-invariant perturbative combinations.

Advantages:

| Feature | Benefit |
|---|---|
| coordinate independence | structural robustness |
| physical clarity | reduced gauge ambiguity |

Disadvantages:

| Issue | Difficulty |
|---|---|
| algebraic complexity | high |
| explicit construction | open |

---

# Option C — Admissible Gauge Framework

A TIG3-specific admissible gauge condition may be required.

Possible admissibility criteria include:

| Condition | Purpose |
|---|---|
| finite perturbation norm | spectral admissibility |
| regularity at core | bounded continuation |
| asymptotic Schwarzschild decay | GR compatibility |
| near-critical regularity | perturbative control |

This remains exploratory.

---

# Reduced Dynamical Variables

The reduction program seeks variables of the form

```text
\Psi(t,r).
```

These variables should:

- encode physical perturbations,
- eliminate pure gauge structure,
- admit radial reduction,
- and possess finite perturbative energy.

---

# Candidate Radial Reduction

The target reduced equation is

```text
\partial_t^2\Psi
-
\partial_{r_*}^2\Psi
+
V_{eff}(r)\Psi
=
0.
```

where

```text
dr_*/dr = 1/F(r).
```

The current document does not derive this equation.

It establishes the gauge pathway toward it.

---

# Near-Core Gauge Issues

For

```text
r \ll r_c,
```

the geometry behaves approximately like a regulated de Sitter-type sector.

Key gauge questions include:

- regularity of gauge generators,
- boundedness of perturbative variables,
- admissible boundary behavior,
- and preservation of finite-energy structure.

---

# Horizon and Branch Structure

The admissible radial geometry depends on the TIG2 branch structure

```text
x^3 - x^2 + \beta^3 = 0.
```

Near

```text
\beta \approx \beta_c,
```

the geometry may exhibit:

- branch merger,
- tortoise stretching,
- effective-potential flattening,
- and slow perturbative relaxation.

The gauge reduction must remain well-defined in this regime.

---

# Gauge Admissibility Conditions

Candidate admissible perturbations should satisfy:

| Condition | Purpose |
|---|---|
| finite norm | Hilbert-space admissibility |
| finite energy | perturbative control |
| regularity at core | bounded continuation |
| asymptotic decay | spectral compatibility |

These conditions constrain allowed gauge transformations.

---

# Expected Mathematical Obstacles

The reduction program faces several major open problems:

| Problem | Status |
|---|---|
| explicit field equations absent | unresolved |
| gauge closure | open |
| polar-sector coupling | open |
| near-critical regularity | open |
| gauge-invariant master variables | open |
| spectral positivity | downstream problem |

---

# Conservative Mathematical Position

The current reduction framework does not claim:

- exact perturbative closure,
- uniqueness of gauge reduction,
- gauge-invariant completeness,
- nonlinear stability,
- or full covariant dynamics.

The program remains a perturbative admissibility framework.

---

# Strategic Interpretation

The gauge-reduction program represents the transition from:

```text
raw perturbative geometry
```

to:

```text
reduced dynamical perturbation structure.
```

This is the essential bridge required before constructing the radial operator theory.

---

# Relation to Existing TIG3 Structure

This document connects:

```text
linear perturbations
→ gauge reduction
→ master variables
→ effective potential
→ spectral analysis.
```

It therefore forms the intermediate layer between geometric perturbations and operator-theoretic dynamics.

---

# Next Required Step

The next mathematical step is:

```text
master equation derivation.
```

This is required before explicit effective-potential analysis becomes possible.

---

# Status

This document establishes the gauge-reduction framework for the TIG3 vacuum-sector perturbation program.