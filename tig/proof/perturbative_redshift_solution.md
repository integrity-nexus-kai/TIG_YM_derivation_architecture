# Perturbative Redshift Solution

## Purpose

This document defines the first perturbative redshift-sector solution obtained from the TIG vacuum field-equation program.

Its purpose is to establish the first explicit correction to the restricted metric sector:

\[
A(r)=B(r).
\]

The result demonstrates that exact vacuum closure requires a nontrivial redshift structure.

---

# Generalized TIG Metric

The generalized static spherically symmetric TIG metric is:

\[
ds^2
=
-e^{2\Phi(r)}B(r)\,dt^2
+
\frac{dr^2}{B(r)}
+
r^2d\Omega^2.
\]

The horizon sector is:

\[
B(r)
=
1-\frac{2Mr^2}{r^3+r_c^3}.
\]

The canonical TIG horizon equation therefore remains:

\[
x^3-x^2+\beta^3=0.
\]

---

# Vacuum Difference Equation

The vacuum field equation:

\[
G_{\mu\nu}
+
\alpha\mathcal H_{\mu\nu}
=
0
\]

reduces at the difference level to:

\[
-\frac{2B(r)\Phi'(r)}{r}
+
\alpha
\left(
\mathcal H^t_{\ t}
-
\mathcal H^r_{\ r}
\right)
=
0.
\]

The restricted metric sector:

\[
\Phi(r)=0
\]

does not produce exact vacuum closure.

---

# Perturbative Solution

To first nontrivial order in:

\[
\alpha,
\]

the redshift equation yields:

\[
\Phi'(r)
=
-\frac{
72\alpha M r^2 r_c^3
\left(
7r^6-40r^3r_c^3+7r_c^6
\right)
}{
(r^3+r_c^3)^5
}.
\]

Integration gives:

\[
\Phi(r)
=
\frac{
12\alpha M r_c^3
\left(
7r^6-22r^3r_c^3-2r_c^6
\right)
}{
(r^3+r_c^3)^4
}
+
C.
\]

Asymptotic Schwarzschild normalization requires:

\[
\Phi(r)\rightarrow0
\quad
\text{for}
\quad
r\rightarrow\infty,
\]

therefore:

\[
C=0.
\]

---

# Corrected TIG Metric

The perturbatively corrected TIG vacuum metric is therefore:

\[
ds^2
=
-e^{2\Phi(r)}B(r)\,dt^2
+
\frac{dr^2}{B(r)}
+
r^2d\Omega^2,
\]

with:

\[
B(r)
=
1-\frac{2Mr^2}{r^3+r_c^3},
\]

and:

\[
\Phi(r)
=
\frac{
12\alpha M r_c^3
\left(
7r^6-22r^3r_c^3-2r_c^6
\right)
}{
(r^3+r_c^3)^4
}.
\]

---

# Interpretation

The perturbative solution establishes:

- the necessity of a nontrivial redshift sector,
- compatibility of the cubic TIG horizon structure with vacuum correction,
- and first-order perturbative vacuum closure.

The result demonstrates that the TIG horizon structure survives beyond the restricted metric sector.

---

# Current Limitation

This result is perturbative only.

The following remain unresolved:

- full nonlinear tensor closure,
- exact global vacuum solution,
- higher-order consistency,
- and exact componentwise residual cancellation.

---

# Current Status

The TIG vacuum program now possesses:

- a generalized metric sector,
- a reduced vacuum proof equation,
- and a first explicit perturbative redshift correction.

The exact nonlinear vacuum proof remains open.

---

# Status

perturbative vacuum correction established
