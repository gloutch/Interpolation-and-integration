## Interpolate couple of position describing position on the upper and lower surface of an airplane wing ##
# coding: utf-8

import numpy as np

# Compute and obtain second derivative on each point of the set
# Taken from Numerical recipes
# Adapted in our situation, where function's ends are like a line
def spline(x, y):
    n = len(x)
    
    u = np.empty(n)
    y2 = np.empty(n)
    
    y2[0] = 0.
    u[0] = 0.
    
    for i in range(1, n-1):
        sig = (x[i] - x[i-1]) / (x[i+1] - x[i-1])
        p = sig * y2[i-1] + 2.
        y2[i] = (sig - 1.) / p
        u[i] = (y[i+1] - y[i])/(x[i+1] - x[i]) - (y[i] - y[i-1])/(x[i] - x[i-1])
        u[i] = (6. * u[i] / (x[i+1] - x[i-1]) - sig * u[i - 1]) / p

    y2[n-1] = 0.
    
    for k in range(n-2, -1, -1):
        y2[k] = y2[k] * y2[k+1] + u[k]
    
    return y2

# Calculate the cubic-spline interpolated value of a given x
# Taken from Numerical recipes
def splint(xa, ya, y2a, x):
    n = len(xa)
    klo = 0
    khi = n-1
    
    while (khi - klo > 1) :
        k = (khi + klo) // 2
        if(xa[k] > x):
            khi = k
        else:
            klo = k

    h = xa[khi] - xa[klo]
    if(h == 0.):
        raise Exception("Error", "bad xa input in splint")

    a = (xa[khi] - x) / h
    b = (x - xa[klo]) / h
    y = a * ya[klo] + b * ya[khi] + (((a*a*a - a) * y2a[klo] + (b*b*b - b) * y2a[khi]) * (h*h) / 6.)

    return y

# Calculate the interpolation of the airfoil
def apply_spline(xa, ya):
    y2a = spline(xa, ya)
    return lambda x : splint(xa, ya, y2a, x)

