# Curvature Invariants

## Metadata

Title: Curvature Invariants  
Author: Kai Stefan Dietrich  
Layer: 2 — Derivation Chain  
Status: derivation candidate  
Last Updated: 2026-05-11  

---

# MRP Classification

MRP Layer:
2 — Derivation Chain

Dependency Level:
depends on:
- geometric_horizon_proof.md
- photon_sphere_structure.md
- effective_metric_ansatz.md
- TIG-Paper-Arxiv.pdf

Rigorous Status:
curvature-regularity derivation candidate

Allowed Scope:
curvature structure of the TIG effective geometric sector

Forbidden Expansion:
no complete vacuum-closure claim
no tensor-completion claim
no singularity-resolution claim beyond the effective sector
no quantum-gravity interpretation

---

# Purpose

This document analyzes the curvature invariants of the TIG effective geometric sector.

The goal is to determine:
- the Ricci scalar,
- the quadratic Ricci invariant,
- the Kretschmann scalar,
- and the regularity structure near the center.

The analysis is restricted to the effective geometry established in:

geometric_horizon_proof.md

---

# Effective Geometry

The effective lapse function is

$$
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
$$

The metric is

$$
ds^2
=
-F(r)dt^2
+
\frac{dr^2}{F(r)}
+
r^2d\Omega^2.
$$

---

# Near-Core Expansion

For

$$
r\rightarrow0,
$$

the denominator satisfies

$$
r^3+r_c^3
\approx
r_c^3.
$$

Therefore,

$$
F(r)
\approx
1-\frac{2M}{r_c^3}r^2.
$$

Define

$$
\Lambda_{\mathrm{eff}}
=
\frac{6M}{r_c^3}.
$$

Then

$$
F(r)
\approx
1-\frac{\Lambda_{\mathrm{eff}}}{3}r^2.
$$

Thus the effective near-core geometry approaches a de Sitter-type structure.

---

# Ricci Scalar

For a static spherically symmetric metric of the form

$$
ds^2
=
-F(r)dt^2
+
\frac{dr^2}{F(r)}
+
r^2d\Omega^2,
$$

the Ricci scalar is

$$
R
=
-F''(r)
-
\frac{4}{r}F'(r)
-
\frac{2}{r^2}(F(r)-1).
$$

---

# Near-Core Ricci Limit

Using

$$
F(r)
\approx
1-\frac{\Lambda_{\mathrm{eff}}}{3}r^2,
$$

one obtains

$$
F'(r)
\approx
-\frac{2\Lambda_{\mathrm{eff}}}{3}r,
$$

and

$$
F''(r)
\approx
-\frac{2\Lambda_{\mathrm{eff}}}{3}.
$$

Substitution yields

$$
R
\rightarrow
4\Lambda_{\mathrm{eff}}
=
\frac{24M}{r_c^3}.
$$

Therefore the Ricci scalar remains finite at the center.

---

# Ricci Tensor Invariant

The quadratic Ricci invariant is

$$
R_{\mu\nu}R^{\mu\nu}.
$$

For the near-core de Sitter-type structure,

$$
R_{\mu\nu}
=
\Lambda_{\mathrm{eff}}g_{\mu\nu}.
$$

Therefore,

$$
R_{\mu\nu}R^{\mu\nu}
=
4\Lambda_{\mathrm{eff}}^2.
$$

Hence

$$
R_{\mu\nu}R^{\mu\nu}
=
\frac{144M^2}{r_c^6}.
$$

This quantity is finite.

---

# Kretschmann Scalar

The Kretschmann invariant is

$$
K
=
R_{\mu\nu\rho\sigma}
R^{\mu\nu\rho\sigma}.
$$

For de Sitter geometry,

$$
K
=
\frac{8}{3}\Lambda_{\mathrm{eff}}^2.
$$

Substitution gives

$$
K
=
\frac{96M^2}{r_c^6}.
$$

Thus the Kretschmann scalar also remains finite.

