# Effective Potential Derivation Plan

## Purpose

This document defines the mathematical derivation program for the TIG3 effective perturbation potential

```text
V_eff(r).
```

The objective is to replace the current heuristic effective-potential ansatz with a systematically derived perturbative structure obtained from the representative TIG3 metric sector.

This is one of the central unresolved mathematical problems of the TIG3 vacuum program.

---

# Current Situation

The TIG3 perturbative framework currently uses the formal radial operator

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r),
```

with the preliminary ansatz

```text
V_eff(r)
=
F(r)
\left[
\frac{\ell(\ell+1)}{r^2}
+
\frac{F'(r)}{r}
+
\mu_eff(r)
\right].
```

At present this expression is structurally motivated but not rigorously derived from perturbation equations.

---

# Central Mathematical Goal

The primary goal is:

```text
derive V_eff(r)
from linearized perturbations
of the representative TIG3 geometry.
```

This requires a controlled perturbative reduction of the metric dynamics into a radial Schrödinger-type operator form.

---

# Representative Background Geometry

The representative TIG3 metric sector is

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 d\Omega^2,
```

with

```text
F(r)
=
1 - \frac{2Mr^2}{r^3 + r_c^3}.
```

The derivation program begins from this fixed background geometry.

---

# Perturbation Strategy

The derivation program should proceed analogously to classical black-hole perturbation theory.

The central stages are:

```text
background geometry
→ metric perturbation
→ gauge reduction
→ angular decomposition
→ radial master equation
→ effective potential.
```

---

# Step 1 — Metric Perturbations

Introduce linear perturbations

```text
g_ab
→
g_ab + h_ab,
```

where

```text
|h_ab| << 1.
```

The perturbations should preserve:

- spherical symmetry of the background,
- linearized consistency,
- and perturbative admissibility.

---

# Step 2 — Tensor Harmonic Decomposition

Decompose perturbations into spherical tensor harmonics.

Candidate sectors include:

| Sector | Interpretation |
|---|---|
| axial sector | odd-parity perturbations |
| polar sector | even-parity perturbations |

This follows the standard Regge–Wheeler/Zerilli philosophy.

---

# Step 3 — Gauge Reduction

A gauge choice must eliminate nonphysical perturbative degrees of freedom.

Candidate approaches include:

- Regge–Wheeler gauge,
- generalized admissible gauge conditions,
- or gauge-invariant master variables.

This stage is critical.

---

# Step 4 — Master Equation Construction

The reduced perturbation equations should be rewritten in the form

```text
\partial_t^2 \Psi
-
\partial_{r_*}^2 \Psi
+
V_eff(r)\Psi
=
0.
```

The objective is to isolate a single radial master variable

```text
\Psi(t,r).
```

---

# Step 5 — Explicit Potential Extraction

Once the master equation is obtained, the effective potential should be identified explicitly.

The resulting \(V_eff(r)\) should depend on:

| Quantity | Role |
|---|---|
| \(F(r)\) | background geometry |
| \(F'(r)\) | radial structure |
| \(\ell\) | angular harmonic index |
| \(r_c\) | regulated core scale |
| \(\beta\) | near-critical control parameter |

---

# Step 6 — Near-Core Analysis

The derived potential must be analyzed for

```text
r \ll r_c.
```

Key questions:

- Does the potential remain finite?
- Does the core behave regularly?
- Are singular Schwarzschild divergences removed?
- Is perturbative control maintained?

This is central to TIG3 admissibility.

---

# Step 7 — Asymptotic Analysis

The derived potential must satisfy:

```text
r \to \infty
```

→ Schwarzschild-compatible asymptotics.

This ensures compatibility with the GR limit.

---

# Step 8 — Near-Critical Analysis

The regime

```text
\beta \approx \beta_c
```

must be analyzed separately.

Questions include:

- Does potential flattening occur?
- Are metastable sectors enhanced?
- Does tortoise stretching appear?
- Are resonance-like structures possible?

This stage connects TIG2 criticality to TIG3 perturbative dynamics.

---

# Step 9 — Operator Construction

Once \(V_eff(r)\) is derived, define:

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r)
```

on an admissible perturbation domain.

This enables:

- self-adjointness analysis,
- spectral admissibility,
- resonance investigation,
- and bounded-evolution studies.

---

# Expected Mathematical Difficulties

The derivation program is expected to face several obstacles:

| Problem | Difficulty |
|---|---|
| gauge fixing | nontrivial |
| horizon structure | branch-sensitive |
| near-core regularity | delicate |
| near-critical behavior | potentially singular |
| spectral positivity | open |
| operator closure | open |

---

# Conservative Mathematical Position

The TIG3 program currently does not claim:

- full covariant field equations,
- exact perturbative closure,
- nonlinear stability,
- or uniqueness of the effective potential.

The objective is only:

```text
derive a mathematically admissible perturbative operator structure.
```

---

# Preliminary Proposition Target

## Proposition — Effective Potential Derivation Target

Given a representative admissible TIG3 background geometry and a consistent linear perturbation reduction, there exists a radial master equation of Schrödinger type with an associated effective perturbation potential

```text
V_eff(r).
```

This remains an open derivation target.

---

# Relation to Existing TIG3 Structure

This derivation program connects:

```text
bounded curvature
→ perturbation theory
→ operator structure
→ spectral admissibility.
```

It is therefore one of the central mathematical bridges of the TIG3 framework.

---

# Future Outputs

Successful completion of this program would provide:

1. explicit \(V_eff(r)\),
2. controlled perturbation equations,
3. self-adjointness input,
4. spectral analysis foundation,
5. metastable-mode analysis,
6. numerical perturbation framework.

---

# Explicit Non-Claims

This document does not establish:

- exact perturbation equations,
- uniqueness of \(V_eff(r)\),
- spectral positivity,
- nonlinear dynamics,
- or observational predictions.

It defines the derivation roadmap only.

---

# Strategic Importance

The effective-potential derivation program is likely the single most important unresolved technical step in TIG3.

Without it:

- spectral admissibility,
- metastable modes,
- and operator-theoretic stability

remain partially heuristic.

---

# Status

This document establishes the derivation roadmap for the TIG3 effective perturbation potential.