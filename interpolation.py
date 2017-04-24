## Interpolate couple of position describing position on the upper and lower surface of an airplane wing ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# Compute and obtain second derivative on each point of the set
# Taken from Numerical recipes
def spline(x, y, yp1, ypn, max = 99e30):
    n = len(x)-1
    u = np.zeros(n)
    y2 = np.zeros(n+1)
    
    if(yp1 > max):
        y2[0] = 0.
        u[0] = 0.
    else:
        y2[0] = -0.5
        u[0] = (3. / (x[1] - x[0])) * ((y[1] - y[0]) / (x[1] - x[0]) - yp1)
    
    for i in range(1, n-1):
        sig = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
        p = sig * y2[i-1] + 2.
        y2[i] = (sig - 1.) / p
        u[i] = (6. * ((y[i+1] - y[i]) / (x[i+1] - x[i]) - (y[i] - y[i-1]) / (x[i] - x[i-1])) / (x[i+1] - x[i-1]) - sig*u[i-1]) / p
    
    if (ypn > max):
        qn = 0.
        un = 0.
    else:
        qn = 0.5
        un = (3. / (x[n] - x[n-1])) * (ypn - (y[n] - y[n-1]) / (x[n] - x[n-1]))
    
    y2[n] = (un - qn * u[n-1]) / (qn * y2[n-1] + 1.)

    for k in range(n-1, 1, -1):
        y2[k] = y2[k] * y2[k+1] + u[k]
    
    return y2
