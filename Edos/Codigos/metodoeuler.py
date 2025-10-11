# Ejemplo visible: Resolver sistema presa-cazador (Lotka-Volterra) con método de Euler
import numpy as np
import matplotlib.pyplot as plt

# Método de Euler para sistemas: u es array (N, m) donde m=2 (presa, cazador)
def euler_system(f, u, t):
    u = np.copy(u)
    dt = t[1] - t[0]
    for n in range(len(t)-1):
        u[n+1, :] = u[n, :] + f(u[n, :], t[n]) * dt
    return u

# Modelo Lotka-Volterra (presa, cazador)
def lotka_volterra(u, t):
    x, y = u  # x = presa, y = cazador
    alpha = 1.0   # tasa de crecimiento presa
    beta  = 0.1   # tasa de depredación
    delta = 0.075 # eficiencia de conversión (presas->cazadores)
    gamma = 1.5   # mortalidad cazador
    dxdt = alpha*x - beta*x*y
    dydt = delta*x*y - gamma*y
    return np.array([dxdt, dydt])

# Condiciones y tiempo
t = np.linspace(0, 30, 6000)       # tiempo: 0 a 30 con muchos pasos (dt pequeño)
u0 = np.zeros((len(t), 2))
u0[0, 0] = 40.0   # presa inicial
u0[0, 1] = 9.0    # cazador inicial

# Resolver con Euler
u_euler = euler_system(lotka_volterra, u0, t)

# Mostrar resultados: poblaciones en el tiempo
plt.figure()
plt.plot(t, u_euler[:, 0], label='Presa (Euler)')
plt.plot(t, u_euler[:, 1], label='Cazador (Euler)')
plt.xlabel('Tiempo')
plt.ylabel('Población')
plt.legend()
plt.grid()
plt.show()

# Mostrar fase (presa vs cazador)
plt.figure()
plt.plot(u_euler[:, 0], u_euler[:, 1])
plt.xlabel('Población presa')
plt.ylabel('Población cazador')
plt.title('Diagrama fase (Euler)')
plt.grid()
plt.show()

# Imprimir valores finales rápidos
print("Valores finales (t={:.2f}): presa = {:.3f}, cazador = {:.3f}".format(t[-1], u_euler[-1,0], u_euler[-1,1]))

