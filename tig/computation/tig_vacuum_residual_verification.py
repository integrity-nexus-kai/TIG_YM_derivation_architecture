#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIG Vacuum Residual Verification Script

Purpose
-------
This script performs the next executable proof step for the TIG vacuum program.

It checks the generalized perturbative TIG metric

    ds^2 = -exp(2 Phi(r)) B(r) dt^2 + dr^2/B(r) + r^2 dOmega^2

with

    B(r) = 1 - 2 M r^2/(r^3 + rc^3)

and first-order redshift correction

    Phi(r) = alpha * Phi1(r)

where

    Phi1(r) =
        12 M rc^3 (7 r^6 - 22 r^3 rc^3 - 2 rc^6)/(r^3 + rc^3)^4.

Goal
----
Compute the mixed residual components

    E^mu_nu = G^mu_nu + alpha H^mu_nu

for the R + alpha R^2 vacuum field equation, expanded through O(alpha),
and test whether the perturbative metric closes the vacuum equations
to first order.

Important
---------
This script is not a full nonlinear proof.
It tests first-order perturbative vacuum closure.

Expected scientific output:
- If all O(alpha) residual components vanish, first-order perturbative
  vacuum closure is supported.
- If some O(alpha) residual components remain nonzero, the proposed
  Phi1 solves only a reduced/difference equation and not the complete
  componentwise first-order vacuum system.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Coordinates and symbols
# ---------------------------------------------------------------------------

t, r, th, ph = sp.symbols("t r theta phi", real=True)
M, rc, alpha = sp.symbols("M rc alpha", positive=True, finite=True, nonzero=True)

coords = [t, r, th, ph]
dim = 4

D = r**3 + rc**3

B = 1 - (2 * M * r**2) / D

Phi1 = (
    12 * M * rc**3 * (7 * r**6 - 22 * r**3 * rc**3 - 2 * rc**6)
    / D**4
)

Phi = alpha * Phi1

# Metric signature: (-,+,+,+)
# For first-order checking, keep exp(2 alpha Phi1) symbolically first,
# then series-expand the final residuals through O(alpha).
g = sp.diag(
    -sp.exp(2 * Phi) * B,
    1 / B,
    r**2,
    r**2 * sp.sin(th)**2,
)

g_inv = sp.simplify(g.inv())

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def clean(expr):
    return sp.factor(sp.together(sp.simplify(expr)))

def series_alpha(expr, order=2):
    """
    Expand in alpha around 0 and truncate.
    order=2 keeps terms through alpha^1.
    """
    return clean(sp.series(expr, alpha, 0, order).removeO())

def coeff_alpha(expr, n):
    return clean(sp.expand(expr).coeff(alpha, n))

def d(expr, idx):
    return sp.diff(expr, coords[idx])

# ---------------------------------------------------------------------------
# Christoffel symbols
# ---------------------------------------------------------------------------

Gamma = [[[
    sp.Integer(0) for _ in range(dim)
] for _ in range(dim)] for _ in range(dim)]

for rho in range(dim):
    for mu in range(dim):
        for nu in range(dim):
            s = sp.Integer(0)
            for sig in range(dim):
                s += g_inv[rho, sig] * (
                    d(g[sig, nu], mu)
                    + d(g[sig, mu], nu)
                    - d(g[mu, nu], sig)
                )
            Gamma[rho][mu][nu] = series_alpha(sp.Rational(1, 2) * s, 2)

# ---------------------------------------------------------------------------
# Ricci tensor
# ---------------------------------------------------------------------------

Ricci = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)

for mu in range(dim):
    for nu in range(dim):
        term = sp.Integer(0)
        for lam in range(dim):
            term += d(Gamma[lam][mu][nu], lam)
            term -= d(Gamma[lam][mu][lam], nu)
            for sig in range(dim):
                term += Gamma[lam][mu][nu] * Gamma[sig][lam][sig]
                term -= Gamma[sig][mu][lam] * Gamma[lam][nu][sig]
        Ricci[mu, nu] = series_alpha(term, 2)

# ---------------------------------------------------------------------------
# Ricci scalar and Einstein tensor
# ---------------------------------------------------------------------------

Rscalar = series_alpha(
    sum(g_inv[mu, nu] * Ricci[mu, nu] for mu in range(dim) for nu in range(dim)),
    2,
)

Einstein = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        Einstein[mu, nu] = series_alpha(
            Ricci[mu, nu] - sp.Rational(1, 2) * g[mu, nu] * Rscalar,
            2,
        )

# ---------------------------------------------------------------------------
# H tensor must be evaluated to zeroth order only for first-order residual:
# E = G(alpha) + alpha H(alpha)
# through O(alpha):
# E^(0) + alpha [G^(1) + H^(0)]
# Therefore compute H from alpha=0 geometry.
# ---------------------------------------------------------------------------

