## Computing the length of plane curves ##
# coding: utf-8

import numpy as np


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
        x[i] = (f(xi + h) - f(xi - h)) / h2
        y[i] = xi

        xi = xi + step

    # return interpation(x, y)
    # for now
    print(x)
    print(y)
    return f

# to check syntaxe
derivative(lambda x: x * x, 0, 1, 5)