---

# Schwarzschild Limit

For large radius,

$$
r\gg r_c,
$$

the lapse function satisfies

$$
F(r)
\rightarrow
1-\frac{2M}{r}.
$$

Therefore:
- the Ricci scalar approaches zero,
- the Ricci tensor invariant approaches zero,
- the Kretschmann scalar approaches the Schwarzschild form

$$
K
\sim
\frac{48M^2}{r^6}.
$$

Thus the TIG effective geometry reproduces the Schwarzschild asymptotic curvature sector.

---

# Geometric Interpretation

The TIG effective geometry replaces the Schwarzschild-type central divergence by a finite de Sitter-type core.

The resulting structure:
- preserves Schwarzschild asymptotics,
- regularizes the effective center,
- and maintains finite curvature invariants throughout the admissible sector.

The regularization follows from the effective mass profile

$$
m(r)\sim r^3
$$

near the center.

---

# Structural Meaning

The curvature regularity is not introduced through:
- ad hoc cutoff procedures,
- coordinate regularization,
- or explicit singularity removal rules.

It follows geometrically from the admissible effective mass profile and the associated lapse function.

---

# Relation to TIG1

TIG1 established the horizon-sector cubic and its effective geometric interpretation.

This TIG2 derivation strengthens the geometric sector by showing that the corresponding curvature invariants remain finite within the effective geometry.

The result therefore supports the internal consistency of the TIG horizon sector.

---

# Structural Stability

The regularity structure depends on:
- the effective near-core scaling,
- spherical symmetry,
- and the admissible interpolation between core and asymptotic regions.

Small admissible perturbations preserving

$$
m(r)\sim r^3
$$

retain finite curvature invariants.

---

# Weakest Step

The curvature analysis depends on the effective geometric ansatz

$$
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
$$

A derivation from a complete nonlinear vacuum tensor system remains unresolved.

This limitation must remain explicit.

---

# Proven Structures

## PR1 — Finite Ricci Scalar

The Ricci scalar remains finite at

$$
r=0.
$$

Status:
rigorous within the effective geometric sector.

## PR2 — Finite Quadratic Ricci Invariant

The invariant

$$
R_{\mu\nu}R^{\mu\nu}
$$

remains finite at the center.

Status:
rigorous within the effective geometric sector.

## PR3 — Finite Kretschmann Scalar

The invariant

$$
K
=
R_{\mu\nu\rho\sigma}
R^{\mu\nu\rho\sigma}
$$

remains finite.

Status:
rigorous within the effective geometric sector.

## PR4 — Schwarzschild Asymptotics

The curvature sector approaches the Schwarzschild geometry for

$$
r\gg r_c.
$$

Status:
rigorous asymptotic result.

---

# Open Problems

## OP1 — Vacuum Interpretation

Determine whether the effective regular core can emerge from a closed vacuum tensor structure.

## OP2 — Global Stability

Determine whether the regular sector remains stable under nonlinear perturbations.

## OP3 — Uniqueness

Determine whether the regularity structure uniquely fixes the effective mass profile.

## OP4 — Covariant Completion

Determine whether the regularized curvature sector admits a fully covariant action principle.

---

# Claim Boundary

This document establishes curvature regularity only within the TIG effective geometric sector.

It does not establish:
- a complete vacuum theory,
- full tensor closure,
- exact singularity resolution in a covariant theory,
- or quantum-gravity completion.

The result is a geometric curvature-sector derivation for TIG2.

---

# Conclusion

The TIG effective geometry

$$
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}
$$

produces finite curvature invariants throughout the admissible geometric sector.

Near the center, the geometry approaches an effective de Sitter-type structure with finite:
- Ricci scalar,
- quadratic Ricci invariant,
- and Kretschmann scalar.

For large radius, the curvature sector approaches the Schwarzschild limit.

This establishes the curvature regularity structure of the TIG2 effective geometric sector.

---

# Classification

derivation candidate
