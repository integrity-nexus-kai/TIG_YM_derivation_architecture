# Field Equation Consistency Proof

## Metadata

Title: Field Equation Consistency Proof
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document provides the minimal consistency proof structure for the TIG field-equation candidate.

Its purpose is not to prove a complete gravitational theory, but to show that the current TIG field-equation form is internally consistent with the effective metric ansatz, the horizon equation, and the critical branch structure.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- tig_field_equation_minimal_form.md
- variational_consistency_conditions.md
- admissibility_preserving_variation.md
- effective_metric_ansatz.md
- effective_horizon_equation.md
- critical_limit_behavior.md

Rigorous Status:
Theorem candidate

Allowed Scope:
internal consistency proof structure

Forbidden Expansion:
complete gravitational proof, quantum gravity completion, Yang–Mills completion

---

# Core Claim

The current TIG field-equation candidate is internally consistent if the following chain holds:

\[
S_{\mathrm{TIG}}
\rightarrow
\delta S_{\mathrm{TIG}}=0
\rightarrow
G_{\mu\nu}
+
\Lambda_{\mathrm{eff}}g_{\mu\nu}
+
\alpha \mathcal{H}_{\mu\nu}
=
8\pi T_{\mu\nu}^{(\mathrm{eff})}
\rightarrow
F(r)
\rightarrow
x^3-x^2+\beta^3=0.
\]

---

# Step 1 — Variational Origin

The admissibility-preserving action candidate is:

\[
S_{\mathrm{TIG}}
=
\int d^4x\,\sqrt{-g}
\left(
R
+
\alpha R^2
+
\mathcal{L}_{\mathrm{eff}}
\right).
\]

Variation with respect to \(g_{\mu\nu}\) yields an effective field-equation structure of the form:

\[
G_{\mu\nu}
+
\alpha \mathcal{H}_{\mu\nu}
=
8\pi T_{\mu\nu}^{(\mathrm{eff})},
\]

with:

\[
\mathcal{H}_{\mu\nu}
=
2R R_{\mu\nu}
-\frac{1}{2}g_{\mu\nu}R^2
-2\nabla_\mu\nabla_\nu R
+2g_{\mu\nu}\Box R.
\]

This establishes the minimal higher-order correction structure used in the TIG field-equation candidate.

---

# Step 2 — Effective Field Equation Form

Including the admissibility-compatible background sector gives:

\[
G_{\mu\nu}
+
\Lambda_{\mathrm{eff}}g_{\mu\nu}
+
\alpha \mathcal{H}_{\mu\nu}
=
8\pi T_{\mu\nu}^{(\mathrm{eff})}.
\]

This is the current minimal TIG field-equation form.

It remains a theorem candidate and not a completed gravitational field theory.

---

# Step 3 — Effective Metric Compatibility

The static spherically symmetric effective metric sector is:

\[
ds^2
=
-F(r)\,dt^2
+
\frac{dr^2}{F(r)}
+
r^2d\Omega^2.
\]

The TIG-compatible lapse function is:

\[
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
\]

This effective geometry is admissible if it preserves:

- asymptotic Schwarzschild compatibility,
- bounded small-radius behavior,
- branch-compatible horizon structure,
- and discriminant-controlled criticality.

---

# Step 4 — Horizon Equation

A horizon candidate satisfies:

\[
F(r_H)=0.
\]

Substitution gives:

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

# Step 5 — Dimensionless Reduction

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
r_H=2Mx,
\qquad
r_c=2M\beta.
\]

Substituting into the horizon equation gives:

\[
(2Mx)^3
-
2M(2Mx)^2
+
(2M\beta)^3
=
0.
\]

This becomes:

\[
8M^3x^3
-
8M^3x^2
+
8M^3\beta^3
=
0.
\]

Dividing by \(8M^3\) yields:

\[
x^3-x^2+\beta^3=0.
\]

Thus the canonical TIG horizon equation follows from the effective metric sector.

---

# Step 6 — Critical Point

Let:

\[
P(x,\beta)=x^3-x^2+\beta^3.
\]

Critical branch degeneracy occurs when:

\[
P(x,\beta)=0
\]

and:

\[
\frac{\partial P}{\partial x}=0.
\]

Since:

\[
\frac{\partial P}{\partial x}=3x^2-2x,
\]

the nontrivial critical point satisfies:

\[
x_c=\frac{2}{3}.
\]

Substituting into \(P(x,\beta)=0\):

\[
\left(\frac{2}{3}\right)^3
-
\left(\frac{2}{3}\right)^2
+
\beta_c^3
=
0.
\]

Therefore:

\[
\frac{8}{27}
-
\frac{4}{9}
+
\beta_c^3
=
0.
\]

Since:

\[
\frac{4}{9}
=
\frac{12}{27},
\]

we obtain:

\[
-\frac{4}{27}
+
\beta_c^3
=
0.
\]

Thus:

\[
\beta_c^3=\frac{4}{27}.
\]

---

# Step 7 — Discriminant Compatibility

The discriminant of the canonical TIG cubic is:

\[
\Delta
=
\beta^3(4-27\beta^3).
\]

At:

\[
\beta_c^3=\frac{4}{27},
\]

one obtains:

\[
\Delta=0.
\]

Thus the critical point coincides with discriminant collapse and branch coalescence.

---

# Consistency Result

The current TIG derivation chain establishes the following internal consistency:

\[
S_{\mathrm{TIG}}
\Rightarrow
G_{\mu\nu}
+
\Lambda_{\mathrm{eff}}g_{\mu\nu}
+
\alpha \mathcal{H}_{\mu\nu}
=
8\pi T_{\mu\nu}^{(\mathrm{eff})}
\Rightarrow
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}
\Rightarrow
x^3-x^2+\beta^3=0
\Rightarrow
(x_c,\beta_c)
=
\left(
\frac{2}{3},
\left(\frac{4}{27}\right)^{1/3}
\right).
\]

This proves internal structural consistency of the current TIG field-equation candidate.

It does not prove uniqueness, full covariance closure, quantum consistency, or Yang–Mills completion.

---

# Current Limitation

This document does NOT prove:

- that the action candidate is unique,
- that the effective metric is the unique solution,
- that the correction sector is complete,
- that geodesic completeness holds,
- or that TIG is a completed gravitational theory.

It proves only internal consistency of the current derivation chain.

---

# Weakest Step

The weakest current step is the transition:

\[
S_{\mathrm{TIG}}
\rightarrow
F(r)
\]

because the effective metric ansatz has not yet been derived as a unique solution of the field-equation candidate.

This remains the central unresolved derivation gap.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/effective_metric_solution_check.md

---

# Classification

theorem candidate
