# Spectral Nonnegativity Conditions

## Purpose

This document defines the spectral nonnegativity framework for the TIG3 radial stability operator.

The objective is to identify the mathematical conditions under which the self-adjoint TIG3 radial operator possesses nonnegative spectrum and therefore excludes exponentially growing linear perturbation modes.

This document is part of the six-file TIG3 proof-closing sequence.

It follows the self-adjoint realization framework and prepares the bounded linear evolution theorem.

---

# Starting Point

The conditional self-adjoint TIG3 radial operator is denoted by

```text
L_TIG^F.
```

It is obtained, conditionally, as the Friedrichs realization associated with the quadratic form

```text
Q[psi]
=
int_I
(
|d psi/dr_*|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

The central spectral question is:

```text
sigma(L_TIG^F) subset [0, infinity)?
```

---

# Spectral Stability Meaning

If

```text
sigma(L_TIG^F) subset [0, infinity),
```

then the perturbative eigenvalue problem

```text
L_TIG^F psi = omega^2 psi
```

admits no negative eigenvalues.

This excludes modes with

```text
omega^2 < 0,
```

which would generate exponential time growth.

---

# Candidate Effective Potential

The current candidate potential is

```text
V_eff(r)
=
F(r)
[
ell(ell+1)/r^2
+
F'(r)/r
],
```

with

```text
F(r)
=
1 - 2Mr^2/(r^3+r_c^3).
```

The derivative term is

```text
F'(r)/r
=
2M(r^3-2r_c^3)/(r^3+r_c^3)^2.
```

---

# Positivity Decomposition

The quadratic form decomposes as

```text
Q[psi]
=
Q_grad[psi]
+
Q_ang[psi]
+
Q_geom[psi],
```

where

```text
Q_grad[psi]
=
int_I |d psi/dr_*|^2 dr_*,
```

```text
Q_ang[psi]
=
int_I F(r) ell(ell+1)/r^2 |psi|^2 dr_*,
```

and

```text
Q_geom[psi]
=
int_I F(r) F'(r)/r |psi|^2 dr_*.
```

---

# Manifestly Nonnegative Parts

The gradient contribution satisfies

```text
Q_grad[psi] >= 0.
```

In exterior regions where

```text
F(r) >= 0,
```

the angular contribution satisfies

```text
Q_ang[psi] >= 0
```

for all

```text
ell >= 0.
```

Thus any possible negative contribution arises from the geometric term.

---

# Geometric Term Sign Structure

The geometric term is governed by

```text
F'(r)/r
=
2M(r^3-2r_c^3)/(r^3+r_c^3)^2.
```

This changes sign at

```text
r = 2^(1/3) r_c.
```

Therefore \(Q_geom\) is not manifestly nonnegative everywhere.

However, the negative region is finite and localized.

---

# Lower-Bound Condition

A sufficient condition for spectral boundedness below is:

```text
Q[psi] >= -C ||psi||^2
```

for some finite constant \(C\).

A sufficient condition for spectral nonnegativity is stronger:

```text
Q[psi] >= 0
```

for all admissible perturbations.

The first condition yields a semibounded self-adjoint operator.

The second condition yields nonnegative spectrum.

---

# Candidate Nonnegativity Strategy

The TIG3 spectral nonnegativity program should proceed by showing that the negative part of

```text
F(r)F'(r)/r
```

is controlled by the positive gradient and angular terms.

A schematic inequality target is:

```text
int_I |V_-(r)| |psi|^2 dr_*
<=
a int_I |d psi/dr_*|^2 dr_*
+
b int_I |psi|^2 dr_*,
```

with suitable constants

```text
0 <= a < 1,
b >= 0.
```

Here \(V_-(r)\) denotes the negative part of the effective potential.

---

# Strong Nonnegativity Target

If the stronger estimate

```text
int_I |V_-(r)| |psi|^2 dr_*
<=
int_I
(
|d psi/dr_*|^2
+
F(r) ell(ell+1)/r^2 |psi|^2
)
dr_*
```

holds, then

```text
Q[psi] >= 0.
```

This would imply

```text
sigma(L_TIG^F) subset [0, infinity).
```

---

# S-Wave Sector

For

```text
ell = 0,
```

the angular contribution vanishes.

The nonnegativity question becomes most delicate:

```text
Q[psi]
=
int_I |d psi/dr_*|^2 dr_*
+
int_I F(r)F'(r)/r |psi|^2 dr_*.
```

Thus the s-wave sector is the critical spectral test case.

If the s-wave sector is nonnegative, higher angular sectors are expected to be better controlled due to the repulsive angular barrier.

---

# Higher Angular Modes

For

```text
ell > 0,
```

the angular barrier provides additional positivity.

Therefore higher modes may satisfy stronger lower-bound estimates than the s-wave sector.

This suggests the hierarchy:

```text
ell = 0 most delicate,
ell > 0 increasingly stable.
```

This remains to be proven.

---

# Horizon Contribution

At a simple horizon,

```text
F(r_H)=0.
```

Since

```text
V_eff(r)=F(r)[...],
```

the potential vanishes if the bracket remains finite.

Thus the horizon endpoint is expected not to introduce negative spectral divergence.

This remains dependent on endpoint classification.

---

# Spatial Infinity

At spatial infinity,

```text
V_eff(r)
~
ell(ell+1)/r^2
+
O(r^-3).
```

This asymptotic structure is compatible with standard nonnegative continuous spectrum beginning at zero.

---

# Near-Core Sector

For

```text
r << r_c,
```

the s-wave potential behaves approximately as

```text
V_eff(r)
approx
-4M/r_c^3.
```

This is finite but negative.

Therefore the core may produce a finite negative well in the s-wave sector.

The key question is whether this well is shallow enough to avoid negative eigenvalues.

---

# Near-Critical Sector

Near

```text
beta approx beta_c,
```

the effective potential may flatten and develop long near-zero regions.

This may produce:

- low-frequency modes,
- near-threshold resonances,
- delayed relaxation,
- or spectral compression.

Nonnegativity may still hold even if the spectral gap tends to zero.

---

# Spectral Gap Distinction

The TIG3 proof program must distinguish:

```text
sigma(L_TIG^F) subset [0, infinity)
```

from the stronger condition

```text
sigma(L_TIG^F) subset [lambda_0, infinity),
lambda_0 > 0.
```

The first excludes exponential growth.

The second gives a positive spectral gap.

TIG3 currently requires only nonnegativity, not a positive gap.

---

# Preliminary Proposition

## Proposition — Conditional Spectral Nonnegativity

Assume:

1. \(L_TIG^F\) is a self-adjoint Friedrichs realization,
2. the quadratic form \(Q\) is nonnegative on its admissible domain,

```text
Q[psi] >= 0.
```

Then

```text
sigma(L_TIG^F) subset [0, infinity).
```

Consequently, the linearized TIG3 radial sector contains no exponentially growing modes generated by negative eigenvalues.

This proposition is conditional on the nonnegativity of \(Q\).

---

# Current Mathematical Status

The following are currently established:

| Item | Status |
|---|---|
| formal radial operator | established |
| candidate \(V_eff\) | established as candidate |
| self-adjoint realization | conditional |
| lower-boundedness | plausible but unproven |
| nonnegativity | open |
| spectral gap | not required |

---

# Main Open Problem

The key open problem is:

```text
prove Q[psi] >= 0
```

or identify the maximal admissible perturbation sector on which this condition holds.

If full nonnegativity fails, a weaker admissible-sector restriction may be required.

---

# Relation to TIG3 Proof Chain

This file connects:

```text
self-adjoint realization
→ spectral nonnegativity
→ exclusion of exponential growth
→ bounded linear evolution.
```

It therefore prepares the final proof-closing step.

---

# Current Limitations

This document does not prove:

- global spectral positivity,
- absence of all resonances,
- nonlinear stability,
- bounded nonlinear evolution,
- or complete vacuum regularity.

It defines the spectral nonnegativity conditions required for the TIG3 perturbative admissibility theorem.

---

# Next Required Step

The next mathematical step is:

```text
bounded_linear_evolution_theorem.md
```

This will formulate the final conditional linear evolution result derived from self-adjointness and spectral nonnegativity.

---

# Status

This document establishes the spectral nonnegativity framework for the TIG3 radial operator program.