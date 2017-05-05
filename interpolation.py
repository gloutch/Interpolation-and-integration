## Interpolate couple of position describing position on the upper and lower surface of an airplane wing ##
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

# Compute and obtain second derivative on each point of the set
# Taken from Numerical recipes
def spline(x, y, yp1, ypn):
    max = .99e30
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

# Calculate the cubic-spline interpolated value of a given x
# Taken from Numerical recipes
def splint(xa, ya, y2a, n, x):
    klo = 0
    khi = n-1
    while (khi-klo > 1) :
        k=int((khi+klo) / 2)
        if(xa[k] > x):
            khi = k
        else:
            klo = k

    h = xa[khi] - xa[klo]

    if(h == 0.):
        raise Exception("Error", "bad xa input in splint")

    a = (xa[khi] - x) / h
    b = (x - xa[klo]) / h
    y = a * ya[klo] + b * ya[khi] + ((a**3 - a) * y2a[klo] + (b**3 - b) * y2a[khi]) * (h**2) / 6.

    return y

# Calculate the interpolation of the airfoil
def apply_spline(xa, ya):
    n = len(xa)
    yp1 = 1e30
    ypn = 1e30    
    return lambda x : splint(xa, ya, spline(xa, ya, yp1, ypn), len(xa), x)

def derivate(f, h):
    return lambda x : (f(x+h) - f(x)) / h
    

def test():
    f = lambda x : x*x*x
    x = np.arange(0, 3, 0.1)
        
    plt.figure(1)
    plt.plot(x, f(x))
    plt.plot(x, derivate(f, 0.001)(x))
    plt.plot(x, derivate(derivate(f, 0.001), 0.001)(x))
    plt.show()
    
def test_wing():
    file = "C:\\Users\\Elfen\\Desktop\\Algonum5\\Interpolation-and-integration\\boe103.txt"
    print("===> Interpolation test for ", file, " <===")
    (ex,ey,ix,iy) = load_foil(file)
    
    plt.figure(1)

    nbpoints = 300
    
    extrados = apply_spline(ex, ey) 
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x1 = np.arange(ex[0], ex[len(ex)-1], pas)
    y1 = []
    for i in range(nbpoints):
        y1.append(extrados(x1[i]))

    intrados = apply_spline(ix, iy) 
    pas = (ix[len(ix)-1] - ix[0]) / nbpoints
    x2 = np.arange(ix[0], ix[len(ix)-1], pas)
    y2 = []
    for i in range(nbpoints):
        y2.append(intrados(x2[i]))
        
    plt.plot(x1, y1, "r")
    plt.plot(x2, y2, "r")
    
    y1 = []
    for i in range(nbpoints):
        y1.append(derivate(extrados, 0.001)(x1[i]))
    y2 = []
    for i in range(nbpoints):
        y2.append(derivate(intrados, 0.001)(x2[i]))
     
    plt.plot(x1, y1, "g")
    plt.plot(x2, y2, "g")
    """
    y1 = []
    for i in range(nbpoints):
        y1.append(derivate(derivate(extrados, 0.001), 0.001)(x1[i]))
    y2 = []
    for i in range(nbpoints):
        y2.append(derivate(derivate(intrados, 0.001), 0.001)(x2[i]))
     
    plt.plot(x1, y1, "b")
    plt.plot(x2, y2, "b")
       
    plt.show()
    """
#test_wing()
