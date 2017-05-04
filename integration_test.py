## Integration tests ##
# coding: utf-8
import matplotlib.pyplot as plt
import math
from integration import *
from time import time

# polynome
X2 = lambda x: x * x
X3 = lambda x: x * x * x
phi3 = lambda x: x * x + x + 1
# trigonometric function
sin = math.sin
f = lambda x: x * math.sin(x + x) + 1


def test_methode():
    a = 0
    b = 1
    print("################")
    print("#    Method    #")
    print("################")
    print("===> Method test <===")
    print("f(x) = x**3 on ["+str(a)+", "+str(b)+"]")
    trap = trapeze(X3, a, b)
    print("Trapeze method : "+str(trap))
    mid_p = middle_point(X3, a, b)
    print("Middle point method : "+str(mid_p))
    sim = simpson(X3, a, b)
    print("Simpson method : "+str(sim))
    print()
test_methode()


def test_integrate():
    a = 0
    b = 4
    n = 100
    print("###################")
    print("#    Integrate    #")
    print("###################")
    print("===> Integrate test <===")
    print("f(x) = x**3 on ["+str(a)+", "+str(b)+"] with "+str(n)+" subdivisions, that gives 64")
    trap = integrate(X3, a, b, n, trapeze)
    print("Trapeze method : "+str(trap))
    mid_p = integrate(X3, a, b, n, middle_point)
    print("Middle point method : "+str(mid_p))
    sim = integrate(X3, a, b, n, simpson)
    print("Simpson method : "+str(sim))
    print()
test_integrate()

def test_derivative():
    a = 0
    b = 4
    n = 100
    print("###################")
    print("#    Derivate     #")
    print("###################")
    print("===> Derivate test <===")
    fig = plt.figure()
    x = [a+i*(b-a)/n for i in range(n+1)]

    fig.add_subplot(221)
    df1 = derivative(X2, a, b, n)
    y1 = [X2(i) for i in x]
    yprim1 = [df1(i) for i in x]
    plt.plot(x, y1, label="X2")
    plt.plot(x, yprim1, label="2X")
    plt.legend()
    
    fig.add_subplot(222)
    df2 = derivative(X3, a, b, n)
    y2 = [X3(i) for i in x]
    yprim2 = [df2(i) for i in x]
    plt.plot(x, y2, label="X3")
    plt.plot(x, yprim2, label="3X2")
    plt.legend()
    
    fig.add_subplot(223)
    df3 = derivative(phi3, a, b, n)
    y3 = [phi3(i) for i in x]
    yprim3 = [df3(i) for i in x]
    plt.plot(x, y3, label="phi3 : X2+X+1")
    plt.plot(x, yprim3, label="2X+1")
    plt.legend()

    fig.add_subplot(224)
    df4 = derivative(f, a, b, n)
    y4 = [f(i) for i in x]
    yprim4 = [df4(i) for i in x]
    plt.plot(x, y4, label="f: Xsin(2X)+1")
    plt.plot(x, yprim4, label="f' : 2Xcos(2X)+sin(2X)")
    plt.legend()
    
    plt.show()
    print()
test_derivative()

def test_length_curves():
    a = 0
    b = 10
    n = 100
    print("###################")
    print("#      Length     #")
    print("###################")
    print("===> Length of plane curves test <===")
    t1 = time()
    trap = length_of_plane_curves(X3, a, b, n, trapeze)
    t_trap = time() - t1
    print("Trapeze method : "+str(trap)+" in "+str(t_trap)+" seconds")
    t2 = time()
    mid_p = length_of_plane_curves(X3, a, b, n, middle_point)
    t_mid = time() - t2
    print("Middle point method : "+str(mid_p)+" in "+str(t_mid)+" seconds")
    t3 = time()
    sim = length_of_plane_curves(X3, a, b, n, simpson)
    t_sim = time() - t3
    print("Simpson method : "+str(sim)+" in "+str(t_sim)+" seconds")
    print()
test_length_curves()
    
# auxiliary function to compare integration method
def speed_and_accuracy(func, a, b, method, subdivision, expect):
    
    n = len(subdivision)
    speed = np.empty(n)
    accuracy = np.empty(n)
    
    for i in range(n):
        t = time()
        r = integrate(func, a, b, subdivision[i], method)
        speed[i] = time() - t
        accuracy[i] = abs(r - expect)

    return speed, accuracy 

def compare_integrate():
    global f
    fig = plt.figure()

    f = X3
    a = 0.
    b = 4.
    sub = range(9, 80, 2)
    expect = 64

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.set_ylabel("Execution time")
    ax2.set_ylabel("Relative error")

    c = "g"
    speed, accuracy = speed_and_accuracy(f, a, b, trapeze, sub, expect)
    ax1.plot(sub, speed, c, label="trapeze method")
    ax2.plot(sub, accuracy, c, label="trapeze method")

    c = "b"
    speed, accuracy = speed_and_accuracy(f, a, b, middle_point, sub, expect)
    ax1.plot(sub, speed, c, label="middle_point method")
    ax2.plot(sub, accuracy, c, label="middle point method")

    c = "r"
    speed, accuracy = speed_and_accuracy(f, a, b, simpson, sub, expect)
    ax1.plot(sub, speed, c, label="simpson method")
    ax2.plot(sub, accuracy, c, label="simpson method")

    plt.legend()
    plt.show()
compare_integrate()
