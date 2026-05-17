# Endpoint Classification

## Purpose

This document defines the endpoint-classification program for the TIG3 radial stability operator.

The objective is to identify the admissible radial endpoints of the representative TIG3 perturbation problem and classify them for future self-adjointness and spectral analysis.

This document is part of the six-file TIG3 proof-closing sequence.

It follows the explicit effective-potential structure and prepares the quadratic-form analysis.

---

# Starting Point

The TIG3 radial operator is

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r),
```

where the tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

The representative TIG3 lapse is

```text
F(r)
=
1 - 2Mr^2/(r^3+r_c^3).
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

Endpoint classification is required before a rigorous self-adjoint realization of \(L_{TIG}\) can be defined.

---

# Radial Domain

The areal coordinate satisfies

```text
r >= 0.
```

However, the spectral problem is formulated in the tortoise coordinate

```text
r_*.
```

The admissible interval depends on:

- core behavior at \(r=0\),
- horizon zeros of \(F(r)\),
- exterior asymptotics as \(r\to\infty\),
- and the TIG2 branch sector controlled by \(\beta\).

---

# Relevant Endpoints

The possible endpoints are:

| Endpoint | Meaning |
|---|---|
| \(r=0\) | regulated core |
| \(r=r_H\) | admissible horizon branch |
| \(r\to\infty\) | asymptotic exterior |
| \(r_H\to r_c\)-type merger | near-critical branch limit |

The precise spectral interval depends on which physical sector is studied.

---

# Endpoint A — Regulated Core

At

```text
r -> 0,
```

the lapse satisfies

```text
F(r)
≈
1 - (2M/r_c^3) r^2.
```

Thus

```text
dr_*/dr ≈ 1,
```

and the tortoise coordinate remains locally regular near the core.

Therefore the regulated core is not a Schwarzschild-type singular endpoint in the representative geometry.

---

# Core Potential Behavior

Near the core,

```text
F'(r)/r
≈
-4M/r_c^3.
```

Thus the geometric part of \(V_{eff}\) remains finite.

However,

```text
ell(ell+1)/r^2
```

remains singular for

```text
ell > 0.
```

Therefore:

- the \(ell=0\) sector is regular at the core,
- the \(ell>0\) sectors require singular-endpoint analysis.

---

# Preliminary Core Classification

## \(ell=0\)

For the s-wave sector, the endpoint \(r=0\) is expected to behave as a regular endpoint.

Candidate boundary conditions include:

```text
psi finite at r=0
```

and possibly

```text
d psi/dr_* = 0 at r=0.
```

## \(ell>0\)

For higher angular modes, the centrifugal term produces a singular inverse-square structure.

These sectors require limit-point / limit-circle analysis.

The classification is not yet proven.

---

# Endpoint B — Horizon Branch

Horizon locations satisfy

```text
F(r_H)=0.
```

Equivalently, in TIG2 variables,

```text
x^3 - x^2 + beta^3 = 0.
```

At a simple horizon,

```text
F(r) ≈ F'(r_H)(r-r_H).
```

Then

```text
r_* -> ± infinity.
```

Thus simple horizons typically become infinite endpoints in tortoise coordinates.

---

# Horizon Endpoint Classification

For simple horizons, the radial equation asymptotically approaches a free-wave form if

```text
V_eff(r) -> 0
```

as

```text
r -> r_H.
```

Since

```text
V_eff(r)
=
F(r)[...],
```

the potential vanishes at simple horizons if the bracket remains finite.

Thus simple horizon endpoints are expected to be limit-point type, but this remains to be verified.

---

# Endpoint C — Spatial Infinity

For

```text
r -> infinity,
```

the lapse satisfies

```text
F(r)
=
1 - 2M/r + O(r^-4).
```

The tortoise coordinate satisfies asymptotically

```text
r_* ~ r + 2M log r.
```

The effective potential behaves as

```text
V_eff(r)
~
ell(ell+1)/r^2 + O(r^-3).
```

Thus spatial infinity is an infinite endpoint.

It is expected to be limit-point for the usual finite-energy sector.

---

# Endpoint D — Near-Critical Branch Merger

At

```text
beta = beta_c,
```

the TIG2 horizon branches merge.

The critical point satisfies

```text
x_c = 2/3,
beta_c^3 = 4/27.
```

In this regime the horizon is degenerate.

The local form of \(F(r)\) near the merged branch may generate enhanced tortoise stretching and altered endpoint behavior.

---

# Near-Critical Endpoint Risk

The near-critical endpoint is the most delicate case.

Potential issues include:

- degenerate horizon behavior,
- long throat formation,
- near-zero effective potential regions,
- resonance accumulation,
- and slow relaxation.

This endpoint requires separate asymptotic analysis.

---

# Limit-Point / Limit-Circle Program

For each endpoint, one must analyze solutions of

```text
L_TIG psi = lambda psi
```

near the endpoint.

An endpoint is:

```text
limit-point
```

if at most one square-integrable solution exists.

It is:

```text
limit-circle
```

if all local solutions are square-integrable and an additional boundary condition is required.

---

# Boundary Conditions

Candidate admissible boundary conditions include:

| Endpoint | Candidate condition |
|---|---|
| core, \(ell=0\) | regularity / evenness |
| core, \(ell>0\) | finite energy |
| simple horizon | finite flux or scattering condition |
| infinity | finite energy / decay |
| critical horizon | separate weighted condition |

The final domain of \(L_{TIG}\) depends on this classification.

---

# Functional-Analytic Consequence

Endpoint classification determines whether the minimal operator

```text
L_min
```

is essentially self-adjoint or requires self-adjoint extension.

If endpoints are limit-point, no boundary data are required there.

If endpoints are limit-circle, admissible boundary conditions must be imposed.

---

# Preliminary Classification Table

| Endpoint | Expected type | Status |
|---|---|---|
| core, \(ell=0\) | regular | plausible |
| core, \(ell>0\) | singular inverse-square | open |
| simple horizon | limit-point | expected |
| spatial infinity | limit-point | expected |
| critical branch merger | delicate / open | unresolved |

---

# Relation to TIG3 Proof Chain

This file connects:

```text
explicit V_eff structure
→ endpoint classification
→ quadratic form analysis
→ self-adjoint realization
→ spectral admissibility.
```

It therefore prepares the rigorous operator-domain construction.

---

# Current Limitations

This document does not yet prove:

- endpoint classification,
- essential self-adjointness,
- spectral positivity,
- boundary uniqueness,
- or bounded evolution.

It defines the required endpoint-analysis roadmap.

---

# Next Required Step

The next mathematical step is:

```text
quadratic_form_analysis.md
```

This will study whether the associated quadratic form is:

- densely defined,
- closable,
- bounded from below,
- and possibly nonnegative.

---

# Status

This document establishes the endpoint-classification framework for the TIG3 radial operator program.