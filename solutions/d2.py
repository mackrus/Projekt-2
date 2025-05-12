import os

import numpy as np
from scipy.integrate import quad, trapezoid

PLOTDIR = "../plots/"
if not os.path.exists(PLOTDIR):
    os.makedirs(PLOTDIR)

"""
INTRUKTIONER

Skriv ett program i Python som löser (5) med trapetsformeln, genom att anropa funktionen trapezoid. 
Sätt 𝜔 = 2 𝜋, 𝜔0 = 3 𝜋, 𝛾 = 0.1. Sätt begynnelsevillkoren till 𝜃 = 𝜃′ = 0. 
Sluttiden sätts till 𝑇 = 10. Låt 𝑁 beteckna antalet steg (intervall). 
Tidssteget (𝑘) ges då enligt 𝑘 = 𝑁𝑇 . 
Beräkna (5) med trapetsformen med 𝑁 = 100, 200, 400, 800 intervall 
och redovisa resultaten i en tabell (se Tabell 1, för tydligt redovisad tabell-mall). 
Låt 𝑆𝑇 (𝑁) beteckna trapetsformeln med 𝑁 intervall. 
Använd nu 3e-dels regeln för att uppskatta felen (som vi betecknar med 𝑒𝑁 ) hos 𝑆𝑇 (200), 𝑆𝑇 (400) och 𝑆𝑇 (800). 
Redovisa de uppskattade felen, dvs 𝑒200, 𝑒400 och 𝑒800 i samma tabell. 
Redovisa därefter den uppskattade konvergensen med hjälp av (6). 
Man bör här se 2a ordningens konvergens (om funktionen är tillräckligt snäll), dvs att felet skalar som ≃ 𝑁−2. Om man mäter felen med 𝑁 och 2𝑁 steg kan man uppskatta metodens noggrannhets-ordningen (konvergensen), som vi betecknar med 𝑞(2𝑁), med följande formel:

 """
# KONSTANTER
omega = 2 * np.pi
omega_0 = 3 * np.pi
gamma = 0.1
N = 200
T = 10

N_SERIES = [100, 200, 400, 800]


def theta_prime(gamma, omega, omega_0, t):
    first_part = (gamma * omega_0**2) / (omega_0**2 - omega**2)
    second_part = omega_0 * np.sin(omega_0 * t) - omega * np.sin(omega * t)
    return first_part * second_part


def speed(t):
    return abs(theta_prime(gamma, omega, omega_0, t))


# Compute reference solution using quad
S_ref, _ = quad(speed, 0, T, epsabs=1.49e-12, epsrel=1.49e-12, limit=500)

# Compute trapezoid rule for each N
ST_SERIES = np.zeros(len(N_SERIES))
E_SERIES = np.zeros(len(N_SERIES))
Q_SERIES = np.zeros(len(N_SERIES))  # For convergence order


def e(N):
    t = np.linspace(0, T, N)
    ST = trapezoid(speed(t), t)
    S, _ = quad(speed, 0, T, epsabs=1.49e-12, epsrel=1.49e-12, limit=500)
    return abs(ST - S)


def q(e, N):
    return np.log2(e(N) / e(2 * N))


for n in range(len(N_SERIES)):
    print(q(e, N_SERIES[n]))


"""
ANTECKNINGAR:
trapezoid för 𝑁 = 100, 200, 400, 800:
 [12.04253355 12.03547874 12.03233961 12.03285432]

"""
