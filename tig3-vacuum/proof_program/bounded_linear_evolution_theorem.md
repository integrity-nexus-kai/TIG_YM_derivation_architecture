# Bounded Linear Evolution Theorem

## Purpose

This document formulates the bounded linear evolution theorem for the TIG3 radial perturbation framework.

The objective is to state the final conditional result connecting:

- effective potential structure,
- self-adjoint realization,
- spectral nonnegativity,
- and absence of exponentially growing linear modes.

This document is part of the six-file TIG3 proof-closing sequence.

It follows the spectral nonnegativity framework.

---

# Starting Point

The TIG3 radial perturbation equation is

```text
partial_t^2 Psi
+
L_TIG^F Psi
=
0,
```

where

```text
L_TIG^F
```

denotes the self-adjoint Friedrichs realization of the radial operator

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r).
```

The candidate effective potential is

```text
V_eff(r)
=
F(r)
[
ell(ell+1)/r^2
+
F'(r)/r
].
```

---

# Assumptions

The bounded linear evolution theorem requires the following assumptions.

---

## Assumption A — Representative Background

The background is the representative TIG3 metric sector

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 dOmega^2,
```

with

```text
F(r)
=
1 - 2Mr^2/(r^3+r_c^3),
```

and

```text
M > 0,
r_c > 0.
```

---

## Assumption B — Effective Potential Admissibility

The effective potential is real-valued and locally integrable on the admissible radial interval:

```text
V_eff in L^1_loc(I).
```

---

## Assumption C — Self-Adjoint Realization

The radial operator admits a self-adjoint Friedrichs realization:

```text
L_TIG^F.
```

This requires the associated quadratic form to be:

- densely defined,
- closable,
- and bounded from below.

---

## Assumption D — Spectral Nonnegativity

The spectrum satisfies

```text
sigma(L_TIG^F) subset [0, infinity).
```

Equivalently, the quadratic form satisfies

```text
Q[psi] >= 0
```

on its admissible domain.

---

## Assumption E — Finite-Energy Initial Data

Initial perturbation data satisfy

```text
Psi(0) in D((L_TIG^F)^(1/2)),
```

and

```text
partial_t Psi(0) in H_TIG.
```

Thus the perturbative energy is finite.

---

# Energy Functional

Define the linear perturbative energy

```text
E[Psi](t)
=
1/2
(
||partial_t Psi(t)||^2
+
< Psi(t), L_TIG^F Psi(t) >
).
```

If

```text
L_TIG^F >= 0,
```

then

```text
E[Psi](t) >= 0.
```

---

# Formal Energy Conservation

For sufficiently regular solutions,

```text
dE/dt = 0.
```

Thus

```text
E[Psi](t)
=
E[Psi](0).
```

This expresses linear energy conservation in the admissible perturbation sector.

---

# Theorem — Conditional Bounded Linear Evolution

Assume:

1. the representative TIG3 background satisfies \(M>0\), \(r_c>0\),
2. the effective potential is real-valued and locally integrable,
3. the radial operator admits a self-adjoint Friedrichs realization \(L_TIG^F\),
4. the spectrum is nonnegative,

```text
sigma(L_TIG^F) subset [0, infinity),
```

5. the initial data have finite perturbative energy.

Then the linear TIG3 radial perturbation equation

```text
partial_t^2 Psi
+
L_TIG^F Psi
=
0
```

admits energy-controlled linear evolution.

In particular, no exponentially growing modes arise from negative spectral eigenvalues.

---

# Spectral Interpretation

By the spectral theorem for self-adjoint operators, the solution may be formally represented through the functional calculus of \(L_TIG^F\):

```text
Psi(t)
=
cos(t sqrt(L_TIG^F)) Psi(0)
+
(L_TIG^F)^(-1/2) sin(t sqrt(L_TIG^F)) partial_t Psi(0).
```

On the nonnegative spectral sector, this evolution is oscillatory or threshold-controlled, not exponentially unstable.

---

# Exclusion of Negative-Mode Instability

If a negative eigenvalue existed,

```text
L_TIG^F phi = -lambda phi,
lambda > 0,
```

then the time-dependent mode would behave as

```text
exp(sqrt(lambda) t).
```

This would violate bounded linear admissibility.

Therefore spectral nonnegativity excludes this instability mechanism.

---

# What the Theorem Establishes

Under the stated assumptions, TIG3 obtains:

- bounded curvature background,
- well-defined linear radial operator,
- self-adjoint spectral evolution,
- exclusion of negative-mode exponential growth,
- and finite-energy perturbative admissibility.

---

# What the Theorem Does Not Establish

This theorem does not prove:

- nonlinear stability,
- global causal completeness,
- full singularity elimination,
- complete covariant field equations,
- observational confirmation,
- or uniqueness of the representative geometry.

It is a conditional linear perturbative admissibility result.

---

# Near-Critical Interpretation

Near

```text
beta approx beta_c,
```

the spectral gap may shrink or vanish.

This does not necessarily violate spectral nonnegativity.

It may instead correspond to:

- slow relaxation,
- near-threshold modes,
- long-lived perturbations,
- or metastable behavior.

These effects require separate resonance analysis.

---

# Relation to TIG3 Vacuum Proof

This theorem closes the current linear proof chain:

```text
bounded curvature
→ perturbative reduction
→ effective potential
→ quadratic form
→ self-adjoint realization
→ spectral nonnegativity
→ bounded linear evolution.
```

It therefore provides the conservative mathematical form of the current TIG3 vacuum admissibility result.

---

# Final Conditional Statement

The representative TIG3 vacuum sector is curvature-bounded and linearly perturbatively admissible provided the effective radial operator admits a nonnegative self-adjoint realization on the specified finite-energy domain.

This is the strongest conservative TIG3 vacuum-proof statement currently justified by the framework.

---

# Status

This document establishes the bounded linear evolution theorem candidate for the TIG3 vacuum-sector program.