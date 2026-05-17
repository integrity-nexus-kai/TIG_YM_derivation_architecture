# Near-Critical Branch Analysis

## Purpose

This document analyzes the near-critical regime of the TIG2/TIG3 branch sector.

The objective is to connect the exact TIG2 cubic branch criticality with the TIG3 bounded-curvature admissibility program.

This is the next mathematical step after the combined curvature-sector analysis.

---

# TIG2 Critical Structure

The TIG2 structural horizon equation is

```text
x^3 - x^2 + beta^3 = 0.
```

The critical point is determined by simultaneous degeneracy:

```text
P(x, beta) = 0,
dP/dx = 0.
```

This gives

```text
x_c = 2/3
```

and

```text
beta_c^3 = 4/27.
```

Equivalently,

```text
beta_c = (4/27)^(1/3).
```

---

# Discriminant

The cubic discriminant is

```text
Delta(beta) = beta^3 (4 - 27 beta^3).
```

Thus:

- Delta > 0 for subcritical admissible branch sectors,
- Delta = 0 at critical branch merger,
- Delta < 0 beyond the critical branch-transition threshold.

The near-critical regime is therefore defined by

```text
beta ≈ beta_c.
```

---

# Near-Critical Expansion

Let

```text
beta^3 = beta_c^3 - delta
```

with

```text
delta > 0
```

small.

Let

```text
x = x_c + epsilon.
```

Expanding the cubic around the critical point yields

```text
epsilon^2 + epsilon^3 - delta = 0.
```

To leading order,

```text
epsilon ~ ± sqrt(delta).
```

Thus the TIG2 branch separation obeys saddle-node square-root scaling.

---

# TIG3 Curvature Scales

From the TIG3 representative metric sector, the core curvature scales are:

```text
K(0) = 3 / (2 beta^6 M^4),
```

```text
R(0) = 3 / (beta^3 M^2),
```

and

```text
R_ab R^ab(0) = 9 / (4 beta^6 M^4).
```

These quantities remain finite for every nonzero beta.

---

# Curvature at the Critical Point

At

```text
beta = beta_c,
```

using

```text
beta_c^3 = 4/27,
```

we obtain:

```text
R(0)|_crit = 81 / (4 M^2),
```

since

```text
R(0) = 3/(beta^3 M^2).
```

For the quadratic curvature invariants:

```text
beta_c^6 = (4/27)^2 = 16/729.
```

Therefore,

```text
K(0)|_crit
=
3 / (2 beta_c^6 M^4)
=
2187 / (32 M^4),
```

and

```text
R_ab R^ab(0)|_crit
=
9 / (4 beta_c^6 M^4)
=
6561 / (64 M^4).
```

Thus all core invariants remain finite at the TIG2 critical branch point in the representative TIG3 geometry.

---

# Near-Critical Curvature Expansion

Let

```text
beta^3 = beta_c^3 - delta.
```

Then

```text
R(0)
=
3 / ((beta_c^3 - delta) M^2).
```

For small delta,

```text
R(0)
=
3/(beta_c^3 M^2)
*
1/(1 - delta/beta_c^3).
```

Expanding,

```text
R(0)
≈
R(0)|_crit
*
[1 + delta/beta_c^3 + O(delta^2)].
```

Similarly,

```text
K(0)
=
3 / (2 beta^6 M^4)
=
3 / (2 (beta_c^3 - delta)^2 M^4),
```

so

```text
K(0)
≈
K(0)|_crit
*
[1 + 2 delta/beta_c^3 + O(delta^2)].
```

Likewise,

```text
R_ab R^ab(0)
≈
[R_ab R^ab(0)]_crit
*
[1 + 2 delta/beta_c^3 + O(delta^2)].
```

Hence the representative TIG3 core curvature is amplified near criticality but remains finite at the TIG2 branch merger.

---

# Structural Interpretation

The TIG2 branch geometry becomes singular in branch structure at the critical point through saddle-node merger.

However, in the representative TIG3 metric sector, the curvature invariants do not diverge at beta = beta_c.

This produces an important structural distinction:

```text
branch criticality ≠ curvature singularity
```

within the representative TIG3 admissibility sector.

This is a central TIG3 insight.

---

# Preliminary Proposition

## Proposition — Finite Curvature at TIG2 Branch Criticality

For the representative TIG3 metric sector

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3),
```

with

```text
beta = r_c/(2M),
```

the core curvature invariants

- K(0),
- R(0),
- R_ab R^ab(0)

remain finite at the TIG2 branch-critical value

```text
beta_c^3 = 4/27.
```

Therefore the representative TIG3 geometry separates algebraic branch criticality from curvature divergence.

---

# Consequence for TIG3

This analysis supports the TIG3 admissibility program by showing that the critical TIG2 branch merger need not correspond to a curvature singularity in the representative geometry.

The near-critical regime may therefore be interpreted as a structurally sensitive but curvature-bounded sector.

This motivates further study of:

- near-critical relaxation,
- metastable core behavior,
- bounded high-curvature dynamics,
- and structural stabilization.

---

# Limitations

This result does not prove:

- full singularity exclusion,
- nonlinear stability,
- covariant field equations,
- PDE well-posedness,
- quantum-gravity completion,
- or observational predictions.

It is a curvature-sector statement for the representative TIG3 metric only.

---

# Next Mathematical Steps

The next required steps are:

1. relate near-critical curvature scaling to the discriminant Delta(beta),
2. study whether relaxation time scales diverge near beta_c,
3. define a stability operator for radial perturbations,
4. compare bounded curvature with branch loss beyond beta_c,
5. integrate this result into the theorem-candidate chain.

---

# Status

This document establishes the first near-critical curvature analysis of the TIG3 representative vacuum geometry.