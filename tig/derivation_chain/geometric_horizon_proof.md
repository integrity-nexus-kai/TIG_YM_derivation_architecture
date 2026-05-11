# Geometric Horizon Proof

## Metadata

Title: Geometric Horizon Proof  
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
- effective_metric_ansatz.md
- effective_horizon_equation.md
- cubic_normal_form.md
- branch_existence_conditions.md
- critical_transition.md
- TIG-Paper-Arxiv.pdf

Rigorous Status:
geometric horizon-sector proof candidate

Allowed Scope:
geometric reconstruction of the TIG1 horizon sector

Forbidden Expansion:
no complete nonlinear vacuum-closure claim
no full tensor-closure claim
no final covariant action claim
no quantum gravity claim
no Yang-Mills transfer

---

# Purpose

This document formulates the geometric proof structure for the TIG1 horizon sector.

The purpose is to show that the TIG cubic

\[
x^3 - x^2 + \beta^3 = 0
\]

arises from a minimal static, spherically symmetric, regular, Schwarzschild-compatible geometry with a single intrinsic correction scale.

This document does not claim a complete nonlinear vacuum solution.

---

# Scope

The proof is restricted to the geometric horizon sector.

It establishes:

- the effective geometric origin of the TIG cubic,
- the admissible horizon equation,
- the critical branch structure,
- the saddle-node transition,
- the Schwarzschild-compatible limit.

It does not establish:

- complete nonlinear vacuum closure,
- full tensor closure,
- final field equations,
- Hamiltonian consistency,
- quantum completion.

These unresolved problems belong to TIG3.

---

# Assumptions

## A1 — Static Spherical Symmetry

The geometry is assumed to be static and spherically symmetric:

\[
ds^2 =
-F(r)dt^2
+
\frac{dr^2}{F(r)}
+
r^2 d\Omega^2.
\]

## A2 — Schwarzschild Asymptotics

For large radius,

\[
F(r) \rightarrow 1-\frac{2M}{r}.
\]

## A3 — Regular Central Structure

The effective mass profile must satisfy

\[
m(r) \sim r^3
\]

as

\[
r \rightarrow 0.
\]

This is the minimal condition required to avoid the Schwarzschild-type central mass singularity in the effective sector.

## A4 — Single Structural Correction Scale

The deformation is governed by one intrinsic length scale

\[
r_c.
\]

No additional fitting scales are introduced.

## A5 — Admissible Horizon Transition

The horizon sector must admit a controlled transition between:

- two-horizon configurations,
- a degenerate critical horizon,
- and horizonless configurations.

## A6 — Structural Integrity

No residual structure may be removed by artificial cancellation, hidden matter insertion, or flexible parameter fitting.

---

# Effective Mass Profile

The minimal effective mass profile compatible with the assumptions is

\[
m(r)
=
M \frac{r^3}{r^3+r_c^3}.
\]

This profile satisfies:

\[
m(r)\rightarrow M
\]

for

\[
r\rightarrow\infty
\]

and

\[
m(r)\sim \frac{M}{r_c^3}r^3
\]

for

\[
r\rightarrow 0.
\]

Thus it is Schwarzschild-compatible at infinity and regular at the center.

---

# Effective Lapse Function

The corresponding lapse function is

\[
F(r)
=
1-\frac{2m(r)}{r}.
\]

Substitution gives

\[
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
\]

This is the minimal effective geometry used for the TIG1 horizon sector.

---

# Horizon Condition

Horizons are defined by

\[
F(r_H)=0.
\]

Therefore,

\[
1-\frac{2Mr_H^2}{r_H^3+r_c^3}=0.
\]

Multiplication by

\[
r_H^3+r_c^3
\]

gives

\[
r_H^3+r_c^3-2Mr_H^2=0.
\]

---

# Dimensionless Reduction

Define

\[
x=\frac{r_H}{2M}
\]

and

\[
\beta=\frac{r_c}{2M}.
\]

Then

\[
r_H=2Mx,
\qquad
r_c=2M\beta.
\]

Substitution into the horizon equation yields

\[
(2M)^3x^3
+
(2M)^3\beta^3
-
2M(2M)^2x^2
=
0.
\]

Division by

\[
(2M)^3
\]

gives

\[
x^3-x^2+\beta^3=0.
\]

This is the TIG cubic.

---

# Geometric Meaning

The TIG cubic is not introduced as a fitting ansatz.

It follows from:

1. static spherical symmetry,
2. Schwarzschild asymptotics,
3. regular central mass behavior,
4. one intrinsic correction scale,
5. admissible horizon transition.

The cubic is therefore the minimal geometric horizon equation of this effective TIG sector.

---

# Critical Point

Let

\[
P(x,\beta)=x^3-x^2+\beta^3.
\]

A critical branch-merger occurs when

\[
P(x_c,\beta_c)=0
\]

and

\[
\frac{\partial P}{\partial x}(x_c,\beta_c)=0.
\]

Since

\[
\frac{\partial P}{\partial x}
=
3x^2-2x
=
x(3x-2),
\]

the nontrivial critical point is

\[
x_c=\frac{2}{3}.
\]

Substitution into

\[
P(x_c,\beta_c)=0
\]

gives

\[
\left(\frac{2}{3}\right)^3
-
\left(\frac{2}{3}\right)^2
+
\beta_c^3
=
0.
\]

