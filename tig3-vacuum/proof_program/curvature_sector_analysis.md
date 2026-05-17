# Curvature Sector Analysis

## Purpose

This document combines the first explicit curvature-control calculations of the TIG3 admissibility program.

The objective is to investigate whether the representative TIG3 minimal metric sector admits bounded curvature behavior in the regulated core region while preserving asymptotic GR compatibility.

The analysis focuses on:

- the Kretschmann scalar,
- the Ricci scalar,
- and the Ricci contraction.

This does not yet constitute a full vacuum proof.

It establishes a preliminary bounded-curvature admissibility result for the representative TIG3 geometry.

---

# Representative TIG3 Metric Sector

We consider the static spherically symmetric metric

```text
ds^2 = -F(r) dt^2 + dr^2 / F(r) + r^2 dOmega^2
```

with representative lapse function

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3).
```

Here:

- M denotes the asymptotic mass scale,
- r_c denotes the structural core scale,
- beta = r_c/(2M) is the TIG structural control parameter.

This metric sector is representative and not claimed to be unique.

---

# Kretschmann Sector

For metrics of the form

```text
ds^2 = -F(r) dt^2 + dr^2/F(r) + r^2 dOmega^2,
```

the Kretschmann scalar may be written as

```text
K(r)
=
[F''(r)]^2
+
4 [F'(r)/r]^2
+
4 [(1 - F(r))/r^2]^2.
```

For the TIG3 lapse function,

```text
F'(r)
=
2 M r (r^3 - 2 r_c^3)/(r^3 + r_c^3)^2,
```

and

```text
F''(r)
=
-4 M (r_c^6 - 7 r_c^3 r^3 + r^6)/(r^3 + r_c^3)^3.
```

Substitution yields

```text
K(r)
=
48 M^2
(2 r_c^12 - 2 r_c^9 r^3 + 18 r_c^6 r^6 - 4 r_c^3 r^9 + r^12)
/
(r^3 + r_c^3)^6.
```

---

# Core Limit of Kretschmann Scalar

At

```text
r -> 0,
```

one obtains

```text
K(0)
=
96 M^2 / r_c^6
=
3 / (2 beta^6 M^4).
```

Thus the Kretschmann scalar remains finite provided

```text
r_c > 0.
```

Therefore beta acts as a curvature regulator within the representative TIG3 sector.

---

# Asymptotic Kretschmann Behavior

For

```text
r -> infinity,
```

the lapse function behaves as

```text
F(r)
=
1 - 2M/r + O(r^-4),
```

and

```text
K(r)
~
48 M^2 / r^6.
```

Thus the asymptotic curvature sector recovers Schwarzschild-compatible GR behavior.

---

# Ricci Scalar Sector

For the same metric class, the Ricci scalar is

```text
R(r)
=
-F''(r)
- 4 F'(r)/r
+ 2(1 - F(r))/r^2.
```

For the TIG3 lapse function,

```text
R(r)
=
12 M r_c^3 (2 r_c^3 - r^3)
/
(r^3 + r_c^3)^3.
```

---

# Core Limit of Ricci Scalar

At

```text
r -> 0,
```

one obtains

```text
R(0)
=
24 M / r_c^3
=
3 / (beta^3 M^2).
```

Hence the Ricci scalar remains finite for

```text
r_c > 0.
```

---

# Asymptotic Ricci Scalar Behavior

For

```text
r -> infinity,
```

the Ricci scalar satisfies

```text
R(r)
~
-12 M r_c^3 / r^6,
```

and therefore

```text
R(r) -> 0.
```

This is asymptotically compatible with Schwarzschild vacuum geometry.

---

# Ricci Contraction

Define

```text
A(r)
=
-[F''(r)/2 + F'(r)/r],
```

and

```text
B(r)
=
[1 - F(r) - rF'(r)]/r^2.
```

Then

```text
R_ab R^ab
=
2 A(r)^2 + 2 B(r)^2.
```

For the TIG3 lapse function,

```text
R_ab R^ab
=
72 M^2 r_c^6
(2 r_c^6 - 2 r_c^3 r^3 + 5 r^6)
/
(r^3 + r_c^3)^6.
```

---

# Core Limit of Ricci Contraction

At

```text
r -> 0,
```

one obtains

```text
R_ab R^ab(0)
=
144 M^2 / r_c^6
=
9 / (4 beta^6 M^4).
```

Thus the Ricci contraction also remains finite in the regulated core sector.

---

# Asymptotic Ricci Contraction Behavior

For

```text
r -> infinity,
```

the Ricci contraction behaves as

```text
R_ab R^ab
~
360 M^2 r_c^6 / r^12,
```

and therefore

```text
R_ab R^ab -> 0.
```

The representative TIG3 sector therefore becomes asymptotically Ricci-flat.

---

# Combined Preliminary Result

## Proposition — Preliminary Bounded Curvature Sector

For the representative TIG3 metric sector

```text
F(r)
=
1 - (2 M r^2)/(r^3 + r_c^3),
```

with

```text
M > 0,
r_c > 0,
```

the following curvature quantities remain finite at the regulated core:

- Kretschmann scalar,
- Ricci scalar,
- Ricci contraction.

Furthermore, all three invariants recover asymptotic Schwarzschild-compatible behavior at large radius.

Therefore the representative TIG3 geometry defines a preliminary bounded-curvature admissibility candidate.

---

# Interpretation

The analysis establishes the first explicit bounded-curvature result of the TIG3 vacuum program.

The representative metric sector is not immediately ruled out by curvature divergence at the regulated core.

This supports the central TIG3 admissibility hypothesis:

```text
Admissible branch geometry may permit regulated high-curvature continuation without immediate invariant divergence.
```

This statement remains restricted to the representative metric sector.

No complete covariant TIG3 field equation has yet been established.

---

# Current Limitations

This analysis does not yet provide:

- a covariant field equation,
- nonlinear stability analysis,
- PDE control,
- uniqueness,
- energy-condition analysis,
- or observational validation.

The present result is a geometric admissibility calculation only.

---

# Next Mathematical Steps

The next mathematical tasks are:

1. analyze the near-critical regime beta ≈ beta_c,
2. derive curvature scaling laws,
3. compare curvature behavior with TIG2 discriminant structure,
4. study effective core geometry,
5. formulate rigorous admissibility lemmas,
6. integrate the curvature sector into the TIG3 theorem chain.

---

# Status

This document establishes the first combined curvature-sector analysis of the representative TIG3 vacuum geometry.