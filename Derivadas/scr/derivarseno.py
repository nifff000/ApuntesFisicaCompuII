import numpy as np
import matplotlib.pyplot as plt

h = 0.01
x = np.linspace(-2*np.pi,2*np.pi,30)
df = (np.sin(x+h)-np.sin(x))/(h)
f = np.sin(x)
derivadaanalitica = np.cos(x)

plt.plot(x,df,color='blue',label = 'Derivada numerica')
plt.plot(x,derivadaanalitica,color = 'red',linestyle='--',label = 'Derivada analitica')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

# --- 2. Generación de los valores de h ---
# Usamos un rango mucho más amplio (e.g., 40 puntos) para ver bien la 'V'
h = np.geomspace(1e-20, 1e-1, 40)

# --- 3. Cálculo de la derivada numérica y el error para cada h ---
# Aproximación de la derivada en x=1
df = ( f(1+h) - f(1) ) / h

# Cálculo del error absoluto
error = np.abs( df - derivada_exacta )

# --- 4. Graficación para visualizar el mínimo error ---
plt.figure(figsize=(10, 6))

# Log-log plot para ver claramente el comportamiento del error
plt.loglog(h, error, "o-", label="Error absoluto") 

# Etiquetar el punto de error mínimo
min_error = np.min(error)
min_h = h[np.argmin(error)]
plt.loglog(min_h, min_error, 'r*', markersize=15, label=f'Mínimo Error\n$h \approx {min_h:.2e}$')

# Configuración de la gráfica
plt.xlabel(r"$h$ (Paso de Diferencia Finita)", fontsize=14)
plt.ylabel("Error absoluto", fontsize=14)
plt.title(r"Error de la Derivada Numérica de $\sin(x)$ en $x=1$ vs. $h$", fontsize=16)
plt.grid(True, which="both", ls="--", linewidth=0.5) 
plt.legend()
plt.show()