subs_alpha0 = {alpha: 0}

g0 = sp.simplify(g.subs(subs_alpha0))
g0_inv = sp.simplify(g_inv.subs(subs_alpha0))
Gamma0 = [[[
    clean(Gamma[rho][mu][nu].subs(subs_alpha0)) for nu in range(dim)
] for mu in range(dim)] for rho in range(dim)]
Ricci0 = sp.MutableDenseMatrix(dim, dim, [clean(Ricci[i, j].subs(subs_alpha0)) for i in range(dim) for j in range(dim)])
R0 = clean(Rscalar.subs(subs_alpha0))

nabla2_R0 = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        term = sp.diff(sp.diff(R0, coords[nu]), coords[mu])
        for lam in range(dim):
            term -= Gamma0[lam][mu][nu] * sp.diff(R0, coords[lam])
        nabla2_R0[mu, nu] = clean(term)

Box_R0 = clean(sum(g0_inv[mu, nu] * nabla2_R0[mu, nu] for mu in range(dim) for nu in range(dim)))

H0 = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        H0[mu, nu] = clean(
            2 * R0 * Ricci0[mu, nu]
            - sp.Rational(1, 2) * g0[mu, nu] * R0**2
            - 2 * nabla2_R0[mu, nu]
            + 2 * g0[mu, nu] * Box_R0
        )

# ---------------------------------------------------------------------------
# First-order residual
# E = G(alpha) + alpha H0 + O(alpha^2)
# Mixed E^mu_nu = g^{-1} E through first order
# ---------------------------------------------------------------------------

E_cov_first = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        E_cov_first[mu, nu] = series_alpha(Einstein[mu, nu] + alpha * H0[mu, nu], 2)

E_mixed_first = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
mixed_raw = g_inv * E_cov_first
for mu in range(dim):
    for nu in range(dim):
        E_mixed_first[mu, nu] = series_alpha(mixed_raw[mu, nu], 2)

diag_labels = ["t", "r", "theta", "phi"]
diag_components = [E_mixed_first[i, i] for i in range(dim)]

# ---------------------------------------------------------------------------
# Extract zeroth and first order coefficients
# ---------------------------------------------------------------------------

E0_diag = [coeff_alpha(comp, 0) for comp in diag_components]
E1_diag = [coeff_alpha(comp, 1) for comp in diag_components]

# Difference equation check
diff_tr = series_alpha(E_mixed_first[0, 0] - E_mixed_first[1, 1], 2)
diff_tr_0 = coeff_alpha(diff_tr, 0)
diff_tr_1 = coeff_alpha(diff_tr, 1)

# Verify Phi derivative
Phi1_prime_expected = (
    -72 * M * r**2 * rc**3 * (7 * r**6 - 40 * r**3 * rc**3 + 7 * rc**6)
    / D**5
)
phi_derivative_check = clean(sp.diff(Phi1, r) - Phi1_prime_expected)

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n=== TIG Vacuum Residual Verification: First Order in alpha ===\n")

    print("B(r) =")
    print(B)

    print("\nPhi1(r) =")
    print(Phi1)

    print("\nDerivative check d(Phi1)/dr - expected =")
    print(phi_derivative_check)

    print("\nRicci scalar R through O(alpha):")
    print(Rscalar)

    print("\nMixed residual diagonal components E^mu_mu through O(alpha):")
    for label, comp in zip(diag_labels, diag_components):
        print(f"\nE^{label}_{label} =")
        print(comp)

    print("\nZeroth-order residual coefficients:")
    for label, comp in zip(diag_labels, E0_diag):
        print(f"E0^{label}_{label} = {comp}")

    print("\nFirst-order residual coefficients:")
    for label, comp in zip(diag_labels, E1_diag):
        print(f"E1^{label}_{label} =")
        print(comp)

    print("\nDifference E^t_t - E^r_r through O(alpha):")
    print(diff_tr)

    print("\nDifference coefficients:")
    print("diff_tr O(alpha^0) =")
    print(diff_tr_0)
    print("\ndiff_tr O(alpha^1) =")
    print(diff_tr_1)

    all_first_order_zero = all(clean(c) == 0 for c in E1_diag)
    diff_first_order_zero = clean(diff_tr_1) == 0

    print("\n=== Verification Summary ===")
    print(f"Phi derivative verified: {phi_derivative_check == 0}")
    print(f"Difference equation closed to O(alpha): {diff_first_order_zero}")
    print(f"All diagonal residual components vanish to O(alpha): {all_first_order_zero}")

    if all_first_order_zero:
        print("\nRESULT: first-order perturbative vacuum closure supported.")
    else:
        print("\nRESULT: full first-order componentwise vacuum closure is NOT established by Phi1 alone.")
        print("Interpretation: Phi1 may close the difference equation but additional conditions/source/corrections may be required.")

    print("\nDone.")