Therefore,

\[
\frac{8}{27}-\frac{4}{9}+\beta_c^3=0,
\]

hence

\[
\beta_c^3=\frac{4}{27}.
\]

Thus,

\[
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
\]

---

# Branch Structure

The discriminant of

\[
x^3-x^2+\beta^3=0
\]

is

\[
\Delta(\beta)=\beta^3(4-27\beta^3).
\]

Therefore:

## Subcritical Sector

For

\[
0<\beta<\beta_c,
\]

the discriminant is positive.

The horizon equation admits two positive real horizon branches.

## Critical Sector

For

\[
\beta=\beta_c,
\]

the discriminant vanishes.

The two positive branches merge at

\[
x_c=\frac{2}{3}.
\]

This is the degenerate critical horizon.

## Supercritical Sector

For

\[
\beta>\beta_c,
\]

the admissible positive horizon branch is absent.

The configuration becomes horizonless in this effective sector.

---

# Near-Critical Scaling

Let

\[
x=x_c+\delta x
\]

and

\[
\beta=\beta_c-\delta\beta
\]

with

\[
\delta\beta>0.
\]

Expanding

\[
P(x,\beta)
\]

around

\[
(x_c,\beta_c)
\]

gives, to leading order,

\[
0
\approx
\frac{1}{2}P_{xx}(x_c,\beta_c)(\delta x)^2
-
P_\beta(x_c,\beta_c)\delta\beta.
\]

Since

\[
P_{xx}(x_c,\beta_c)=2
\]

and

\[
P_\beta(x_c,\beta_c)=3\beta_c^2,
\]

one obtains

\[
(\delta x)^2
\approx
3\beta_c^2\delta\beta.
\]

Therefore,

\[
x_\pm-x_c
\approx
\pm \sqrt{3}\,\beta_c(\beta_c-\beta)^{1/2}.
\]

This is the universal square-root scaling of a saddle-node transition.

---

# Relation to TIG1

TIG1 established the structural horizon cubic and its critical transition.

This TIG2 document reconstructs that result geometrically from the effective mass profile and lapse function.

Thus TIG2 does not replace TIG1.

It hardens TIG1 by isolating the precise geometric assumptions under which the TIG horizon sector follows.

---

# Proven Structures

## PR1 — Horizon Reduction

The horizon condition

\[
F(r_H)=0
\]

algebraically reduces to

\[
x^3-x^2+\beta^3=0.
\]

Status:
rigorous within the stated effective geometry.

## PR2 — Critical Point

The simultaneous conditions

\[
P(x_c,\beta_c)=0,
\qquad
\partial_xP(x_c,\beta_c)=0
\]

yield

\[
x_c=\frac{2}{3},
\qquad
\beta_c=\left(\frac{4}{27}\right)^{1/3}.
\]

Status:
rigorous algebraic result.

## PR3 — Branch Transition

The discriminant

\[
\Delta(\beta)=\beta^3(4-27\beta^3)
\]

determines the subcritical, critical, and supercritical horizon sectors.

Status:
rigorous algebraic result.

## PR4 — Near-Critical Scaling

The local expansion around

\[
(x_c,\beta_c)
\]

yields

\[
x_\pm-x_c
\sim
\pm(\beta_c-\beta)^{1/2}.
\]

Status:
rigorous local normal-form result.

---

# Weakest Step

The weakest step is the selection of the effective mass profile

\[
m(r)
=
M\frac{r^3}{r^3+r_c^3}.
\]

It is geometrically minimal and structurally admissible, but it is not yet derived from a complete nonlinear vacuum action.

This limitation must remain explicit.

---

# Missing Derivations

The following derivations are not completed in TIG2:

1. full nonlinear vacuum closure,
2. complete tensor closure,
3. final covariant action,
4. Hamiltonian constraint analysis,
5. uniqueness theorem for the effective mass profile.

These belong to TIG3.

---

# Open Problems

## OP1 — Vacuum Closure

Determine whether the TIG effective geometry solves a closed nonlinear vacuum system without introducing artificial effective sources.

## OP2 — Tensor Consistency

Determine whether the residual tensor structure can be closed by a principled geometric correction.

## OP3 — Action Principle

Determine whether a covariant action exists whose admissible static sector yields the TIG horizon geometry.

## OP4 — Uniqueness

Determine whether the cubic horizon structure is unique under the stated geometric assumptions or one member of a broader admissible class.

---

# Claim Boundary

This document proves the TIG horizon equation only within the stated effective geometric sector.

It does not prove that TIG is a complete replacement for General Relativity.

It does not prove a full vacuum solution.

It does not prove a final covariant theory.

It establishes the geometric horizon-sector proof required for TIG2.

---

# Conclusion

Under the assumptions of static spherical symmetry, Schwarzschild asymptotics, regular central structure, one intrinsic correction scale, and admissible horizon transition, the TIG1 horizon sector reduces to

\[
x^3-x^2+\beta^3=0.
\]

The resulting structure contains:

- an outer Schwarzschild-connected branch,
- a critical branch merger,
- a degenerate critical horizon,
- a horizonless supercritical sector,
- and universal saddle-node scaling.

This establishes the geometric proof candidate for the TIG2 horizon sector while preserving the unresolved vacuum-closure problem for TIG3.

---

# Classification

theorem candidate
