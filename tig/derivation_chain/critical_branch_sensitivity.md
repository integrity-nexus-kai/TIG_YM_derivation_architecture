# Critical Branch Sensitivity

## Metadata

Title: Critical Branch Sensitivity
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document defines the structural sensitivity of admissible TIG horizon branches near the critical regime.

Its purpose is to characterize why the admissible outer branch becomes increasingly fragile as the discriminant approaches zero.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- outer_branch_monotonicity.md
- critical_limit_behavior.md
- discriminant_geometry.md
- admissible_branch_selection.md

Rigorous Status:
Theorem candidate

Allowed Scope:
critical branch sensitivity analysis

Forbidden Expansion:
dynamical collapse claims, spectral claims, quantum gravity claims, Yang–Mills completion

---

# Core Principle

Within TIG:

\[
\text{criticality increases branch sensitivity}
\]

Branch behavior near the critical regime must therefore be treated separately from ordinary smooth deformation.

---

# Canonical Horizon Equation

The canonical TIG horizon equation is:

\[
P(x,\beta)=x^3-x^2+\beta^3=0.
\]

---

# Branch Sensitivity

For an implicit branch:

\[
x=x(\beta),
\]

implicit differentiation gives:

\[
\frac{dx}{d\beta}
=
-\frac{\partial P/\partial \beta}{\partial P/\partial x}.
\]

With:

\[
\frac{\partial P}{\partial \beta}=3\beta^2
\]

and:

\[
\frac{\partial P}{\partial x}=3x^2-2x,
\]

one obtains:

\[
\frac{dx}{d\beta}
=
-\frac{3\beta^2}{3x^2-2x}.
\]

---

# Critical Sensitivity

At the critical point:

\[
x_c=\frac{2}{3},
\]

the denominator satisfies:

\[
3x_c^2-2x_c=0.
\]

Thus the branch derivative becomes singular in the critical limit.

---

# Structural Interpretation

The singular branch derivative indicates:

- increased structural sensitivity,
- reduced perturbative reliability,
- branch compression,
- and critical accessibility limitation.

It does NOT imply:

- physical instability,
- singularity resolution,
- quantum criticality,
- or dynamical collapse.

---

# Admissibility Requirement

Near criticality, admissible analysis must account for:

- branch sensitivity,
- discriminant compatibility,
- bounded structural interpretation,
- and critical-sector restrictions.

Ordinary branch continuation is not sufficient.

---

# Current Limitation

This document does NOT prove a dynamical instability theorem.

It only characterizes the structural sensitivity of the implicit TIG branch near the critical point.

---

# Weakest Step

The weakest current step is the absence of a rigorous perturbative expansion theorem near discriminant collapse.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/near_critical_scaling.md

---

# Classification

theorem candidate
