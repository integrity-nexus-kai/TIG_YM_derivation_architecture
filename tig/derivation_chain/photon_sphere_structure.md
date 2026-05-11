# Photon Sphere Structure

## Metadata

Title: Photon Sphere Structure  
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
- critical_branch_structure.md
- effective_metric_ansatz.md
- TIG-Paper-Arxiv.pdf

Rigorous Status:
photon-sphere derivation candidate

Allowed Scope:
photon-sphere structure of the TIG effective horizon sector

Forbidden Expansion:
no observational claim
no waveform claim
no EHT-fit claim
no complete vacuum-closure claim
no quantum interpretation

---

# Purpose

This document derives the photon-sphere structure of the TIG effective geometric sector.

The goal is to determine:
- the photon-sphere equation,
- the Schwarzschild limit,
- the leading TIG correction,
- and the behavior near the critical horizon sector.

The analysis is restricted to the effective geometry defined in:

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

# Null Geodesic Structure

Consider equatorial null geodesics:

$$
\theta=\frac{\pi}{2}.
$$

For null motion,

$$
ds^2=0.
$$

The conserved quantities are:
- energy \(E\),
- angular momentum \(L\).

The radial equation becomes

$$
\dot r^2
+
V_{\mathrm{eff}}(r)
=
E^2,
$$

with effective potential

$$
V_{\mathrm{eff}}(r)
=
\frac{L^2}{r^2}F(r).
$$

---

# Photon Sphere Condition

Circular null geodesics satisfy

$$
\frac{dV_{\mathrm{eff}}}{dr}=0.
$$

This gives the standard condition

$$
rF'(r)-2F(r)=0.
$$

This equation determines the photon-sphere radius.

---

# Derivative of the Lapse Function

The lapse function is

$$
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
$$

Differentiation yields

$$
F'(r)
=
-\frac{
4Mr(r^3+r_c^3)
-
6Mr^4
}{
(r^3+r_c^3)^2
}.
$$

Simplifying:

$$
F'(r)
=
\frac{
2Mr(r^3-2r_c^3)
}{
(r^3+r_c^3)^2
}.
$$

---

# Photon Sphere Equation

Substitute into

$$
rF'(r)-2F(r)=0.
$$

This gives

$$
\frac{
2Mr^2(r^3-2r_c^3)
}{
(r^3+r_c^3)^2
}
-
2\left(
1-\frac{2Mr^2}{r^3+r_c^3}
\right)
=0.
$$

After simplification:

$$
r^6
-
3Mr^5
+
2r^3r_c^3
+
r_c^6
=
0.
$$

This is the TIG photon-sphere equation.

---

# Schwarzschild Limit

For

$$
r_c\rightarrow0,
$$

the equation reduces to

$$
r^5(r-3M)=0.
$$

Hence

$$
r_{\mathrm{ph}}=3M.
$$

Therefore the TIG photon sphere continuously reproduces the Schwarzschild photon sphere.

---

# Dimensionless Variables

Define

$$
y=\frac{r_{\mathrm{ph}}}{M},
\qquad
\alpha=\frac{r_c}{M}.
$$

The photon-sphere equation becomes

$$
y^6
-
3y^5
+
2y^3\alpha^3
+
\alpha^6
=
0.
$$

This defines the dimensionless TIG photon-sphere sector.

---

# Perturbative Expansion

Assume

$$
\alpha\ll1.
$$

Write

$$
y=3+\delta y.
$$

Expanding to leading order gives

$$
\delta y
\sim
-\frac{2}{27}\alpha^3.
$$

Thus the TIG correction shifts the photon sphere inward relative to Schwarzschild.

---

# Geometric Interpretation

The inward shift reflects the regularized near-core geometry.

As the correction scale increases:
- the effective attraction weakens near the center,
- the horizon structure deforms,
- and the unstable photon orbit moves inward.

The correction is perturbatively small in the Schwarzschild-connected regime.

---

# Relation to Criticality

Near the critical horizon sector:
- the photon sphere remains outside the outer horizon branch,
- but the separation decreases,
- and the effective trapping region becomes increasingly shallow.

A complete wave-dynamical analysis is not performed in TIG2.

---

# Structural Stability

The photon-sphere equation follows directly from:
- the effective metric,
- spherical symmetry,
- and null geodesic structure.

It is therefore geometrically stable within the TIG effective sector.

---

# Weakest Step

The weakest step is again the effective geometric ansatz:

$$
F(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
$$

A derivation from a complete nonlinear vacuum system remains unresolved.

This limitation must remain explicit.

---

# Proven Structures

## PR1 — Photon Sphere Equation

The TIG effective geometry yields the photon-sphere equation

$$
r^6
-
3Mr^5
+
2r^3r_c^3
+
r_c^6
=
0.
$$

Status:
rigorous within the effective geometric sector.

## PR2 — Schwarzschild Limit

The Schwarzschild photon sphere

$$
r_{\mathrm{ph}}=3M
$$

is recovered continuously.

Status:
rigorous asymptotic result.

## PR3 — Leading TIG Correction

The leading perturbative correction scales as

$$
\delta y
\sim
-\frac{2}{27}\alpha^3.
$$

Status:
leading-order perturbative result.

---

# Open Problems

## OP1 — Exact Photon-Sphere Branches

Determine the exact global branch structure of the photon-sphere equation.

## OP2 — Wave Dynamics

Determine the effect on quasinormal modes and geometric-optics propagation.

## OP3 — Critical Trapping

Determine the near-critical behavior of unstable null trapping.

## OP4 — Observational Constraints

Determine whether the TIG photon-sphere shift is observationally distinguishable.

---

# Claim Boundary

This document establishes the photon-sphere structure only within the TIG effective geometric sector.

It does not establish:
- observational agreement,
- EHT compatibility,
- exact wave dynamics,
- or full vacuum closure.

The result is a geometric photon-sphere derivation for TIG2.

---

# Conclusion

The TIG effective geometry produces a modified photon-sphere equation given by

$$
r^6
-
3Mr^5
+
2r^3r_c^3
+
r_c^6
=
0.
$$

The Schwarzschild limit is recovered continuously as

$$
r_c\rightarrow0.
$$

The leading TIG correction shifts the photon sphere inward relative to Schwarzschild.

This establishes the photon-sphere structure of the TIG2 effective geometric sector.

---

# Classification

derivation candidate
