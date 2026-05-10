# Branch Merging Structure

## Metadata

Title: Branch Merging Structure
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document defines the canonical branch-merging behavior of the TIG horizon equation near the critical regime.

Its purpose is to characterize how admissible horizon branches coalesce at discriminant collapse.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- near_critical_scaling.md
- critical_branch_sensitivity.md
- critical_limit_behavior.md
- branch_existence_conditions.md

Rigorous Status:
Theorem candidate

Allowed Scope:
local branch-merging analysis

Forbidden Expansion:
phase-transition claims, quantum gravity claims, Yang–Mills completion

---

# Core Principle

Within TIG:

\[
\text{criticality corresponds to branch coalescence}
\]

Branch merging occurs when the horizon equation and its first derivative vanish simultaneously.

---

# Canonical Horizon Equation

The canonical TIG horizon equation is:

\[
P(x,\beta)=x^3-x^2+\beta^3=0.
\]

Critical branch merging requires:

\[
P(x,\beta)=0
\]

and:

\[
\frac{\partial P}{\partial x}=0.
\]

---

# Critical Branch Point

Since:

\[
\frac{\partial P}{\partial x}=3x^2-2x,
\]

the nontrivial critical solution is:

\[
x_c=\frac{2}{3}.
\]

Substitution into \(P(x,\beta)=0\) yields:

\[
\beta_c^3=\frac{4}{27}.
\]

---

# Branch Merging Interpretation

At:

\[
(x_c,\beta_c)=\left(\frac{2}{3},\left(\frac{4}{27}\right)^{1/3}\right),
\]

two real branches coalesce.

This coalescence represents:

- loss of ordinary branch separation,
- critical structural compression,
- and reduced admissible continuation.

---

# Structural Interpretation

Branch merging currently refers only to:

- local algebraic coalescence,
- discriminant collapse,
- and admissibility-compatible critical compression.

It does NOT imply:

- physical phase transition,
- singularity resolution,
- dynamical instability,
- or spectral closure.

---

# Admissibility Requirement

Near branch merging, admissible interpretation must preserve:

- real positive branch structure,
- discriminant compatibility,
- bounded structural behavior,
- and Schwarzschild-connected interpretation where applicable.

---

# Current Limitation

This document does NOT prove global branch classification.

It only defines the local branch-merging structure of the canonical TIG horizon equation.

---

# Weakest Step

The weakest current step is the absence of a rigorous global theorem classifying all admissible and non-admissible branches.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/local_normal_form.md

---

# Classification

theorem candidate
