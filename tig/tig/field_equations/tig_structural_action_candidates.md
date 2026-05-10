# TIG Structural Action Candidates

## Metadata

Title: TIG Structural Action Candidates
Author: Kai Stefan Dietrich
Layer: Field Equations
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document defines the first structural action candidates for the TIG v2 dynamical reconstruction program.

Its purpose is to derive TIG dynamics from the canonical cubic structure rather than imposing a preselected field equation.

---

# Core Principle

The TIG cubic is treated as primary:

\[
P(x,\beta)=x^3-x^2+\beta^3.
\]

The goal is to identify variational structures whose stationary conditions naturally generate:

\[
P(x,\beta)=0.
\]

---

# Structural Potential Candidate

Define the structural potential:

\[
\mathcal V(x,\beta)
=
\frac14x^4
-
\frac13x^3
+
\beta^3x.
\]

Then:

\[
\frac{\partial \mathcal V}{\partial x}
=
x^3-x^2+\beta^3.
\]

Therefore the TIG horizon equation becomes the stationarity condition:

\[
\frac{\partial \mathcal V}{\partial x}=0.
\]

---

# Interpretation

The canonical TIG cubic is no longer interpreted merely as an algebraic horizon condition.

It can be interpreted as the Euler condition of a structural admissibility potential.

This provides the first dynamical bridge:

\[
\mathcal V(x,\beta)
\rightarrow
P(x,\beta)=0
\rightarrow
\text{admissible horizon branch}.
\]

---

# Critical Structure

The second derivative is:

\[
\frac{\partial^2 \mathcal V}{\partial x^2}
=
3x^2-2x.
\]

Critical degeneracy occurs when:

\[
\frac{\partial \mathcal V}{\partial x}=0
\]

and:

\[
\frac{\partial^2 \mathcal V}{\partial x^2}=0.
\]

This gives:

\[
x_c=\frac23.
\]

Substitution into:

\[
x^3-x^2+\beta^3=0
\]

yields:

\[
\beta_c^3=\frac4{27}.
\]

Thus the critical TIG point is naturally reproduced by the structural potential.

---

# Dynamical Significance

The potential:

\[
\mathcal V(x,\beta)
\]

encodes:

- admissible branch selection,
- horizon stationarity,
- critical coalescence,
- and structural transition behavior.

This suggests that TIG dynamics may be reconstructed from an admissibility potential rather than from a predefined curvature action.

---

# Required Extension

The next step is to lift the finite-dimensional structural potential:

\[
\mathcal V(x,\beta)
\]

to a geometric action candidate:

\[
\mathcal A_{\mathrm{TIG}}[g,\chi]
\]

where:

- \(g\) denotes the spacetime metric,
- \(\chi\) denotes a structural admissibility field or scalar,
- and the TIG cubic emerges as a reduced stationarity condition.

---

# Candidate Reconstruction Direction

A possible reconstruction path is:

\[
\mathcal A_{\mathrm{TIG}}[g,\chi]
\rightarrow
\frac{\delta \mathcal A_{\mathrm{TIG}}}{\delta \chi}=0
\rightarrow
x^3-x^2+\beta^3=0.
\]

This would make the TIG cubic an Euler-Lagrange condition of the structural sector.

---

# Forbidden Interpretation

This document does NOT claim:

- a completed action,
- exact tensor closure,
- quantum completion,
- or full covariance closure.

It defines only the first structural action candidate for TIG v2.

---

# Current Status

The TIG v2 reconstruction program now possesses:

- a canonical structural potential,
- a variational origin for the TIG cubic,
- preservation of the critical branch point,
- and a pathway toward a geometric action.

---

# Next Objective

The next reconstruction objective is:

tig/field_equations/geometric_lift_of_structural_potential.md

---

# Classification

theorem candidate
