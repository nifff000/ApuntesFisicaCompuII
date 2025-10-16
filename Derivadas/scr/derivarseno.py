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


