# Notation Conventions

## Purpose

This document defines the canonical notation conventions for the TIG3 vacuum-sector framework.

Its purpose is:

- notation stability,
- manuscript consistency,
- theorem readability,
- and prevention of symbolic ambiguity.

This document is part of the TIG3 publication-hardening layer.

---

# General Convention

All TIG3 documents should use a fixed notation system.

A symbol must not change meaning between:

- proof-program files,
- paper-architecture files,
- publication-hardening files,
- and future LaTeX manuscripts.

---

# Units and Signature

The default unit convention is:

```text
G = c = 1.
```

The metric signature is:

```text
(-,+,+,+).
```

---

# Coordinates

The standard coordinate system is:

```text
(t,r,theta,phi).
```

The radial coordinate \(r\) is the areal radius.

The angular sector is:

```text
dOmega^2 = dtheta^2 + sin^2(theta)dphi^2.
```

---

# Metric Convention

The representative TIG3 metric is:

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 dOmega^2.
```

The lapse function is:

```text
F(r)
=
1 - 2Mr^2/(r^3+r_c^3).
```

This form should remain canonical.

---

# Core Parameters

| Symbol | Meaning |
|---|---|
| \(M\) | mass parameter |
| \(r_c\) | regulated core scale |
| \(\beta\) | dimensionless structural parameter |
| \(\beta_c\) | critical TIG2 branch value |
| \(x\) | dimensionless horizon coordinate |
| \(r_H\) | horizon radius |

The structural parameter is:

```text
beta = r_c/(2M).
```

The dimensionless horizon coordinate is:

```text
x = r_H/(2M).
```

---

# TIG2 Branch Notation

The canonical branch equation is:

```text
x^3 - x^2 + beta^3 = 0.
```

The critical point is:

```text
x_c = 2/3,
beta_c^3 = 4/27.
```

The discriminant is:

```text
Delta(beta)
=
beta^3(4 - 27 beta^3).
```

---

# Curvature Notation

Use the following curvature notation consistently:

| Symbol | Meaning |
|---|---|
| \(R\) | Ricci scalar |
| \(R_{ab}R^{ab}\) | Ricci contraction |
| \(K\) | Kretschmann scalar |
| \(R_{abcd}R^{abcd}\) | full Kretschmann expression |

When possible, use \(K\) for compact notation.

---

# Perturbation Notation

Metric perturbations are denoted by:

```text
g_ab -> g_ab + h_ab.
```

The perturbative condition is:

```text
|h_ab| << 1.
```

The master perturbation variable is:

```text
Psi(t,r).
```

The radial mode function may be denoted by:

```text
psi(r).
```

Do not use \(Psi\) and \(psi\) interchangeably without definition.

---

# Tortoise Coordinate

The tortoise coordinate is:

```text
dr_*/dr = 1/F(r).
```

Use:

```text
r_*
```

only for the tortoise coordinate.

Do not use \(r_*\) for critical radius or core radius.

---

# Effective Potential Notation

The canonical effective potential symbol is:

```text
V_eff(r).
```

The current candidate structure is:

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

This must be labeled as:

```text
candidate effective potential
```

unless a full derivation is supplied.

---

# Angular Mode Notation

The angular mode number is:

```text
ell.
```

The spherical harmonic indices are:

```text
ell, m.
```

The angular barrier is:

```text
ell(ell+1)/r^2.
```

---

# Operator Notation

The formal TIG3 radial operator is:

```text
L_TIG
=
- d^2/dr_*^2
+
V_eff(r).
```

The Friedrichs self-adjoint realization is:

```text
L_TIG^F.
```

Use \(L_TIG\) for the formal operator.

Use \(L_TIG^F\) only when the self-adjoint realization is explicitly assumed.

---

# Hilbert Space Notation

The perturbative Hilbert space is:

```text
H_TIG = L^2(I,dr_*).
```

Here \(I\) denotes the admissible tortoise-coordinate interval.

The operator domain is:

```text
D(L_TIG).
```

The Friedrichs-domain notation is:

```text
D(L_TIG^F).
```

---

# Quadratic Form Notation

The quadratic form is:

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

The perturbative energy is:

```text
E[Psi](t).
```

Use \(Q\) for spatial quadratic forms.

Use \(E\) for time-dependent perturbative energy.

---

# Spectral Notation

The spectrum of an operator is:

```text
sigma(L_TIG^F).
```

The canonical spectral admissibility condition is:

```text
sigma(L_TIG^F) subset [0,infinity).
```

Do not claim a spectral gap unless explicitly proven.

---

# Frequency Notation

Mode frequencies are denoted by:

```text
omega.
```

The radial spectral equation is:

```text
L_TIG^F psi = omega^2 psi.
```

Negative eigenvalues correspond to:

```text
omega^2 < 0.
```

These generate exponential growth and are excluded by spectral nonnegativity.

---

# Near-Critical Notation

The near-critical regime is:

```text
beta approx beta_c.
```

The exact critical value is:

```text
beta = beta_c.
```

The phrase “near-critical” must always refer to the TIG2 branch-merger regime.

---

# Status Labels

Use the following labels consistently:

| Label | Meaning |
|---|---|
| established | constructed or calculated in current framework |
| conditional | depends on stated assumptions |
| partial | structurally developed but incomplete |
| conjectural | plausible but unproven |
| open | unresolved |
| outside scope | intentionally not addressed |

---

# Prohibited Symbolic Ambiguities

Avoid:

| Ambiguity | Reason |
|---|---|
| using \(r_c\) as critical horizon radius | reserved for core scale |
| using \(x\) for arbitrary coordinate | reserved for dimensionless horizon coordinate |
| using \(L\) without subscript | ambiguous |
| using \(V\) without defining whether effective or geometric | ambiguous |
| using “proof” without conditional status | overclaim risk |

---

# Canonical Publication Notation

The paper should introduce notation in this order:

```text
M, r_c, beta, x, beta_c, F(r), r_*, V_eff, L_TIG, Q, L_TIG^F.
```

This ordering mirrors the theorem dependency graph.

---

# Final Status

This document establishes the canonical notation conventions for the TIG3 publication-hardening program.