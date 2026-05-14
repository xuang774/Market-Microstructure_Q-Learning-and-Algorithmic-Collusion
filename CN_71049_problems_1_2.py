import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# Problem 1(4)(b)

# Parameters
sigma_v = 1.0
sigma_u = 0.1
I_range = np.arange(1, 11)

# Closed-form expressions for xi = 0

# Nash equilibrium
chi_N = sigma_u / (np.sqrt(I_range) * sigma_v)
lam_N = np.sqrt(I_range) / (I_range + 1) * (sigma_v / sigma_u)
pi_N  = (1 - lam_N * I_range * chi_N) * chi_N * sigma_v**2

# Perfect cartel
chi_M = sigma_u / (I_range * sigma_v)
lam_M = np.ones_like(I_range, dtype=float) * sigma_v / (2 * sigma_u)
pi_M  = (1 - lam_M * I_range * chi_M) * chi_M * sigma_v**2

# Plots
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle(
    r'Problem 1(4)(b): Nash vs Cartel ($\xi = 0$, '
    r'$\sigma_v=1$, $\sigma_u=0.1$)', fontsize=14)

# Price impact
ax = axes[0, 0]
ax.plot(I_range, lam_N, 'bo-', label=r'$\lambda^N$ (Nash)')
ax.plot(I_range, lam_M, 'rs--', label=r'$\lambda^M$ (Cartel)')
ax.set_xlabel('I (number of speculators)')
ax.set_ylabel(r'$\lambda$')
ax.set_title(r'Price Impact $\lambda$')
ax.legend(); ax.grid(True, alpha=0.3)

# Trading intensity
ax = axes[0, 1]
ax.plot(I_range, chi_N, 'bo-', label=r'$\chi^N$ (Nash)')
ax.plot(I_range, chi_M, 'rs--', label=r'$\chi^M$ (Cartel)')
ax.set_xlabel('I (number of speculators)')
ax.set_ylabel(r'$\chi$')
ax.set_title(r'Trading Intensity $\chi$')
ax.legend(); ax.grid(True, alpha=0.3)

# Per-speculator profit
ax = axes[1, 0]
ax.plot(I_range, pi_N, 'bo-', label=r'$\pi^N$ (Nash)')
ax.plot(I_range, pi_M, 'rs--', label=r'$\pi^M$ (Cartel)')
ax.set_xlabel('I (number of speculators)')
ax.set_ylabel(r'$\pi$')
ax.set_title(r'Per-Speculator Profit $\pi$')
ax.legend(); ax.grid(True, alpha=0.3)

# Profit ratio
ax = axes[1, 1]
ratio = pi_M / pi_N
ax.plot(I_range, ratio, 'go-')
ax.set_xlabel('I (number of speculators)')
ax.set_ylabel(r'$\pi^M / \pi^N$')
ax.set_title(r'Profit Ratio $\pi^M / \pi^N$')
ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('problem1_4b.png', dpi=150, bbox_inches='tight')
plt.show()

# Print numerical table
print(f"{'I':>3} {'chi_N':>10} {'chi_M':>10} {'lam_N':>10} "
      f"{'lam_M':>10} {'pi_N':>10} {'pi_M':>10} {'pi_M/pi_N':>10}")
for i in range(len(I_range)):
    print(f"{I_range[i]:>3d} {chi_N[i]:>10.4f} {chi_M[i]:>10.4f} "
          f"{lam_N[i]:>10.4f} {lam_M[i]:>10.4f} {pi_N[i]:>10.4f} "
          f"{pi_M[i]:>10.4f} {ratio[i]:>10.4f}")


# Problem 2(1)(b)

# Parameters
sigma_v = 1.0
sigma_u = 0.1
I_range = np.arange(1, 11)

# Closed-form expressions for xi = 0

# Nash equilibrium
chi_N = sigma_u / (np.sqrt(I_range) * sigma_v)
lam_N = np.sqrt(I_range) / (I_range + 1) * (sigma_v / sigma_u)

# Perfect cartel
chi_M = sigma_u / (I_range * sigma_v)
lam_M = np.ones_like(I_range, dtype=float) * sigma_v / (2 * sigma_u)

# Market quality measures

# Price informativeness
info_N = (I_range**2 * chi_N**2 * sigma_v**2 + sigma_u**2) \
       / (sigma_v**2 * sigma_u**2)
info_M = (I_range**2 * chi_M**2 * sigma_v**2 + sigma_u**2) \
       / (sigma_v**2 * sigma_u**2)

# Market liquidity
liq_N = 1.0 / lam_N
liq_M = 1.0 / lam_M

