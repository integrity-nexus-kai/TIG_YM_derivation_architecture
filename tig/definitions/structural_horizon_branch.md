# Structural Horizon Branch

## Metadata

Title: Structural Horizon Branch  
Author: Kai Stefan Dietrich  
Layer: 1 — Definitions  
Status: theorem candidate  
Last Updated: 2026-05-10  

---

# MRP Classification

MRP Layer:
1 — Core Definitions

Dependency Level:
depends on:
- admissible_horizon_state.md
- structural_parameter_beta.md

Rigorous Status:
preliminary structural definition

Allowed Scope:
definition of admissible solution branches

Forbidden Expansion:
no dynamical claims
no thermodynamic interpretation
no Yang–Mills mapping
no operator-theoretic closure

---

# Purpose

This document defines structural horizon branches within the TIG framework.

The purpose is to distinguish admissible geometric solution families from purely algebraic roots.

---

# Structural Equation

The TIG structural horizon equation is

\[
x^3 - x^2 + \beta^3 = 0.
\]

---

# Definition: Structural Branch

A structural branch is a continuous family

\[
x(\beta)
\]

satisfying

\[
x(\beta)^3 - x(\beta)^2 + \beta^3 = 0
\]

for a connected interval of admissible values of

\[
\beta.
\]

---

# Admissible Branch

A branch is called admissible if:

1. \(x(\beta)\) remains real,
2. \(x(\beta) > 0\),
3. the branch is continuously connected to the Schwarzschild limit,
4. no structural singular transition occurs without explicit critical analysis.

---

# Schwarzschild-Connected Branch

The canonical admissible branch is the branch satisfying

\[
x(\beta) \rightarrow 1
\]

as

\[
\beta \rightarrow 0.
\]

This branch defines the outer admissible TIG horizon sector.

---

# Non-Admissible Branches

Algebraic roots may exist which:

- become negative,
- become complex,
- disconnect from the Schwarzschild sector,
- or terminate at structural degeneracies.

Such branches are currently considered non-admissible unless proven otherwise.

---

# Critical Branch Degeneracy

At the critical point

\[
\beta_c = \left(\frac{4}{27}\right)^{1/3},
\]

multiple branches merge.

At this point:

- ordinary perturbative intuition may fail,
- branch identity may become ambiguous,
- and admissibility requires separate analysis.

---

# Structural Interpretation

A branch is interpreted as a structural geometric sector rather than merely a polynomial solution set.

The branch structure encodes possible horizon configurations of the TIG effective geometry.

---

# Open Problems

1. Prove uniqueness of the Schwarzschild-connected branch.
2. Classify all algebraically allowed branches.
3. Determine admissibility boundaries.
4. Analyze near-critical branch topology.
5. Connect branch structure to effective operator stability.

---

# Weakest Step

The weakest step is the transition from algebraic continuity to geometric admissibility.

Additional regularity conditions may be required.

---

# Drift Control

This document does NOT claim:

- a proof of black-hole stability,
- a proof of singularity removal,
- a quantum-gravity mechanism,
- or a Yang–Mills correspondence.

It only defines structural branch concepts within TIG.

---

# Next Dependency Step

Possible next admissible documents:

tig/derivation_chain/cubic_normal_form.md

or

tig/horizon_structure/critical_transition.md

---

# Classification

theorem candidate
