## Computing the length of plane curves ##
# coding: utf-8

from math import sqrt
import numpy as np
from interpolation import *
<<<<<<< HEAD
#from scipy.special import legendre
#from scipy.special import roots_legendre
=======
from scipy.special import legendre
>>>>>>> 32c2b659aa09e6c2418c862cd6c1dd09fa1e3645

# collection of method for approximation
def trapeze(f, a, b):
    return f(a) + f(b)

def middle_point(f, a, b):
    return 2 * f((a + b) / 2.)

def simpson(f, a, b):
    return f(a)/3. + 4 * f((a + b) / 2.)/3. + f(b)/3.

def gauss(f, a=-1, b=1, eps=1e-8):
    gauss, s, r = 0, 0, 0
    while True:
        gauss = s
        s = 0
        r += 1
        Pr = legendre(r)
        roots = Pr.r
        dPr = Pr.deriv()
        for i in range(len(roots)):
            w = 2./((1-roots[i]**2)*(dPr(roots[i])**2))
            s += w * f(roots[i])
        if abs(gauss-s) < eps:
            return s

def romberg(f, a=-1, b=1, eps=1e-8):
    tmp = [[0.5 * (b - a) * (f(a) + f(b))]] 
    n = 1
    while True:
        h = float(b - a) / 2 ** n
        tmp.append([None] * (n + 1))  
        tmp[n][0] = 0.5*tmp[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in range(1, 2**(n-1)+1))
        for m in range(1, n+1):
            tmp[n][m] = tmp[n][m-1] + (tmp[n][m-1] - tmp[n-1][m-1]) / (4 ** m - 1)
        if abs(tmp[n][n-1] - tmp[n][n]) < eps:
            return tmp[n][n]
        n += 1

# compute the integral of f on [a, b] using
# nb_sub subdivision and with method approximation
def integrate(f, a, b, nb_sub, method):
    s = 0.
    h = (b - a) / nb_sub
    x0 = a
    x1 = a + h
    
    for i in range(nb_sub):
        g = lambda t: f( ((1 - t) * x0 / 2) + ((1 + t) * x1 / 2))
        s += ((x1 - x0) / 2) * method(g, -1, 1)

        x0 = x1
        x1 = x1 + h

    return s

# no tested function
# compute the derivative of f on [a, b] using n point
def derivative(f, a, b, n):
    step = (b - a) / n
    h = step / n
    h2 = 2 * h
    
    # set of point of derivative
    x = np.empty(n)
    y = np.empty(n)
    xi = a
    
    for i in range(n):
        y[i] = (f(xi + h) - f(xi - h)) / h2
        x[i] = xi

        xi = xi + step

    return apply_spline(x, y)

# no tested function
def length_of_plane_curves(f, a, b, n, method):
    df = derivative(f, a, b, n)
    g = lambda x: sqrt(1+df(x)**2)
    return integrate(g, a, b, n, method)