# Noise-trader losses
W_N_nash   = lam_N * sigma_u**2
W_N_cartel = lam_M * sigma_u**2

# Plots
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle(
    r'Problem 2(1)(b): Market Quality -- Nash vs Cartel '
    r'($\xi = 0$, $\sigma_v=1$, $\sigma_u=0.1$)', fontsize=14)

# Price impact
ax = axes[0, 0]
ax.plot(I_range, lam_N, 'bo-', label=r'$\lambda^N$ (Nash)')
ax.plot(I_range, lam_M, 'rs--', label=r'$\lambda^M$ (Cartel)')
ax.set_xlabel(r'$I$'); ax.set_ylabel(r'$\lambda$')
ax.set_title(r'Price Impact $\lambda$')
ax.legend(); ax.grid(True, alpha=0.3)

# Price informativeness
ax = axes[0, 1]
ax.plot(I_range, info_N, 'bo-', label=r'$\mathcal{I}^N$ (Nash)')
ax.plot(I_range, info_M, 'rs--', label=r'$\mathcal{I}^M$ (Cartel)')
ax.set_xlabel(r'$I$'); ax.set_ylabel(r'$\mathcal{I}$')
ax.set_title(r'Price Informativeness $\mathcal{I}$')
ax.legend(); ax.grid(True, alpha=0.3)

# Noise-trader losses
ax = axes[0, 2]
ax.plot(I_range, W_N_nash, 'bo-', label=r'$W_N^N$ (Nash)')
ax.plot(I_range, W_N_cartel, 'rs--', label=r'$W_N^M$ (Cartel)')
ax.set_xlabel(r'$I$'); ax.set_ylabel(r'$W_N$')
ax.set_title(r'Noise-Trader Losses $W_N$')
ax.legend(); ax.grid(True, alpha=0.3)

# Ratios (bottom row)
ax = axes[1, 0]
ax.plot(I_range, lam_M / lam_N, 'go-')
ax.set_xlabel(r'$I$'); ax.set_ylabel(r'$\lambda^M / \lambda^N$')
ax.set_title(r'Price Impact Ratio')
ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
ax.grid(True, alpha=0.3)

ax = axes[1, 1]
ax.plot(I_range, info_M / info_N, 'go-')
ax.set_xlabel(r'$I$')
ax.set_ylabel(r'$\mathcal{I}^M / \mathcal{I}^N$')
ax.set_title(r'Informativeness Ratio')
ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
ax.grid(True, alpha=0.3)

ax = axes[1, 2]
ax.plot(I_range, W_N_cartel / W_N_nash, 'go-')
ax.set_xlabel(r'$I$'); ax.set_ylabel(r'$W_N^M / W_N^N$')
ax.set_title(r'Noise-Trader Losses Ratio')
ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('problem2_1b.png', dpi=150, bbox_inches='tight')
plt.show()

# Print numerical table
print(f"{'I':>3} {'lam_N':>8} {'lam_M':>8} {'I_N':>8} "
      f"{'I_M':>8} {'W_N_N':>8} {'W_N_M':>8}")
for i in range(len(I_range)):
    print(f"{I_range[i]:>3d} {lam_N[i]:>8.4f} {lam_M[i]:>8.4f} "
          f"{info_N[i]:>8.4f} {info_M[i]:>8.4f} "
          f"{W_N_nash[i]:>8.4f} {W_N_cartel[i]:>8.4f}")


# Problems 2(2) and 2(3)

#  SOLVER

def solve_equilibrium(I, sigma_v, sigma_u, theta, xi, mode='nash'):
    """
    Solve the fixed-point system for Nash or Cartel equilibrium.
    mode: 'nash' or 'cartel'
    Returns: (chi, lam, gamma, pi)
    """
    def residual(chi):
        gamma = I * chi / ((I * chi)**2 + (sigma_u / sigma_v)**2)
        lam = (theta * gamma + xi) / (theta + xi**2)
        if mode == 'nash':
            chi_new = 1.0 / ((I + 1) * lam)
        else:  # cartel
            chi_new = 1.0 / (2 * I * lam)
        return chi_new - chi

    chi_lo, chi_hi = 1e-12, 100.0
    for _ in range(10):
        if residual(chi_lo) * residual(chi_hi) < 0:
            break
        chi_hi *= 10

    chi_star = brentq(residual, chi_lo, chi_hi, xtol=1e-14)
    gamma_star = I * chi_star / (
        (I * chi_star)**2 + (sigma_u / sigma_v)**2)
    lam_star = (theta * gamma_star + xi) / (theta + xi**2)
    pi_star = (1 - lam_star * I * chi_star) * chi_star * sigma_v**2
    return chi_star, lam_star, gamma_star, pi_star

