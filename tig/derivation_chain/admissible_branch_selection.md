# Admissible Branch Selection

## Metadata

Title: Admissible Branch Selection
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document defines the canonical selection criteria for admissible TIG horizon branches.

Its purpose is to distinguish physically and structurally admissible branches from merely algebraic roots of the canonical horizon equation.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- branch_existence_conditions.md
- effective_horizon_equation.md
- structural_horizon_branch.md
- canonical_admissibility_axioms.md

Rigorous Status:
Theorem candidate

Allowed Scope:
effective admissible branch selection

Forbidden Expansion:
complete dynamical closure, singularity-resolution claims, Yang–Mills completion

---

# Core Principle

Within TIG:

\[
\text{not every algebraic root is an admissible branch}
\]

Admissibility requires additional structural selection criteria beyond root existence.

---

# Canonical Horizon Equation

The canonical TIG horizon equation is:

\[
x^3-x^2+\beta^3=0.
\]

Algebraic roots of this equation are candidates only.

They become admissible only if they satisfy the branch-selection criteria below.

---

# Selection Criterion S1 — Reality

An admissible branch must remain real-valued within its admissible domain.

Complex roots are not admissible horizon branches.

---

# Selection Criterion S2 — Positivity

An admissible branch must satisfy:

\[
x>0.
\]

Negative roots are not admissible horizon branches.

---

# Selection Criterion S3 — Schwarzschild Continuity

The canonical outer admissible branch must satisfy:

\[
x(\beta)\rightarrow 1
\]

as:

\[
\beta\rightarrow 0.
\]

This condition selects the Schwarzschild-connected horizon sector.

---

# Selection Criterion S4 — Discriminant Compatibility

An admissible branch must remain compatible with:

\[
\Delta=\beta^3(4-27\beta^3).
\]

The branch must not cross a discriminant-critical boundary without explicit critical-sector analysis.

---

# Selection Criterion S5 — Asymptotic Compatibility

An admissible branch must preserve Schwarzschild-compatible asymptotic behavior in the large-radius regime.

Branches that destroy asymptotic consistency are non-admissible.

---

# Selection Criterion S6 — Structural Boundedness

An admissible branch must preserve bounded structural interpretation.

Branches generating uncontrolled divergence or non-admissible asymptotic amplification are excluded.

---

# Canonical Selection Result

The canonical admissible TIG branch is currently the real positive branch continuously connected to the Schwarzschild limit.

This is a structural selection statement.

It is not yet a complete dynamical uniqueness theorem.

---

# Non-Admissible Branches

A branch is non-admissible if it:

- becomes complex,
- becomes negative,
- disconnects from the Schwarzschild-compatible sector,
- violates discriminant compatibility,
- destroys asymptotic consistency,
- or generates uncontrolled structural divergence.

---

# Critical Branch Behavior

Near:

\[
\beta\rightarrow \beta_c
\]

branch selection becomes structurally sensitive.

At this boundary, ordinary branch continuation may fail and critical-sector analysis becomes mandatory.

---

# Current Limitation

This document does NOT prove:

- global uniqueness,
- dynamical stability,
- geodesic completeness,
- or full physical branch classification.

It only defines structural selection criteria for admissible TIG horizon branches.

---

# Weakest Step

The weakest current step is the absence of a rigorous dynamical theorem proving uniqueness and persistence of the selected branch.

At present, admissible branch selection remains structurally defined.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/outer_branch_monotonicity.md

---

# Classification

theorem candidate
