import matplotlib.pyplot as plt
import numpy as np
import pylab as py

def df_dt(x, t):

    a = 0.1
    b = 0.02
    c = 0.3
    d = 0.01

    """Funcion del sistema en forma canonica"""
    dx = a * x[0] - b * x[0] * x[1]
    dy = - c * x[1] + d * x[0] * x[1]
    return np.array([dx, dy])


# initial conditions for the system
x0 = 40
y0 = 9


# vector of times
t = np.linspace( 0, 200, 800 )

result = py.rk4( df_dt, [x0,y0], t )
print result


plt.plot(t,result)

plt.xlabel('Tiempo')
plt.ylabel('Tamano de la poblecion')
plt.legend(('presa','depredador'))
plt.title('Modelo Lotka-Volterra')
plt.show()