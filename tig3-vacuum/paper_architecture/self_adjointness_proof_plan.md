# Self-Adjointness Proof Plan

## Purpose

This document defines the rigorous proof strategy for establishing a self-adjoint realization of the TIG3 radial stability operator.

The objective is to convert the current formal perturbative operator framework into a mathematically controlled spectral system suitable for:

- perturbative admissibility,
- spectral analysis,
- bounded evolution studies,
- and metastable-mode investigation.

This document is not itself a proof.

It defines the proof architecture.

---

# Central Operator

The formal TIG3 radial stability operator is

```text
L_TIG
=
- \frac{d^2}{dr_*^2}
+
V_eff(r).
```

The central mathematical problem is to determine whether this operator admits a self-adjoint realization on an admissible perturbation domain.

---

# Strategic Objective

The long-term theorem target is:

```text
L_TIG
admits a self-adjoint realization
with controlled spectral structure.
```

This is the mathematical foundation required for:

- spectral admissibility,
- perturbative boundedness,
- and linear stability analysis.

---

# Background Geometry

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

The tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

The operator domain depends critically on the global structure of the admissible tortoise interval.

---

# Proof Architecture Overview

The proof program is organized as:

```text
effective potential
→ admissible Hilbert space
→ minimal symmetric operator
→ endpoint classification
→ self-adjoint extension
→ spectral control.
```

---

# Step 1 — Effective Potential Control

The first prerequisite is an explicit derivation of

```text
V_eff(r).
```

Required properties include:

| Property | Purpose |
|---|---|
| real-valuedness | symmetry |
| local integrability | operator definition |
| asymptotic control | spectral analysis |
| near-core boundedness | admissibility |
| near-critical behavior | stability analysis |

Without explicit \(V_eff(r)\), self-adjointness remains formal.

---

# Step 2 — Hilbert Space Construction

Define the perturbative Hilbert space

```text
H_TIG = L^2(I,dr_*),
```

where \(I\) is the admissible radial interval.

The exact structure of \(I\) depends on:

- horizon branches,
- tortoise-coordinate behavior,
- near-core continuation,
- and asymptotic geometry.

---

# Step 3 — Minimal Operator Definition

Define the minimal operator

```text
L_min psi
=
L_TIG psi,
```

with domain

```text
D(L_min)
=
C_c^\infty(I).
```

The first proof task is to establish:

```text
L_min symmetric.
```

This follows if \(V_eff(r)\) is real-valued.

---

# Step 4 — Operator Closure

Determine whether:

```text
L_min
```

is closable.

Construct the closure

```text
\overline{L_min}.
```

This is required before spectral analysis becomes mathematically meaningful.

---

# Step 5 — Endpoint Classification

Each endpoint of the admissible radial interval must be classified.

Possible endpoints include:

| Endpoint | Interpretation |
|---|---|
| regulated core | bounded-curvature center |
| horizon branch | admissible horizon |
| asymptotic infinity | GR-compatible exterior |
| merged critical branch | near-critical geometry |

Each endpoint must be analyzed using:

```text
limit-point / limit-circle theory.
```

---

# Step 6 — Boundary Conditions

If an endpoint is limit-circle, admissible boundary conditions must be imposed.

Possible admissibility conditions include:

| Condition | Interpretation |
|---|---|
| finite perturbation norm | perturbative admissibility |
| finite energy | physical admissibility |
| regularity at core | bounded continuation |
| asymptotic decay | spectral control |

This stage determines the admissible operator domain.

---

# Step 7 — Quadratic Form Analysis

Define the quadratic form

```text
Q[\psi]
=
\int
(
|d\psi/dr_*|^2
+
V_eff(r)|\psi|^2
)
dr_*.
```

Required properties:

| Property | Purpose |
|---|---|
| densely defined | operator construction |
| closable | extension theory |
| bounded below | Friedrichs extension |
| nonnegative | spectral admissibility |

---

# Step 8 — Friedrichs Extension

If

```text
Q[\psi] \ge -C ||\psi||^2,
```

then the Friedrichs construction yields a self-adjoint operator associated with the closed quadratic form.

If additionally

```text
Q[\psi] \ge 0,
```

then the operator spectrum satisfies

```text
\sigma(L_TIG)
\subset
[0,\infty).
```

This is the central spectral admissibility target.

---

# Step 9 — Near-Critical Analysis

The regime

```text
\beta \approx \beta_c
```

requires separate analysis.

Potential complications include:

- tortoise stretching,
- branch merger,
- effective-potential flattening,
- resonance accumulation,
- and slow spectral decay.

The near-critical regime may require weighted-function-space methods.

---

# Step 10 — Spectral Consequences

If self-adjointness and spectral nonnegativity are established, then:

| Result | Consequence |
|---|---|
| self-adjoint operator | well-defined spectral evolution |
| nonnegative spectrum | exclusion of exponentially growing linear modes |
| closed quadratic form | bounded energy structure |
| admissible domain | controlled perturbative sector |

This would establish the first rigorous spectral admissibility structure of TIG3.

---

# Candidate Theorem Targets

## Theorem Target A — Self-Adjoint Realization

Under admissible geometric and perturbative conditions, the TIG3 radial stability operator admits a self-adjoint realization on a suitable Hilbert space.

---

## Theorem Target B — Spectral Nonnegativity

Under admissible geometric conditions, the spectrum satisfies

```text
\sigma(L_TIG)
\subset
[0,\infty).
```

---

## Theorem Target C — Bounded Linear Evolution

Finite-energy admissible perturbations remain bounded under linear evolution generated by the self-adjoint radial operator.

---

# Expected Mathematical Obstacles

The proof program may encounter several major difficulties:

| Problem | Status |
|---|---|
| explicit \(V_eff\) derivation | open |
| endpoint regularity | open |
| near-critical spectral compression | open |
| resonance accumulation | open |
| positivity estimates | open |
| nonlinear continuation | outside current scope |

---

# Explicit Non-Claims

This program does not currently establish:

- nonlinear stability,
- complete singularity exclusion,
- quantum gravity,
- global causal completeness,
- or observational verification.

The framework remains a perturbative operator-theoretic admissibility program.

---

# Strategic Interpretation

The self-adjointness proof program represents the transition of TIG3 from:

```text
heuristic perturbative structure
```

to:

```text
mathematically controlled spectral theory.
```

This is likely the most technically demanding part of the entire TIG3 framework.

---

# Relation to Existing TIG3 Structure

This proof architecture connects:

```text
curvature admissibility
→ perturbation theory
→ operator construction
→ spectral analysis
→ bounded evolution.
```

It therefore forms the mathematical backbone of the TIG3 perturbative sector.

---

# Status

This document establishes the self-adjointness proof roadmap for the TIG3 vacuum-sector program.