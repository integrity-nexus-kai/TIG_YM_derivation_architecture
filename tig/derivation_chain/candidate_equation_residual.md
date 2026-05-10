# Candidate Equation Residual

## Metadata

Title: Candidate Equation Residual
Author: Kai Stefan Dietrich
Layer: Derivation Chain
Status: theorem candidate
Last Updated: 2026-05-10

---

# Purpose

This document evaluates the residual structure of the current TIG field-equation candidate under the effective TIG metric sector.

Its purpose is not to establish a complete field-equation proof, but to determine whether unresolved inconsistencies emerge when comparing the effective geometry against the admissibility-compatible tensor structure.

---

# MRP Classification

MRP Layer:
Derivation Chain

Dependency Level:
depends on:
- closed_form_tensor_components.md
- symbolic_tensor_evaluation.md
- tensor_level_consistency_check.md
- tig_field_equation_minimal_form.md

Rigorous Status:
Theorem candidate

Allowed Scope:
residual consistency analysis

Forbidden Expansion:
full covariance proof, quantum gravity completion, Yang–Mills completion

---

# Candidate Field Equation

The current TIG field-equation candidate is:

\[
G_{\mu\nu}
+
\Lambda_{\mathrm{eff}}g_{\mu\nu}
+
\alpha\mathcal H_{\mu\nu}
=
8\pi T_{\mu\nu}^{(\mathrm{eff})}.
\]

Define the residual tensor:

\[
\mathcal E_{\mu\nu}
=
G_{\mu\nu}
+
\Lambda_{\mathrm{eff}}g_{\mu\nu}
+
\alpha\mathcal H_{\mu\nu}
-
8\pi T_{\mu\nu}^{(\mathrm{eff})}.
\]

Exact field-equation closure would require:

\[
\mathcal E_{\mu\nu}=0.
\]

---

# Effective Metric Sector

The TIG lapse structure is:

\[
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
\]

The corresponding metric is:

\[
ds^2
=
-F(r)\,dt^2
+
\frac{dr^2}{F(r)}
+
r^2d\Omega^2.
\]

---

# Einstein Tensor Contribution

The effective geometry generates:

\[
G^t_{\ t}
=
G^r_{\ r}
=
-\frac{
6Mr_c^3
}{
(r^3+r_c^3)^2
}.
\]

Thus the Einstein tensor remains:

- finite for \(r>0\),
- bounded near the effective core sector,
- and asymptotically decaying.

---

# Asymptotic Residual Behavior

For:

\[
r\gg r_c,
\]

one obtains:

\[
G_{\mu\nu}\rightarrow0.
\]

The higher-order correction sector also decays asymptotically.

Therefore:

\[
\mathcal E_{\mu\nu}\rightarrow0
\]

asymptotically under admissibility-compatible effective source assumptions.

Thus asymptotic Schwarzschild compatibility is preserved.

---

# Small-Radius Residual Behavior

For:

\[
r\rightarrow0,
\]

the effective tensor sector remains finite:

\[
G^t_{\ t}
\rightarrow
-\frac{
6M
}{
r_c^3
}.
\]

No immediate divergence appears within the effective residual structure.

Thus the effective core sector remains structurally regularized.

---

# Higher-Order Correction Residual

The correction tensor:

\[
\mathcal H_{\mu\nu}
=
2R R_{\mu\nu}
-\frac{1}{2}g_{\mu\nu}R^2
-2\nabla_\mu\nabla_\nu R
+2g_{\mu\nu}\Box R
\]

introduces nontrivial curvature corrections near:

\[
r\sim r_c.
\]

No explicit closed-form cancellation proof currently exists.

However, no immediate incompatibility has been identified within the admissible effective regime.

---

# Residual Compatibility Result

The current residual analysis indicates:

- asymptotic decay of the residual structure,
- bounded effective tensor behavior,
- absence of immediate divergence instabilities,
- and structural compatibility between the effective geometry and the candidate field equation.

No direct residual contradiction has been identified.

---

# Structural Interpretation

The residual tensor currently behaves as:

- asymptotically suppressed,
- bounded within the effective core regime,
- and structurally compatible with admissibility-preserving higher-order corrections.

The current TIG geometry therefore remains admissible at the residual level.

---

# Current Limitation

This document does NOT prove:

- exact residual cancellation,
- rigorous tensor equality,
- uniqueness of the effective metric,
- full covariance closure,
- or Yang–Mills compatibility.

It establishes only preliminary residual compatibility.

---

# Weakest Step

The weakest current step is the absence of explicit symbolic evaluation of:

\[
\mathcal H_{\mu\nu}
-
8\pi T_{\mu\nu}^{(\mathrm{eff})}.
\]

This remains the primary unresolved residual-level derivation problem.

---

# Next Dependency Step

The next derivation objective is:

tig/derivation_chain/field_equation_proof_status.md

---

# Classification

theorem candidate
