import numpy as np
from scipy.integrate import trapezoid

# T = 0.25
T = 10
omega = 2 * np.pi
omega_0 = 3 * np.pi
gamma = 0.1
r = 1


# Ekvation (4)
def theta_dot(gamma, omega_0, omega, t):
    return ((gamma * omega_0**2) / (omega_0**2 - omega**2)) * (
        omega_0 * np.sin(omega_0 * t) - omega * np.sin(omega * t)
    )


# Ekvation theta_dot = |v(t)| * r
def v(t, gamma, omega_0, omega, r):
    return np.abs((r * theta_dot(gamma, omega_0, omega, t)))


def trap(N, T=T, omega=omega, omega_0=omega_0, gamma=gamma, r=r):
    t = np.linspace(0, T, N + 1)
    f = v(t, gamma, omega_0, omega, r)
    return trapezoid(f, t)


def simpson(N, T=T, omega=omega, omega_0=omega_0, gamma=gamma, r=r):
    t = np.linspace(0, T, N + 1)
    f = v(t, gamma, omega_0, omega, r)
    k = T / N
    return (k / 3) * (f[0] + f[-1] + 4 * np.sum(f[1:-1:2]) + 2 * np.sum(f[2:-2:2]))


# Beräkna konvergensen
def q(errors):
    q_N = np.zeros(len(errors))
    for i in range(1, len(errors)):
        q_N[i] = np.log2(errors[i - 1] / errors[i])
    return q_N


# Huvudkörning
N_värden = np.array([50, 100, 200, 400, 800])

trap_värden = np.zeros(len(N_värden))
trap_2_värden = np.zeros(len(N_värden))

simp_värden = np.zeros(len(N_värden))
simp_2_värden = np.zeros(len(N_värden))

fel_3 = np.zeros(len(N_värden))  # Trapetsfel
fel_5 = np.zeros(len(N_värden))  # Simpsons fel

for i, N in enumerate(N_värden):
    trap_värden[i] = trap(N, T, omega, omega_0, gamma)

    simp_värden[i] = simpson(N, T, omega, omega_0, gamma, r)

    fel_3[i] = np.abs(trap_värden[i] - trap_värden[i - 1]) / 3  # Tredjedelsregeln
    fel_5[i] = (
        np.abs(simp_värden[i] - simp_värden[i - 1]) / 15
    )  # Simpsons fel (med exakt samma idé)

q_värden_3 = q(fel_3)
q_värden_5 = q(fel_5)

print(" N  |  S_T(N)  |  e_3(N)      |  q_3(N)  |  S_S(N)   | e_5(N)     | q_5(N)")
print(
    "----------------------------------------------------------------------------------------------"
)
for i in range(len(N_värden)):
    print(
        f"{N_värden[i]:<3} |  {trap_värden[i]:.3f}   |  {fel_3[i]:.3e}   |  {q_värden_3[i]:.3f}   |  {simp_värden[i]:.3f}   | {fel_5[i]:.3e}   | {q_värden_5[i]:.3f}"
    )
