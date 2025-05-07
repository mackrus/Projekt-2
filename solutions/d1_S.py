import os

import numpy as np
from scipy.integrate import quad

PLOTDIR = '../plots/'
if not os.path.exists(PLOTDIR):
    os.makedirs(PLOTDIR)

"""
Skapa en funktion i Python, som givet en tidsvektor returnerar beloppet
av hastigheten |𝑣(𝑡)| i motsvarande
punkter där den analytiska vinkelhastig-heten ges av (4) . Övriga 3
parametervärden ( 𝜔 0, 𝜔 och 𝛾 ) ska tilldelas utanför
funktionen, och ska vara inparametrar till funktionen. Redovisa en figur
för hastigheten 𝑣 ( 𝑡 ) mellan 𝑡 =
0 och 𝑡 = 10 då 𝜔 = 2 𝜋 , 𝜔_0 = 3 𝜋 och
 𝛾 = 0 . 1. Använd 𝑁 = 4000 intervall för en
kontinuerlig kurva. Skriv sedan ett program i Python som beräknar (5)
med den (i SciPy ) inbyggda
integral lösaren quad och redovisa resultatet. Då kurvan för
 𝑣 ( 𝑡 ) är rela-tivt osnäll så är det
lämpligt att höja noggrannheten i beräkningen. I python
kan anropet till quad se ut som följande (där vi skapat en funktion som
heter vel , och där vi tilldelat värden för alla parametrar),
from scipy.integrate import quad, trapezoid
3 S, err = quad(vel, 0, T, args = (omega0,omega,gamma), ...

epsabs=1.49e-12, epsrel=1.49e-12, limit=500)

Här kan man fråga sig om man kommer se förväntad konvergens med Simpsons
formel. Notera att strikta felformeln för Simpson innehåller en
fjärdederivata av integranden, dvs absolutbeloppet av vinkelhastigheten
given av (4). Ser ni också någon varning då ni anropar quad i detta
fall?

Man ser att hastigheten för första gången (efter t=0) blir noll
nära 𝑡 = 0 . 255. Testa nu att räkna (med quad) mellan
 𝑡 = 0 och 𝑡= 0.25, där lösningen är snäll i hela
intervallet, där ni också plottar upp
 𝑣 ( 𝑡 ). Använd 𝑁 = 200 intervall i
detta fall.

 """
# KONSTANTER
omega = 2*np.pi
omega_0 = 3*np.pi
gamma = 0.1
N = 4000
T = 10

def theta_prime(gamma,omega,omega_0,t):
 first_part = (gamma * omega_0**2) / (omega_0**2 - omega**2)
 second_part = (omega_0*np.sin(omega_0*t)-omega*np.sin(omega*t))
 return first_part * second_part

def speed(t):
 return abs(theta_prime(gamma,omega,omega_0,t))

t = np.linspace(0,T,N)

speed_instance = speed(t)

S, err = quad(speed, 0, 0.25, epsabs=1.49e-12, epsrel=1.49e-12, limit=500)

print(S, err)

