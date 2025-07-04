import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as ode
from scipy.integrate import trapezoid


omega = 2 * np.pi
omega_0 = (3 * omega) / 2
beta = omega_0 / 4
gamma = np.arange(1.04, 1.17, 0.01)
gamma_eq_1 = 1.07
T = 40

f = np.array([0, 0])


def F(t, u, omega, omega_0, beta, gamma):
    return np.array(
        [
            u[1],
            -(omega_0**2) * np.sin(u[0])
            - 2 * beta * u[1]
            + gamma * omega_0**2 * np.cos(omega * t),
        ]
    )


tspan = (0, T)

SOL_1 = ode.solve_ivp(
    F,
    tspan,
    f,
    method="RK45",
    args=(omega, omega_0, beta, gamma_eq_1),
    rtol=1e-12,
    atol=1e-12,
)

trap = trapezoid(SOL_1.y[1], SOL_1.t)
print(trap)
plt.ylim(-20, 20)
# plottyx = np.linspace(0,T,len(SOL_1.t))
# plottyy = np.linspace(0,SOL_1.y[0],len(SOL_1.t))
plt.plot(SOL_1.t, SOL_1.y[0], label="$\\gamma = 1.07$")
plt.fill_between(
    SOL_1.t, SOL_1.y[0], 0, label=f"Area under grafen = {round(trap, 3)}", alpha=0.5
)
plt.ylim(-20, 20)
plt.legend()
plt.xlabel("t")
plt.grid(True)
plt.ylabel("$\\theta(t)$")
plt.show()

f = np.array([0, 0])
tspan = (0, T)
label = []
