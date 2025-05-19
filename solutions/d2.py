from scipy.integrate import quad, trapezoid
import numpy as np
import matplotlib.pyplot as plt

# (5) s(t) = intergral rand 0 - T abs(v(t))dt 

omega = 2*np.pi
omega_0 = 3*np.pi
gamma = 0.1
# theta = theta' = 0
T = 10
N = np.array([100,200,400,800])
k = T/N[1]

def theta(gamma,omega,omega_0,t):
 first_part = (gamma * omega_0**2) / (omega_0**2 - omega**2)
 second_part = (omega_0*np.sin(omega_0*t)-omega*np.sin(omega*t))
 return first_part * second_part

def speed(t):
 return abs(theta(gamma,omega,omega_0,t))

    
0
t = np.linspace(0,T,N[2])
S, err = quad(speed, 0, T, epsabs=1.49e-12, epsrel=1.49e-12, limit=500)
S_trap =  np.zeros(len(N))

for i in range(len(N)):
    t = np.linspace(0,T,N[i])
    S_trap[i] = trapezoid(speed(t),t)

felet = np.zeros(len(N))
for i in range(len(N)):
   felet[i] = abs(S-S_trap[i])

def fel(N):
    S_trap = np.zeros(len(N))
    diff = np.zeros(len(N))
    for i in range(len(N)):
        t = np.linspace(0,T,N[i])
        S_trap[i] = trapezoid(speed(t),t)
        diff[i] = abs(S_trap[i]-S)
    return diff

def q(fel, N):
    # Skapa en ny lista med dubbla värden
    N_double = [2*n for n in N]
    return abs(np.log2(fel(N)/fel(N_double)))

print(f'simpsons ger {S} error: {err}')
print(f'felet i med stegen {N}: felet = {felet}')
print(f'area under grafen {S_trap}')
print(f'konvergensen = {q(fel,N)}')
plt.plot(N,q(fel,N))
plt.yscale('log')

plt.xlabel('Antal $N$')
plt.ylabel('felet med logskala')
plt.savefig('errorplot')

plt.show()