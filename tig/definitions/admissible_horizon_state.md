# Admissible Horizon State

## Metadata

Title: Admissible Horizon State  
Author: Kai Stefan Dietrich  
Layer: 1 — Definitions  
Status: theorem candidate  
Last Updated: 2026-05-10  

---

# MRP Classification

MRP Layer:
1 — Core Definitions

Dependency Level:
none

Rigorous Status:
preliminary definition / theorem candidate

Allowed Scope:
definition of structural horizon admissibility

Forbidden Expansion:
no Yang–Mills transfer  
no quantum gravity claims  
no thermodynamic claims  
no observational claims  

---

# Purpose

This document defines the minimal admissibility concept for TIG horizon states.

The purpose is to specify when a structural horizon configuration is considered mathematically admissible within the TIG framework.

---

# Core Variables

Let

\[
x := \frac{r_H}{2M}
\]

and

\[
\beta := \frac{r_c}{2M}.
\]

The TIG structural horizon equation is

\[
P(x,\beta) := x^3 - x^2 + \beta^3 = 0.
\]

---

# Definition: Structural Horizon State

A structural horizon state is a pair

\[
(x,\beta)
\]

with

\[
x > 0, \qquad \beta \geq 0
\]

satisfying

\[
P(x,\beta)=0.
\]

---

# Definition: Admissible Horizon State

A structural horizon state \((x,\beta)\) is called admissible if:

1. \(x\) is real and positive,
2. \(P(x,\beta)=0\),
3. the state belongs to a continuous branch connected to the Schwarzschild limit,
4. the branch does not cross a structural degeneracy without explicit critical analysis,
5. the corresponding effective geometry remains structurally regular under the assumptions of the TIG model.

---

# Schwarzschild Limit

The Schwarzschild reference state is recovered for

\[
\beta = 0,
\]

where

\[
x = 1.
\]

Thus the admissible outer branch must satisfy

\[
x(\beta) \rightarrow 1
\]

as

\[
\beta \rightarrow 0.
\]

---

# Critical Degeneracy

The critical point is expected at

\[
x_c = \frac{2}{3},
\]

with

\[
\beta_c = \left(\frac{4}{27}\right)^{1/3}.
\]

At this point the admissible horizon branch becomes structurally degenerate.

This requires separate critical analysis and must not be treated as an ordinary regular point.

---

# Structural Interpretation

Admissibility does not mean that every algebraic root is physically meaningful.

Admissibility requires compatibility between:

- algebraic reality,
- positivity,
- Schwarzschild continuity,
- branch stability,
- and structural regularity.

---

# Current Limitation

This definition is not yet a full proof of physical admissibility.

Open issues include:

- derivation of the effective metric from first principles,
- rigorous branch stability analysis,
- curvature regularity bounds,
- and operator-compatible formulation.

---

# Open Problems

1. Prove uniqueness of the Schwarzschild-connected admissible branch.
2. Classify non-admissible roots.
3. Determine whether critical degeneracy implies structural instability.
4. Connect admissibility to finite-correlation geometry.
5. Derive regularity conditions from an effective action or operator structure.

---

# Weakest Step

The weakest step is the transition from algebraic admissibility to geometric admissibility.

Currently, this requires additional assumptions on the effective TIG geometry.

---

# Drift Control

This document does NOT claim:

- a complete gravitational theory,
- a proof of singularity resolution,
- a quantum gravity mechanism,
- or a Yang–Mills mass gap result.

It only defines a preliminary admissibility condition for TIG horizon states.

---

# Next Dependency Step

The next admissible document is:

\[
\texttt{tig/definitions/structural\_parameter\_beta.md}
\]

or

\[
\texttt{tig/horizon\_structure/critical\_transition.md}
\]

depending on whether the next step focuses on definitions or branch analysis.

---

# Classification

theorem candidate
