import numpy as np

from scipy.misc import derivative

def f(x):
    return x**2


def test_cont(f,a,b):
    eps = 1e-20
    X = np.linspace(a+eps,b-eps,(b-a)*100)
    for x in X:
        if ( f(x) != f(x+eps) ) or ( f(x) != f(x-eps) ) or ( f(x-eps) != f(x+eps) ):
            return 0
    return 1


def test_deriv_1(f,a,b):
    eps = 1e-17
    X = np.linspace(a+eps,b-eps,(b-a)*100)
    for x in X:
        if (derivative(f,x-eps,0.01) != derivative(f,x+eps,0.01)) or (derivative(f,x,0.01) != derivative(f,x+eps,0.01)) or (derivative(f,x,0.01) != derivative(f,x-eps,0.01)):
            return 0,x
    return 1



def test_deriv_2(f,a,b):
    eps = 1e-17
    X = np.linspace(a+eps,b-eps,(b-a)*100)
    for x in X:
        if (derivative(f,x-eps,0.01,2) != derivative(f,x+eps,0.01,2)) or (derivative(f,x,0.01,2) != derivative(f,x+eps,0.01,2)) or (derivative(f,x,0.01,2) != derivative(f,x-eps,0.01,2)):
            return 0,x
    return 1



#il reste la continuite de la derivee

def test_c_2(f,a,b):
    return test_deriv_1(f,a,b) and test_deriv_2(f,a,b) and test_cont(f,a,b)
