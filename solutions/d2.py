from scipy.integrate import trapezoid, simpson
import numpy as np


def theta(gamma, omega, omega_0, t):
    first_part = (gamma * omega_0**2) / (omega_0**2 - omega**2)
    second_part = omega_0 * np.sin(omega_0 * t) - omega * np.sin(omega * t)
    return first_part * second_part


def speed(t):
    return abs(theta(gamma, omega, omega_0, t))


omega = 2 * np.pi
omega_0 = 3 * np.pi
gamma = 0.1
T = 0.25
N = np.array([100, 200, 400, 800])
K = [T / n for n in N]

TRAP = []
TRAP_ERRORS = []
TRAP_CONVERGENCE = []

SIMPSON = []
SIMPSON_ERRORS = []
SIMPSON_CONVERGENCE = []

# Integraler
for i in range(len(N)):
    t = np.linspace(0, T, N[i])
    y = speed(t)
    trap_result = trapezoid(y, dx=K[i])
    simpson_result = simpson(y, dx=K[i])
    TRAP.append(trap_result)
    SIMPSON.append(simpson_result)

# Richardson-extrapolation
for i in range(len(N) - 1):
    error_trap = (TRAP[i + 1] - TRAP[i]) / 3
    TRAP_ERRORS.append(error_trap)
    error_simpson = (SIMPSON[i + 1] - SIMPSON[i]) / 15
    SIMPSON_ERRORS.append(error_trap)


# Konvergens
for i in range(len(N) - 2):
    ratio_trap = TRAP_ERRORS[i] / TRAP_ERRORS[i + 1]
    q_trap = np.log2(abs(ratio_trap))
    TRAP_CONVERGENCE.append(q_trap)

    ratio_simpson = SIMPSON_ERRORS[i + 1] / SIMPSON_ERRORS[i]
    q_simpson = np.log2(abs(ratio_simpson))
    SIMPSON_CONVERGENCE.append(q_simpson)

print(f"""
{TRAP}
{TRAP_ERRORS}
{TRAP_CONVERGENCE}
------------------------------------
{SIMPSON}
{SIMPSON_ERRORS}
{SIMPSON_CONVERGENCE}""")
