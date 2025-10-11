import numpy as np
import matplotlib.pyplot as plt

# Parámetros
g = 9.81
l = 1.0
dt = 0.01
N = 1000
t = np.arange(0, N*dt, dt)

# Condiciones iniciales: [theta0, omega0]
u0 = np.array([np.pi/6, 0.0])

# Definimos la función del sistema
def f(u, t):
    theta, omega = u
    return np.array([omega, - (g/l) * np.sin(theta)])

# Función Euler proporcionada
def euler(f, u, t):
    u = np.copy(u)
    dt = t[1] - t[0]
    for n in range(len(t)-1): 
        u[n+1] = u[n] + f(u[n], t[n])*dt
    return u

# Inicializamos la matriz para almacenar la solución
# Cada fila es [theta, omega]
u = np.zeros((N, 2))
u[0] = u0

# Ejecutamos Euler
u = euler(f, u, t)

# Extraemos resultados
theta = u[:,0]
omega = u[:,1]

# Graficar theta vs tiempo
plt.figure(figsize=(8,4))
plt.plot(t, theta)
plt.xlabel('Tiempo [s]')
plt.ylabel('θ [rad]')
plt.title('Péndulo simple - Método de Euler')
plt.show()

