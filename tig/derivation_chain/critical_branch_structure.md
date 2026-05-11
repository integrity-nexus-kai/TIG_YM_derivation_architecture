# Critical Branch Structure

## Metadata

Title: Critical Branch Structure  
Author: Kai Stefan Dietrich  
Layer: 2 — Derivation Chain  
Status: theorem candidate  
Last Updated: 2026-05-11  

---

# MRP Classification

MRP Layer:
2 — Derivation Chain

Dependency Level:
depends on:
- geometric_horizon_proof.md
- cubic_normal_form.md
- TIG-Paper-Arxiv.pdf

Rigorous Status:
critical-geometry proof candidate

Allowed Scope:
critical branch geometry of the TIG horizon sector

Forbidden Expansion:
no complete vacuum-closure claim
no tensor-completion claim
no cosmological extrapolation
no quantum-gravity interpretation

---

# Purpose

This document establishes the critical branch structure of the TIG horizon sector.

The goal is to determine:
- admissible horizon branches,
- the critical branch merger,
- the degenerate horizon point,
- and the universal near-critical scaling behavior.

The analysis is restricted to the effective geometric sector established in:

geometric_horizon_proof.md

---

# Horizon Polynomial

The TIG horizon sector is governed by

$$
P(x,\beta)
=
x^3-x^2+\beta^3.
$$

The dimensionless variables are

$$
x=\frac{r_H}{2M},
\qquad
\beta=\frac{r_c}{2M}.
$$

Only positive real roots correspond to admissible horizon radii.

---

# Discriminant Structure

The discriminant of the cubic polynomial is

$$
\Delta(\beta)
=
\beta^3(4-27\beta^3).
$$

The sign of

$$
\Delta
$$

determines the admissible branch structure.

---

# Subcritical Sector

## Condition

$$
0<\beta<\beta_c.
$$

In this regime,

$$
\Delta>0.
$$

The cubic possesses:
- three real roots,
- two positive admissible horizon branches.

The larger positive branch connects continuously to the Schwarzschild horizon.

---

# Schwarzschild-Connected Branch

For

$$
\beta\rightarrow0,
$$

the outer branch satisfies

$$
x\rightarrow1.
$$

Therefore,

$$
r_H\rightarrow2M.
$$

This defines the Schwarzschild-connected admissible branch.

---

# Inner Admissible Branch

The second positive solution defines the inner admissible horizon branch.

As

$$
\beta
$$

increases toward criticality, the inner and outer branches approach each other continuously.

---

# Critical Sector

Criticality occurs when

$$
P(x_c,\beta_c)=0
$$

and

$$
\frac{\partial P}{\partial x}(x_c,\beta_c)=0.
$$

The derivative is

$$
\frac{\partial P}{\partial x}
=
3x^2-2x.
$$

The nontrivial stationary point is

$$
x_c=\frac23.
$$

Substitution into the cubic gives

$$
\beta_c
=
\left(
\frac{4}{27}
\right)^{1/3}.
$$

At this point:
- the two admissible branches merge,
- the horizon becomes degenerate,
- the polynomial develops a double root.

This is the critical geometric point of the TIG horizon sector.

---

# Supercritical Sector

## Condition

$$
\beta>\beta_c.
$$

In this regime,

$$
\Delta<0.
$$

The admissible positive horizon branch disappears.

The effective TIG sector becomes horizonless.

---

# Saddle-Node Structure

The branch merger is the canonical structure of a saddle-node transition.

The TIG critical point therefore belongs to the universal saddle-node class.

The structure follows from:
- smooth branch evolution,
- admissibility,
- and local double-root degeneracy.

It does not depend on microscopic interpretation.

---

# Near-Critical Expansion

Define

$$
x=x_c+\delta x,
\qquad
\beta=\beta_c-\delta\beta,
$$

with

$$
\delta\beta>0.
$$

Expanding around the critical point gives

$$
0
\approx
\frac12
P_{xx}(x_c,\beta_c)
(\delta x)^2
-
P_\beta(x_c,\beta_c)\delta\beta.
$$

Since

$$
P_{xx}(x_c,\beta_c)=2
$$

and

$$
P_\beta(x_c,\beta_c)=3\beta_c^2,
$$

one obtains

$$
(\delta x)^2
\approx
3\beta_c^2\delta\beta.
$$

Therefore,

$$
x_\pm-x_c
\approx
\pm
\sqrt3\,\beta_c(\beta_c-\beta)^{1/2}.
$$

---

# Universal Critical Scaling

The branch separation scales as

$$
(\beta_c-\beta)^{1/2}.
$$

The exponent

$$
\frac12
$$

is the universal saddle-node critical exponent.

This scaling follows directly from the local double-root structure.

---

# Geometric Interpretation

Near the critical point:
- the horizon branches flatten,
- branch separation decreases,
- and the near-horizon region becomes increasingly degenerate.

The TIG critical sector therefore behaves as a near-degenerate horizon geometry.

---

# Structural Stability

The saddle-node structure is structurally stable under sufficiently small admissible perturbations.

The branch merger therefore does not arise from:
- fine tuning,
- algebraic coincidence,
- or parameter fitting.

It is geometrically robust.

---

# Weakest Step

The branch structure depends on the effective geometric sector derived in:

geometric_horizon_proof.md

A complete nonlinear vacuum derivation remains unresolved.

This limitation must remain explicit.

---

# Proven Structures

## PR1 — Critical Point

The horizon polynomial possesses a nontrivial critical point at

$$
x_c=\frac23,
\qquad
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
$$

Status:
rigorous algebraic result.

## PR2 — Branch Merger

Two admissible positive branches merge continuously at the critical point.

Status:
rigorous discriminant result.

## PR3 — Saddle-Node Geometry

The TIG critical sector belongs to the universal saddle-node class.

Status:
rigorous local normal-form result.

## PR4 — Universal Scaling

The branch separation obeys

$$
x_\pm-x_c
\sim
(\beta_c-\beta)^{1/2}.
$$

Status:
rigorous local scaling result.

---

# Open Problems

## OP1 — Vacuum Closure

Determine whether the branch structure follows from a fully closed vacuum tensor system.

## OP2 — Dynamical Stability

Determine the nonlinear stability of the admissible branches.

## OP3 — Covariant Completion

Determine whether the critical sector admits a fully covariant action principle.

## OP4 — Uniqueness

Determine whether the TIG cubic is unique under the admissibility assumptions.

---

# Claim Boundary

This document establishes the critical branch structure only within the TIG effective geometric sector.

It does not establish:
- a complete gravitational theory,
- full vacuum closure,
- tensor completion,
- or quantum completion.

The result is a geometric critical-sector proof candidate for TIG2.

---

# Conclusion

The TIG horizon polynomial

$$
x^3-x^2+\beta^3=0
$$

contains:
- a Schwarzschild-connected admissible branch,
- an inner admissible branch,
- a degenerate critical horizon,
- and a horizonless supercritical sector.

The critical branch merger occurs at

$$
x_c=\frac23,
\qquad
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
$$

The near-critical branch separation obeys universal saddle-node scaling with exponent

$$
\frac12.
$$

This establishes the critical branch geometry of the TIG2 horizon sector.

---

# Classification

theorem candidate
