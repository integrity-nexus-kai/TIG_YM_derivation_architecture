# Canonical Dependency Map

## Metadata

Title: Canonical Dependency Map  
Author: Kai Stefan Dietrich  
Layer: Governance  
Status: canonical reference  
Last Updated: 2026-05-10  

---

# Purpose

This document defines the canonical dependency structure of the TIG theorem-oriented development.

Its purpose is to prevent circular reasoning, uncontrolled conceptual expansion, and unsupported theorem escalation.

---

# Core Rule

TIG development proceeds only upward through the dependency hierarchy.

No document may depend on a higher layer.

No later interpretation may be used to justify an earlier definition.

---

# Canonical Layer Order

## Layer 1 — Definitions

Purpose:
define primitive TIG objects.

Includes:

- admissible_horizon_state.md
- structural_parameter_beta.md
- structural_horizon_branch.md

Allowed:
definitions only.

Forbidden:
stability claims, operator claims, YM transfer, thermodynamic claims.

---

## Layer 2 — Derivation Chain

Purpose:
formalize the structural normal form.

Includes:

- cubic_normal_form.md

Allowed:
controlled derivation candidates.

Forbidden:
full field-equation claims, operator closure, YM transfer.

---

## Layer 3 — Horizon Structure

Purpose:
analyze critical horizon geometry.

Includes:

- critical_transition.md
- discriminant_geometry.md

Allowed:
branch criticality, discriminant structure, degeneracy analysis.

Forbidden:
spectral claims, thermodynamic claims, YM claims.

---

## Layer 4 — Admissibility

Purpose:
define structurally admissible sectors.

Includes:

- asymptotic_regularization.md
- finite_correlation_geometry.md
- operator_admissibility.md
- nonlinear_branch_coupling.md
- effective_spectral_compression.md

Allowed:
admissibility hypotheses, structural restrictions, asymptotic constraints.

Forbidden:
rigorous operator theorems, mass-gap claims, confinement claims.

---

## Layer 5 — Operator Theory

Purpose:
develop effective operator-oriented structural hypotheses.

Includes:

- asymptotic_operator_bounds.md
- admissible_semiflow_structure.md
- critical_operator_compression.md
- asymptotic_state_restriction.md
- admissible_infrared_sector.md
- effective_gap_emergence.md
- infrared_spectral_restriction.md
- asymptotic_sector_compactness.md
- admissible_low_energy_sector.md
- effective_ir_suppression.md
- nondivergent_asymptotic_modes.md
- finite_effective_propagation.md
- admissible_asymptotic_stability.md
- effective_structural_gap.md
- infrared_mode_separation.md
- admissible_energy_hierarchy.md
- structural_spectral_threshold.md
- asymptotic_accessibility_bounds.md
- admissible_mode_compactness.md
- infrared_sector_rigidity.md

Allowed:
effective operator-oriented hypotheses.

Forbidden:
unqualified functional analysis claims, rigorous spectral theorems, YM proof claims.

---

# Dependency Rule

A document may depend only on:

1. documents from the same layer,
2. documents from lower layers,
3. governance documents.

A document may not depend on higher-layer conclusions.

---

# Circularity Prohibition

The following are forbidden:

- using YM motivation to justify TIG definitions,
- using operator claims to justify horizon equations,
- using spectral language to justify admissibility definitions,
- using effective gap language to justify earlier branch structure.

---

# Recovery Procedure

If a dependency violation is detected:

1. stop further expansion,
2. identify the illegal dependency,
3. remove unsupported assumptions,
4. return to the last valid lower-layer statement,
5. reconstruct upward minimally.

---

# Minimal Closure Rule

A layer is considered temporarily closed only when:

- core objects are defined,
- dependencies are explicit,
- weakest steps are identified,
- no higher-layer concept is used as justification.

---

# Current Status

The current TIG structure is not a completed theorem system.

It is a theorem-oriented dependency architecture.

---

# Classification

canonical governance reference
