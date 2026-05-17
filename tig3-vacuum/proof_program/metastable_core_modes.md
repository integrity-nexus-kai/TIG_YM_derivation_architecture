# Metastable Core Modes

## Purpose

This document defines the preliminary concept of metastable core modes within the TIG3 admissibility framework.

The objective is to translate the heuristic TIG3 observation of bounded core relaxation into a controlled mathematical language connected to:

- bounded curvature,
- radial perturbation theory,
- near-critical branch dynamics,
- and spectral stability.

This document does not prove the existence of metastable modes.

It defines the structural framework in which such modes may be studied.

---

# Starting Point

The TIG3 bounded-curvature analysis established that the representative metric sector

```text
F(r) = 1 - (2 M r^2)/(r^3 + r_c^3)
```

admits finite curvature invariants at the regulated core for

```text
r_c > 0.
```

The radial stability-operator framework then introduces an effective perturbation equation of the form

```text
partial_t^2 psi - partial_r_*^2 psi + V_eff(r) psi = 0.
```

Metastable core modes are candidate bounded solutions of this perturbative framework.

---

# Preliminary Definition

A metastable TIG3 core mode is a perturbative configuration

```text
psi(t,r)
```

localized near the regulated core region and satisfying:

1. finite perturbative energy,
2. bounded amplitude for finite time intervals,
3. admissible behavior at the regulated core,
4. asymptotic decay away from the core,
5. compatibility with the TIG2 branch sector.

Such a mode is called metastable if it persists over long but finite relaxation times.

---

# Operator Interpretation

Let the radial stability operator be

```text
L_TIG = - d^2/dr_*^2 + V_eff(r).
```

A metastable mode may be represented schematically by a resonance-like solution

```text
psi(t,r) ~ exp(-gamma t) cos(omega t) phi(r),
```

where:

- omega is the oscillation frequency,
- gamma is the damping rate,
- phi(r) is a localized radial profile.

Metastability corresponds to the regime

```text
0 < gamma << omega.
```

This expresses long-lived bounded relaxation without permanent instability.

---

# Near-Critical Enhancement

The near-critical branch regime

```text
beta approx beta_c
```

may enhance metastability through:

- flattening of the effective potential,
- increased branch sensitivity,
- delayed relaxation,
- and longer-lived localized modes.

This provides a mathematical interpretation of TIG3 core breathing as near-critical bounded relaxation.

---

# Relation to Bounded Curvature

Metastable modes require a bounded background sector.

If curvature invariants diverged at the core, perturbative control would generally fail.

The bounded-curvature result therefore supplies the geometric precondition for defining controlled core modes.

Thus the logical chain is:

```text
bounded curvature
-> radial stability operator
-> localized perturbation modes
-> metastable relaxation behavior
```

---

# Admissibility Conditions

Candidate admissibility conditions for metastable modes include:

1. finite energy norm,
2. bounded radial profile,
3. regularity at the core,
4. decay at large radius,
5. compatibility with the structural control parameter beta,
6. absence of exponentially growing modes.

A possible energy functional is

```text
E[psi]
=
1/2 integral
(
|partial_t psi|^2
+
|partial_r_* psi|^2
+
V_eff(r)|psi|^2
)
dr_*.
```

Admissible metastable modes should satisfy

```text
E[psi] < infinity.
```

---

# Structural Interpretation

Metastable core modes are the mathematical formulation of bounded TIG3 core relaxation.

They should not be interpreted as proof that black holes physically oscillate in the full theory.

Rather, they define a possible perturbative sector in which the representative TIG3 geometry supports long-lived localized relaxation behavior.

---

# Preliminary Proposition Target

## Proposition - Metastable Core Mode Candidate

If the representative TIG3 metric sector admits a self-adjoint radial stability operator with a localized resonance-like spectral sector and finite perturbative energy, then bounded long-lived core relaxation modes may exist.

This is a theorem target and not yet established.

---

# Limitations

This document does not provide:

- explicit V_eff(r),
- spectral theorem,
- nonlinear stability proof,
- decay estimates,
- resonance construction,
- or observational predictions.

The mode structure remains conjectural.

---

# Next Mathematical Steps

The next required steps are:

1. derive or choose an explicit effective potential V_eff(r),
2. define the admissible Hilbert space,
3. impose core and asymptotic boundary conditions,
4. study possible resonance poles,
5. analyze near-critical dependence of gamma and omega,
6. compare with simulation-observed relaxation behavior.

---

# Status

This document defines the preliminary metastable-mode framework of the TIG3 admissibility program.