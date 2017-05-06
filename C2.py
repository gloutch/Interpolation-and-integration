import numpy as np

from scipy.misc import derivative


def derivative2(f,x,h):
    return (f(x+h)-f(x))/h



def f(x):
    return abs(x)


def test_cont(f,a,b):
    eps = 1e-20
    X = np.linspace(a+eps,b-eps,(b-a)*10)
    for x in X:
        if ( f(x) != f(x+eps) ) or ( f(x) != f(x-eps) ) or ( f(x-eps) != f(x+eps) ):
            return 0
    return 1


def test_deriv_1(f,a,b):
    eps = 1e-1
    X = np.linspace(a+eps,b-eps,(b-a)*10)
    for x in X:
        if abs(derivative(f,x-eps,0.01) - derivative(f,x+eps,0.01)) > 0.01:
            return 0,x
        if abs(derivative(f,x,0.01) - derivative(f,x+eps,0.01)) > 0.01:
            return 0,x
        if abs(derivative(f,x,0.01) - derivative(f,x-eps,0.01)) > 0.01:
            return 0,x
    return 1



def test_deriv_2(f,a,b):
    eps = 1e-17
    X = np.linspace(a+eps,b-eps,(b-a)*10)
    for x in X:
        if abs(derivative(f,x-eps,0.01,2) - derivative(f,x+eps,0.01,2)) >0.01:
            return 0,x
        if abs(derivative(f,x,0.01,2) - derivative(f,x+eps,0.01,2)) > 0.01:
            return 0,x
        if abs(derivative(f,x,0.01,2) - derivative(f,x-eps,0.01,2)) > 0.01:
            return 0,x
    return 1



#il reste la continuite de la derivee

def test_c_2(f,a,b):
    return test_deriv_1(f,a,b) and test_deriv_2(f,a,b) and test_cont(f,a,b)

#print test_c_2(f,-1,1)

print test_cont(f,-1,1)
print "--------------"
print test_deriv_1(f,-1,1)
#print "--------------"
#print test_deriv_2(f,-1,1)
