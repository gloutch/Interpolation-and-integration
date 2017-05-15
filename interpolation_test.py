## Interpolation tests ##
# coding: utf-8

from interpolation import *
import matplotlib.pyplot as plt
import math
from Open import *

f = lambda x: ((1 + x)**3) * ((1 - x)**3) * math.cos(x)

def display_interpolation(file):
    print("#####################")
    print("#   Interpolation   #")
    print("#####################")
    print("===> Interpolation test for ", file, " <===")
    (ex,ey,ix,iy) = load_foil(file)
    
    nbpoints = 1200
    
    extrados = apply_spline(ex, ey) 
    pas = (ex[len(ex)-1] - ex[0]) / nbpoints
    x1 = np.arange(ex[0], ex[len(ex)-1], pas)
    y1 = np.empty(nbpoints)
    for i in range(nbpoints):
        y1[i] = extrados(x1[i])

    intrados = apply_spline(ix, iy) 
    pas = (ix[len(ix)-1] - ix[0]) / nbpoints
    x2 = np.arange(ix[0], ix[len(ix)-1], pas)
    y2 = np.empty(nbpoints)
    for i in range(nbpoints):
        y2[i] = intrados(x2[i])
        

    plt.plot([0, 1], [0, 0], color='black')

    # interpolaton
    plt.plot(x1, y1, "r")
    plt.plot(x2, y2, "r")
    
    # original shape
    plt.plot(ex, ey, "b--")
    plt.plot(ix, iy, "b--") 

    plt.title("Interpolated points of " + file)
    plt.show()


    
def convergence_interpolation():
    nbpoints = 10
    
    fig = plt.figure()
    f1 = fig.add_subplot(121)
    x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
    y = np.empty(nbpoints + 1)
    for i in range(nbpoints + 1):
        y[i] = f(x[i])
    f1.plot(x, y, "bo")
    
    nbpoints = 1000
    interpolation = apply_spline(x, y) 
    x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
    y = np.empty(nbpoints + 1)
    for i in range(nbpoints + 1):
        y[i] = interpolation(x[i])
    f1.plot(x, y, "r")
    plt.title('Interpolation based on blue points')
    
    error = []
    N = []
    nbpoints = 2
    n = 1000
    
    for i in range(7):
        N.append(nbpoints)
        x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
        y = np.empty (nbpoints + 1)
        for i in range(nbpoints + 1):
            y[i] = f(x[i])
        interpolation = apply_spline(x, y)
        x = []
        y = []
        for i in range(n):
            x.append(interpolation(i * 1/n) - f(i * 1/n))
            y.append(f(i * 1/n))
        error.append(np.linalg.norm(x) / np.linalg.norm(y))
        nbpoints = nbpoints * 2
        
    f2 = fig.add_subplot(122) 
    f2.set_yscale('log')
    f2.plot(N, error, "g")
    plt.xlabel("Interpolation points")
    plt.title('Error')
    
    plt.show()


    
def derivate(f, h, x):
    return lambda x: (f(x + h) - f(x)) / h
    
def test_C2():
    
    fig = plt.figure()
    f1 = fig.add_subplot(221)
    nbpoints = 1000
    x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
    y = np.empty(nbpoints + 1)
    for i in range(nbpoints + 1):
        y[i] = f(x[i])
    f1.plot(x, y, "b")
    plt.title("f(x) = (1+x)^3 * (1-x)^3 * cos(x)")
    
    f2 = fig.add_subplot(222)
    nbpoints = 10
    x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
    y = np.empty (nbpoints + 1)
    for i in range(nbpoints + 1):
        y[i] = f(x[i])
    f2.plot(x, y, "bo")
    plt.title("Interpolation of f")
    
    nbpoints = 1000
    interpolation = apply_spline(x, y) 
    x = np.arange(-1, 1 + 2/nbpoints, 2/nbpoints)
    y = np.empty(nbpoints + 1)
    for i in range(nbpoints + 1):
        y[i] = interpolation(x[i])
    f2.plot(x, y, "r")
    
    f3 = fig.add_subplot(223)
    h = 10**(-6)
    y = np.empty(nbpoints + 1)
    C1 = derivate(interpolation, h, x)
    for i in range(nbpoints + 1):
        y[i] = C1(x[i])
    f3.plot(x, y, "g")
    plt.title("f'")
    
    f4 = fig.add_subplot(224)
    h = 10**(-6)
    y = np.empty(nbpoints + 1)
    C2 = derivate(C1, h, x)
    for i in range(nbpoints + 1):
        y[i] = C2(x[i])
    f4.plot(x, y, "purple")
    plt.title("f''")
    plt.show()

