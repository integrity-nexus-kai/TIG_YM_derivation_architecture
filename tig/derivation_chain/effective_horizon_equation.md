# Effective Horizon Equation

## Metadata

Title: Effective Horizon Equation
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document derives the effective TIG horizon equation from the current admissible metric ansatz.

Its purpose is to connect the effective geometric carrier to the canonical TIG structural normal form.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- effective_metric_ansatz.md
- admissibility_preserving_variation.md
- structural_parameter_beta.md
- structural_horizon_branch.md

Rigorous Status:
Theorem candidate

Allowed Scope:
effective horizon equation derivation

Forbidden Expansion:
complete field-equation claims, quantum gravity claims, Yang–Mills completion

---

# Effective Metric Ansatz

The current TIG effective metric function is:

\[
F(r)=1-\frac{2Mr^2}{r^3+r_c^3}
\]

A horizon candidate is defined by:

\[
F(r_H)=0.
\]

---

# Horizon Condition

Setting:

\[
F(r_H)=0
\]

gives:

\[
1-\frac{2Mr_H^2}{r_H^3+r_c^3}=0.
\]

Therefore:

\[
r_H^3+r_c^3=2Mr_H^2.
\]

Rearranging:

\[
r_H^3-2Mr_H^2+r_c^3=0.
\]

---

# Dimensionless Reduction

Define:

\[
x:=\frac{r_H}{2M}
\]

and:

\[
\beta:=\frac{r_c}{2M}.
\]

Then:

\[
r_H=2Mx
\]

and:

\[
r_c=2M\beta.
\]

Substitution yields:

\[
(2Mx)^3-2M(2Mx)^2+(2M\beta)^3=0.
\]

This becomes:

\[
8M^3x^3-8M^3x^2+8M^3\beta^3=0.
\]

Dividing by:

\[
8M^3
\]

gives the canonical TIG horizon equation:

\[
x^3-x^2+\beta^3=0.
\]

---

# Structural Interpretation

The canonical horizon equation emerges from the effective metric ansatz through dimensionless reduction.

At the current stage this establishes:

- effective branch generation,
- structural horizon compatibility,
- and discriminant-compatible critical behavior.

It does NOT establish a complete field equation.

---

# Critical Compatibility

The resulting equation is compatible with the canonical discriminant:

\[
\Delta=\beta^3(4-27\beta^3).
\]

Critical degeneracy occurs at:

\[
\beta_c^3=\frac{4}{27}.
\]

---

# Admissibility Interpretation

Not every algebraic root is automatically admissible.

Admissibility still requires:

- positivity,
- real branch structure,
- Schwarzschild-connected continuity,
- asymptotic boundedness,
- and critical-sector compatibility.

---

# Weakest Step

The weakest current step is that the metric ansatz itself has not yet been derived from a rigorous action principle.

This document derives the horizon equation from the ansatz, not the ansatz from first principles.

---

# Current Status

This document provides:

- an effective derivation of the canonical TIG horizon equation,
- a dimensionless reduction,
- and compatibility with branch criticality.

It does NOT provide:

- rigorous gravitational field equations,
- full variational closure,
- quantum gravity completion,
- or Yang–Mills equivalence.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/critical_limit_behavior.md

---

# Classification

theorem candidate
