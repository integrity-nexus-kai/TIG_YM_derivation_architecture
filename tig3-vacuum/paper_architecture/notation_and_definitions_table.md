# Notation and Definitions Table

## Purpose

This document defines the core notation, symbols, and terminology used throughout the TIG3 vacuum-sector program.

The objective is to maintain:

- mathematical consistency,
- notation stability,
- publication clarity,
- and conceptual discipline.

All symbols should retain fixed meaning throughout the TIG3 manuscript.

---

# Core Structural Parameters

| Symbol | Definition | Interpretation |
|---|---|---|
| \(M\) | mass parameter | asymptotic gravitational mass |
| \(r_c\) | structural core scale | regulated TIG3 core radius |
| \(\beta\) | \(r_c/(2M)\) | dimensionless structural control parameter |
| \(\beta_c\) | \((4/27)^{1/3}\) | exact TIG2 critical parameter |
| \(x\) | \(r_H/(2M)\) | dimensionless horizon coordinate |
| \(r_H\) | horizon radius | admissible horizon location |

---

# TIG2 Branch Structure

## Cubic Branch Equation

The exact TIG2 branch equation is

```text
x^3 - x^2 + \beta^3 = 0.
```

---

## Discriminant

The discriminant is

```text
\Delta(\beta)
=
\beta^3(4 - 27\beta^3).
```

Interpretation:

| Condition | Interpretation |
|---|---|
| \(\Delta > 0\) | distinct admissible horizon branches |
| \(\Delta = 0\) | critical branch merger |
| \(\Delta < 0\) | non-admissible branch sector |

---

## Critical Point

The exact critical point is

```text
x_c = 2/3,
\qquad
\beta_c^3 = 4/27.
```

---

# Representative TIG3 Metric Sector

## Metric

The representative TIG3 metric is

```text
ds^2
=
-F(r)dt^2
+
dr^2/F(r)
+
r^2 d\Omega^2.
```

---

## Lapse Function

The representative lapse function is

```text
F(r)
=
1 - \frac{2Mr^2}{r^3 + r_c^3}.
```

Interpretation:

| Regime | Behavior |
|---|---|
| \(r \to \infty\) | Schwarzschild recovery |
| \(r \ll r_c\) | regulated core sector |
| \(\beta \to 0\) | GR-compatible limit |

---

# Curvature Quantities

| Symbol | Definition |
|---|---|
| \(K\) | Kretschmann scalar |
| \(R\) | Ricci scalar |
| \(R_{ab}R^{ab}\) | Ricci contraction |

---

## Core Curvature Values

### Kretschmann Scalar

```text
K(0)
=
96M^2/r_c^6.
```

---

### Ricci Scalar

```text
R(0)
=
24M/r_c^3.
```

---

### Ricci Contraction

```text
R_{ab}R^{ab}(0)
=
144M^2/r_c^6.
```

---

# Perturbative Framework

## Tortoise Coordinate

The tortoise coordinate satisfies

```text
dr_*/dr = 1/F(r).
```

---

## Radial Stability Operator

The formal TIG3 radial operator is

```text
L_{TIG}
=
- \frac{d^2}{dr_*^2}
+
V_{eff}(r).
```

Interpretation:

| Term | Meaning |
|---|---|
| \(L_{TIG}\) | radial perturbation operator |
| \(V_{eff}(r)\) | effective perturbation potential |
| \(r_*\) | tortoise coordinate |

---

## Effective Potential

The preliminary effective potential ansatz is

```text
V_{eff}(r)
=
F(r)
\left[
\frac{\ell(\ell+1)}{r^2}
+
\frac{F'(r)}{r}
+
\mu_{eff}(r)
\right].
```

---

# Spectral Framework

| Symbol | Definition |
|---|---|
| \(H_{TIG}\) | perturbative Hilbert space |
| \(D(L_{TIG})\) | admissible operator domain |
| \(\sigma(L_{TIG})\) | spectrum of the radial operator |
| \(Q[\psi]\) | quadratic form |
| \(E[\psi]\) | perturbative energy functional |

---

## Hilbert Space

The preliminary perturbative Hilbert space is

```text
H_{TIG} = L^2(dr_*).
```

---

## Perturbative Energy

The perturbative energy functional is

```text
E[\psi]
=
\frac12
\int
\left(
|\partial_t \psi|^2
+
|\partial_{r_*}\psi|^2
+
V_{eff}(r)|\psi|^2
\right)
dr_*.
```

---

## Quadratic Form

The quadratic form associated with the operator is

```text
Q[\psi]
=
\int
\left(
|d\psi/dr_*|^2
+
V_{eff}(r)|\psi|^2
\right)
dr_*.
```

---

# Spectral Admissibility Conditions

The central spectral admissibility target is

```text
\sigma(L_{TIG})
\subset
[0,\infty).
```

Interpretation:

| Condition | Meaning |
|---|---|
| nonnegative spectrum | exclusion of exponentially growing linear modes |
| finite energy | perturbative admissibility |
| self-adjoint realization | mathematically controlled spectral dynamics |

---

# Near-Critical Regime

The near-critical regime is defined by

```text
\beta \approx \beta_c.
```

Possible structural consequences include:

- discriminant collapse,
- curvature amplification,
- effective-potential flattening,
- metastable perturbative relaxation.

These remain partially conjectural.

---

# Terminology Conventions

| Term | Meaning |
|---|---|
| admissible | mathematically consistent within the TIG3 framework |
| regulated core | bounded-curvature core sector |
| branch criticality | discriminant-collapse regime |
| metastable mode | long-lived bounded perturbative mode candidate |
| bounded continuation | perturbative/geometric continuation without immediate curvature divergence |

---

# Explicit Restrictions

The following expressions are not used as formal mathematical claims:

| Expression | Status |
|---|---|
| “singularity eliminated” | prohibited claim |
| “quantum gravity completion” | not part of TIG3 |
| “proof of black-hole stability” | not established |
| “core breathing” | heuristic shorthand only |
| “replacement of General Relativity” | explicitly excluded |

---

# Style Conventions

The TIG3 program adopts the following conventions:

| Convention | Choice |
|---|---|
| signature | \((- + + +)\) |
| units | geometric units \(G=c=1\) |
| perturbation theory | linearized only |
| geometry | static spherically symmetric representative sector |
| asymptotics | Schwarzschild-compatible |

---

# Strategic Interpretation

The TIG3 notation system is designed to support:

- conservative mathematical presentation,
- operator-theoretic consistency,
- perturbative stability analysis,
- and bounded-curvature admissibility studies.

The framework should be interpreted as:

```text
structural gravitational admissibility analysis
```

rather than a complete alternative gravity theory.

---

# Status

This document establishes the notation and terminology framework for the TIG3 vacuum-sector program.