#  PROBLEM 2(2): Table for I=2, varying xi

sigma_v, sigma_u, theta = 1.0, 0.1, 0.1
for xi in [0, 50, 500]:
    chi_N, lam_N, _, pi_N = solve_equilibrium(
        2, sigma_v, sigma_u, theta, xi, 'nash')
    chi_M, lam_M, _, pi_M = solve_equilibrium(
        2, sigma_v, sigma_u, theta, xi, 'cartel')
    print(f"xi={xi:>3}: Nash chi={chi_N:.4f}, lam={lam_N:.4f}, "
          f"pi={pi_N:.4f} | "
          f"Cartel chi={chi_M:.4f}, lam={lam_M:.4f}, pi={pi_M:.4f}")

#  PROBLEM 2(3): Comparative statics, xi=500

xi_val, I_range = 500, np.arange(1, 11)
results = {'N': {}, 'M': {}}

for idx, I in enumerate(I_range):
    for mode, key in [('nash', 'N'), ('cartel', 'M')]:
        chi, lam, gam, pi = solve_equilibrium(
            I, sigma_v, sigma_u, theta, xi_val, mode)
        results[key].setdefault('lam', []).append(lam)
        results[key].setdefault('info', []).append(
            ((I*chi)**2 * sigma_v**2 + sigma_u**2)
            / (sigma_v**2 * sigma_u**2))
        results[key].setdefault('W_N', []).append(lam * sigma_u**2)
        results[key].setdefault('pi', []).append(pi)

# Plots (2x3 grid)
fig, axes = plt.subplots(2, 3, figsize=(16, 9))
fig.suptitle(r'Problem 2(3): Market Quality ($\xi=500$, '
             r'$\theta=0.1$)', fontsize=14)

for ax, key, label in zip(
        axes[0], ['lam', 'info', 'W_N'],
        [r'$\lambda$', r'$\mathcal{I}$', r'$W_N$']):
    ax.plot(I_range, results['N'][key], 'bo-', label='Nash')
    ax.plot(I_range, results['M'][key], 'rs--', label='Cartel')
    ax.set_xlabel(r'$I$'); ax.set_ylabel(label)
    ax.legend(); ax.grid(True, alpha=0.3)

for ax, key in zip(axes[1], ['lam', 'info', 'W_N']):
    ratio = np.array(results['M'][key]) / np.array(results['N'][key])
    ax.plot(I_range, ratio, 'go-')
    ax.axhline(y=1, color='k', linestyle=':', alpha=0.5)
    ax.set_xlabel(r'$I$'); ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('problem2_3.png', dpi=150, bbox_inches='tight')
plt.show()


# Problem 2(4)(b)

def solve_equilibrium(I, sigma_v, sigma_u, theta, xi, mode='nash'):
    def residual(chi):
        gamma = I * chi / ((I * chi)**2 + (sigma_u / sigma_v)**2)
        lam = (theta * gamma + xi) / (theta + xi**2)
        if mode == 'nash':
            chi_new = 1.0 / ((I + 1) * lam)
        else:
            chi_new = 1.0 / (2 * I * lam)
        return chi_new - chi
    chi_lo, chi_hi = 1e-12, 100.0
    for _ in range(10):
        if residual(chi_lo) * residual(chi_hi) < 0:
            break
        chi_hi *= 10
    chi_star = brentq(residual, chi_lo, chi_hi, xtol=1e-14)
    gamma_star = I * chi_star / (
        (I * chi_star)**2 + (sigma_u / sigma_v)**2)
    lam_star = (theta * gamma_star + xi) / (theta + xi**2)
    return chi_star, lam_star, gamma_star

def get_lambda(I_val, sigma_v, sigma_u, theta, xi, mode):
    _, lam, _ = solve_equilibrium(
        I_val, sigma_v, sigma_u, theta, xi, mode)
    return lam

# Parameters
sigma_v, sigma_u, theta, xi = 1.0, 0.1, 0.1, 500

for I in [2, 3, 5]:
    lam_M = get_lambda(I, sigma_v, sigma_u, theta, xi, 'cartel')

    def objective(I_star):
        return get_lambda(
            I_star, sigma_v, sigma_u, theta, xi, 'nash') - lam_M

    I_star = brentq(objective, 0.1, 1000.0, xtol=1e-10)
    print(f"I={I}: lambda^M={lam_M:.8f}, I*={I_star:.6f}")

    