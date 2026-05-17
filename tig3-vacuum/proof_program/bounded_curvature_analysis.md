# Bounded Curvature Analysis

## Purpose

This document begins the first explicit mathematical analysis block of TIG3.

The objective is to test whether the representative minimal TIG3 metric sector admits bounded curvature behavior in the regulated core region.

This is not yet a complete vacuum proof, but it is the first concrete curvature-control calculation in the TIG3 admissibility program.

---

# Minimal Metric Sector

We use the representative static spherically symmetric TIG3 sector

```text
ds^2 = -F(r) dt^2 + dr^2 / F(r) + r^2 dOmega^2
```

with lapse function

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

Here:

- M is the asymptotic mass scale,
- r_c is the structural core scale,
- beta = r_c / (2M) is the TIG structural control parameter.

This metric sector is representative and not claimed to be unique.

---

# Curvature Control Target

For metrics of the form

```text
ds^2 = -F(r) dt^2 + dr^2 / F(r) + r^2 dOmega^2,
```

the Kretschmann scalar may be written as

```text
K(r) = [F''(r)]^2 + 4 [F'(r)/r]^2 + 4 [(1 - F(r))/r^2]^2.
```

The TIG3 bounded-curvature target is

```text
sup_r K(r) < infinity.
```

---

# Derivatives of the TIG3 Lapse

For

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3),
```

the first derivative is

```text
F'(r) = 2 M r (r^3 - 2 r_c^3)/(r^3 + r_c^3)^2.
```

The second derivative is

```text
F''(r) = -4 M (r_c^6 - 7 r_c^3 r^3 + r^6)/(r^3 + r_c^3)^3.
```

---

# Kretschmann Scalar

Substitution gives the exact curvature expression

```text
K(r) = 48 M^2
       (2 r_c^12 - 2 r_c^9 r^3 + 18 r_c^6 r^6 - 4 r_c^3 r^9 + r^12)
       /(r^3 + r_c^3)^6.
```

This expression is finite for all r >= 0 provided r_c > 0.

---

# Core Limit

At the regulated core,

```text
r -> 0,
```

the Kretschmann scalar satisfies

```text
K(0) = 96 M^2 / r_c^6.
```

Thus the representative TIG3 sector avoids curvature divergence at r = 0 as long as the structural core scale is nonzero.

In terms of beta = r_c/(2M), this becomes

```text
K(0) = 3 / (2 beta^6 M^4).
```

This shows explicitly that beta acts as a curvature regulator in the representative metric sector.

---

# Asymptotic Limit

For large radius,

```text
r -> infinity,
```

the lapse behaves as

```text
F(r) = 1 - 2M/r + O(r^-4),
```

and the Kretschmann scalar approaches the Schwarzschild form

```text
K(r) ~ 48 M^2 / r^6.
```

Thus the representative TIG3 sector is asymptotically GR-compatible.

---

# Preliminary Result

## Proposition: Bounded Core Curvature in the Representative TIG3 Sector

For the representative metric sector

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3),
```

with M > 0 and r_c > 0, the Kretschmann scalar remains finite at r = 0 and decays asymptotically as the Schwarzschild curvature invariant.

Therefore, the representative TIG3 sector provides a bounded-curvature admissibility candidate.

---

# Interpretation

This calculation does not prove the full TIG3 vacuum program.

It establishes a concrete first result:

```text
The minimal TIG3 representative geometry possesses a finite core curvature invariant and a Schwarzschild-compatible asymptotic limit.
```

This supports the TIG3 admissibility program by showing that the proposed minimal metric sector is not immediately ruled out by curvature divergence at the core.

---

# Current Limitations

The calculation does not yet establish:

- a covariant field equation,
- nonlinear dynamical stability,
- uniqueness,
- full Ricci-sector control,
- PDE well-posedness,
- or observational validity.

These remain future TIG3 research targets.

---

# Next Mathematical Steps

The next required steps are:

1. analyze Ricci scalar and Ricci contractions,
2. express curvature bounds in terms of beta,
3. study the near-critical regime beta ≈ beta_c,
4. compare with the TIG2 branch discriminant,
5. formulate a precise bounded-curvature admissibility proposition,
6. decide whether this result belongs in a future TIG3 paper as Lemma 1 or Proposition 1.

---

# Status

This document establishes the first explicit curvature calculation of the TIG3 vacuum-sector program.