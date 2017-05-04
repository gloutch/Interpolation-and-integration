## Computing the length of plane curves ##
# coding: utf-8

from math import sqrt
import numpy as np
from interpolation import *

# collection of method for approximation
def trapeze(f, a, b):
    return f(a) + f(b)

def middle_point(f, a, b):
    return 2 * f((a + b) / 2.)

def simpson(f, a, b):
    return f(a)/3. + 4 * f((a + b) / 2.)/3. + f(b)/3.

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

