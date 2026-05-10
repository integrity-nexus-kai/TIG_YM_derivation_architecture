#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TIG Tensor Residual SymPy Script

Purpose
-------
Compute the tensor objects required for the TIG vacuum-proof program
for the generalized static spherically symmetric metric

    ds^2 = -exp(2 Phi(r)) B(r) dt^2 + dr^2/B(r) + r^2 dOmega^2

with

    B(r) = 1 - 2 M r^2 / (r^3 + rc^3)

The script computes:
- Christoffel symbols
- Ricci tensor
- Ricci scalar
- Einstein tensor
- R^2 correction tensor H_{mu nu}
- vacuum residual E_{mu nu} = G_{mu nu} + alpha H_{mu nu}
- mixed residual components E^mu_mu
- difference equation E^t_t - E^r_r

This is a calculation tool, not a proof by itself.
The proof requires simplification/solving of the generated equations.
"""

import sympy as sp

# ---------------------------------------------------------------------------
# Coordinates and symbols
# ---------------------------------------------------------------------------

t, r, th, ph = sp.symbols("t r theta phi", real=True)
M, rc, alpha = sp.symbols("M rc alpha", positive=True, finite=True, nonzero=True)

coords = [t, r, th, ph]
dim = 4

Phi = sp.Function("Phi")(r)

B = 1 - (2 * M * r**2) / (r**3 + rc**3)

# Metric signature: (-,+,+,+)
g = sp.diag(
    -sp.exp(2 * Phi) * B,
    1 / B,
    r**2,
    r**2 * sp.sin(th)**2,
)

g_inv = sp.simplify(g.inv())

# ---------------------------------------------------------------------------
# Helper functions
# ---------------------------------------------------------------------------

def clean(expr):
    """Moderate simplification helper."""
    return sp.factor(sp.together(sp.simplify(expr)))

def d(expr, idx):
    return sp.diff(expr, coords[idx])

# ---------------------------------------------------------------------------
# Christoffel symbols Gamma^rho_{mu nu}
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
            Gamma[rho][mu][nu] = clean(sp.Rational(1, 2) * s)

# ---------------------------------------------------------------------------
# Ricci tensor R_{mu nu}
# R_{mu nu} = d_l Gamma^l_{mu nu} - d_nu Gamma^l_{mu l}
#             + Gamma^l_{mu nu} Gamma^s_{l s}
#             - Gamma^s_{mu l} Gamma^l_{nu s}
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
        Ricci[mu, nu] = clean(term)

# ---------------------------------------------------------------------------
# Ricci scalar R and Einstein tensor G_{mu nu}
# ---------------------------------------------------------------------------

Rscalar = clean(sum(g_inv[mu, nu] * Ricci[mu, nu] for mu in range(dim) for nu in range(dim)))

Einstein = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        Einstein[mu, nu] = clean(Ricci[mu, nu] - sp.Rational(1, 2) * g[mu, nu] * Rscalar)

# ---------------------------------------------------------------------------
# Covariant second derivative of scalar R:
# nabla_mu nabla_nu R = partial_mu partial_nu R - Gamma^lambda_{mu nu} partial_lambda R
# ---------------------------------------------------------------------------

nabla2_R = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)

for mu in range(dim):
    for nu in range(dim):
        term = sp.diff(sp.diff(Rscalar, coords[nu]), coords[mu])
        for lam in range(dim):
            term -= Gamma[lam][mu][nu] * sp.diff(Rscalar, coords[lam])
        nabla2_R[mu, nu] = clean(term)

Box_R = clean(sum(g_inv[mu, nu] * nabla2_R[mu, nu] for mu in range(dim) for nu in range(dim)))

# ---------------------------------------------------------------------------
# R^2 correction tensor:
# H_{mu nu} = 2 R R_{mu nu} - 1/2 g_{mu nu} R^2
#             - 2 nabla_mu nabla_nu R + 2 g_{mu nu} Box R
# ---------------------------------------------------------------------------

H = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)

for mu in range(dim):
    for nu in range(dim):
        H[mu, nu] = clean(
            2 * Rscalar * Ricci[mu, nu]
            - sp.Rational(1, 2) * g[mu, nu] * Rscalar**2
            - 2 * nabla2_R[mu, nu]
            + 2 * g[mu, nu] * Box_R
        )

# ---------------------------------------------------------------------------
# Vacuum residual E_{mu nu} = G_{mu nu} + alpha H_{mu nu}
# Mixed residual E^mu_nu = g^{mu rho} E_{rho nu}
# ---------------------------------------------------------------------------

E = sp.MutableDenseMatrix(dim, dim, [0] * dim * dim)
for mu in range(dim):
    for nu in range(dim):
        E[mu, nu] = clean(Einstein[mu, nu] + alpha * H[mu, nu])

E_mixed = clean(g_inv * E)

difference_Et_Er = clean(E_mixed[0, 0] - E_mixed[1, 1])
difference_Gt_Gr = clean((g_inv * Einstein)[0, 0] - (g_inv * Einstein)[1, 1])
difference_Ht_Hr = clean((g_inv * H)[0, 0] - (g_inv * H)[1, 1])

# ---------------------------------------------------------------------------
# Restricted sector Phi = 0 diagnostic
# ---------------------------------------------------------------------------

subs_phi_zero = {
    Phi: 0,
    sp.diff(Phi, r): 0,
    sp.diff(Phi, r, 2): 0,
    sp.diff(Phi, r, 3): 0,
    sp.diff(Phi, r, 4): 0,
    sp.diff(Phi, r, 5): 0,
}

restricted_G_diff = clean(difference_Gt_Gr.subs(subs_phi_zero))
restricted_H_diff = clean(difference_Ht_Hr.subs(subs_phi_zero))
restricted_E_diff = clean(difference_Et_Er.subs(subs_phi_zero))

# ---------------------------------------------------------------------------
# First-order perturbative Phi'(r)
# From: Gdiff + alpha Hdiff = 0
# Linear order around Phi=0:
#   -2 B Phi'/r + alpha Hdiff|_{Phi=0} = 0
# ---------------------------------------------------------------------------

Phi_prime_first_order = clean(alpha * r * restricted_H_diff / (2 * B))

# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("\n=== TIG Tensor Residual SymPy Script ===\n")

    print("B(r) =")
    print(B)

    print("\nRicci scalar R =")
    print(Rscalar)

    print("\nMixed Einstein components:")
    print("G^t_t =")
    print(clean((g_inv * Einstein)[0, 0]))
    print("\nG^r_r =")
    print(clean((g_inv * Einstein)[1, 1]))
    print("\nG^theta_theta =")
    print(clean((g_inv * Einstein)[2, 2]))

    print("\nGeneral difference G^t_t - G^r_r =")
    print(difference_Gt_Gr)

    print("\nGeneral difference H^t_t - H^r_r =")
    print(difference_Ht_Hr)

    print("\nRestricted Phi=0 diagnostics:")
    print("Gdiff|Phi=0 =")
    print(restricted_G_diff)
    print("\nHdiff|Phi=0 =")
    print(restricted_H_diff)
    print("\nEdiff|Phi=0 =")
    print(restricted_E_diff)

    print("\nFirst-order perturbative Phi'(r) from Ediff=0:")
    print(Phi_prime_first_order)

    print("\nResidual mixed diagonal components:")
    print("E^t_t =")
    print(E_mixed[0, 0])
    print("\nE^r_r =")
    print(E_mixed[1, 1])
    print("\nE^theta_theta =")
    print(E_mixed[2, 2])
    print("\nE^phi_phi =")
    print(E_mixed[3, 3])

    print("\nDone.")
