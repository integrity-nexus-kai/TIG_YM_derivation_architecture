# Radial Stability Operator

## Purpose

This document defines the preliminary radial stability-operator framework for the TIG3 representative metric sector.

The objective is to begin translating bounded curvature and near-critical branch behavior into a perturbative stability language.

This document does not establish a full nonlinear stability theorem.

It defines the first operator-level structure required for future TIG3 dynamical analysis.

---

# Starting Point

We use the representative TIG3 metric sector

```text
ds^2 = -F(r) dt^2 + dr^2/F(r) + r^2 dOmega^2
```

with

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

The TIG3 curvature-sector analysis shows that this representative geometry possesses finite core curvature invariants for

```text
r_c > 0.
```

The next question is whether small admissible perturbations around this sector remain dynamically controlled.

---

# Perturbative Ansatz

Let a radial perturbation of the representative geometry be denoted by

```text
F(r) -> F(r) + epsilon psi(t,r),
```

where:

- epsilon is a formal perturbation parameter,
- psi(t,r) is a radial perturbation mode,
- and the perturbation is assumed small in the admissible regime.

This ansatz is not yet a full covariant perturbation theory.

It is a minimal radial stability model.

---

# Effective Mode Equation

A first admissible stability model takes the schematic form

```text
partial_t^2 psi - partial_r_*^2 psi + V_eff(r) psi = 0,
```

where:

```text
dr_*/dr = 1/F(r)
```

defines the tortoise coordinate in the admissible exterior sector, and

```text
V_eff(r)
```

is an effective radial stability potential.

The precise form of V_eff(r) remains to be derived from the chosen perturbation class.

---

# Operator Form

The radial stability equation may be written formally as

```text
partial_t^2 psi + L_TIG psi = 0,
```

with radial operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r).
```

The stability question becomes:

Does L_TIG admit a nonnegative spectrum on the admissible perturbation domain?

---

# Admissible Domain

The perturbation domain must be chosen to preserve:

- regularity at the regulated core,
- compatibility with horizon branch structure,
- asymptotic decay,
- and finite perturbative energy.

A candidate admissible domain is

```text
D(L_TIG) subset L^2(dr_*)
```

with boundary conditions determined by:

- regularity near the core,
- finite energy,
- and asymptotic GR compatibility.

The exact functional domain remains open.

---

# Stability Criterion

A preliminary linear stability criterion is:

```text
sigma(L_TIG) subset [0, infinity).
```

If this holds, then no exponentially growing radial perturbation modes occur at the linear level.

Equivalently, the quadratic form

```text
Q[psi] = integral ( |d psi/dr_*|^2 + V_eff(r)|psi|^2 ) dr_*
```

should satisfy

```text
Q[psi] >= 0
```

for all admissible perturbations psi.

This is a future theorem target, not yet established.

---

# Near-Critical Role

The near-critical regime

```text
beta approx beta_c
```

may influence the radial operator through:

- deformation of F(r),
- horizon-branch merger,
- effective potential flattening,
- long-lived metastable modes,
- and amplified relaxation times.

Thus the radial stability operator is the natural mathematical object for analyzing TIG3 relaxation behavior.

---

# Relation to Bounded Curvature

The bounded-curvature analysis establishes that the representative background geometry is finite at the regulated core.

The radial stability-operator program asks the next question:

Are small admissible perturbations around that bounded background dynamically controlled?

This shifts TIG3 from static admissibility toward dynamical admissibility.

---

# Preliminary Proposition Target

## Proposition - Radial Linear Stability Candidate

For the representative TIG3 metric sector, if the effective stability operator

```text
L_TIG = - d^2/dr_*^2 + V_eff(r)
```

is self-adjoint and nonnegative on an admissible perturbation domain, then the corresponding radial perturbation sector contains no exponentially growing linear modes.

This is currently a theorem target, not a proven result.

---

# Mathematical Obstacles

To make this operator framework rigorous, TIG3 must still define:

1. the exact perturbation class,
2. the effective potential V_eff(r),
3. the correct inner product,
4. the admissible boundary conditions,
5. self-adjointness of L_TIG,
6. spectral lower bounds,
7. and near-critical spectral behavior.

---

# Structural Interpretation

The radial stability operator provides the first mathematical bridge between:

- bounded curvature,
- near-critical branch geometry,
- and dynamical relaxation behavior.

It is therefore the correct formal object for investigating whether TIG3 core dynamics can remain bounded under small perturbations.

---

# Explicit Restrictions

This document does not claim:

- nonlinear stability,
- spectral gap,
- Yang-Mills relation,
- observational prediction,
- or complete dynamical proof.

It defines only the preliminary operator architecture for future TIG3 stability analysis.

---

# Status

This document establishes the first operator-level framework for radial TIG3 stability analysis.