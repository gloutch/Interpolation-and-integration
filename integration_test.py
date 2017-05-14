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
    print("################")
    print("#    Method    #")
    print("################")
    print("===> Method test <===")
    a = -1
    b = 1
    print("f(x) = x*sin(2x)+1 on ["+str(a)+", "+str(b)+"]")
    trap = trapeze(f, a, b)
    print("Trapeze method : "+str(trap))
    mid_p = middle_point(f, a, b)
    print("Middle point method : "+str(mid_p))
    sim = simpson(f, a, b)
    print("Simpson method : "+str(sim))
    gaus = gauss(f, a, b)
    print("Gauss method : "+str(gaus))
    romb = romberg(f, a, b)
    print("Romberg method : "+str(romb))
    print()

def test_integrate():
    print("###################")
    print("#    Integrate    #")
    print("###################")
    print("===> Integrate test <===")
    a = 0
    b = 4
    n = 100
    print("f(x) = x**3 on ["+str(a)+", "+str(b)+"] with "+str(n)+" subdivisions, that gives 64")
    trap = integrate(X3, a, b, n, trapeze)
    print("Trapeze method : "+str(trap))
    mid_p = integrate(X3, a, b, n, middle_point)
    print("Middle point method : "+str(mid_p))
    sim = integrate(X3, a, b, n, simpson)
    print("Simpson method : "+str(sim))
    gaus = integrate(X3, a, b, n, gauss)
    print("Gauss method : "+str(gaus))
    romb = integrate(X3, a, b, n, romberg)
    print("Romberg method : "+str(romb))
    print()

def test_derivative():
    print("###################")
    print("#    Derivate     #")
    print("###################")
    print("===> Derivate test <===")
    a = 0
    b = 4
    n = 100
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

def test_length_curves():
    print("###################")
    print("#      Length     #")
    print("###################")
    print("===> Length of plane curves test <===")
    a = 0
    b = 10
    n = 100
    t1 = time()
    trap = length_of_plane_curves(f, a, b, n, trapeze)
    t_trap = time() - t1
    print("Trapeze method : "+str(trap)+" in "+str(t_trap)+" seconds")
    t2 = time()
    mid_p = length_of_plane_curves(f, a, b, n, middle_point)
    t_mid = time() - t2
    print("Middle point method : "+str(mid_p)+" in "+str(t_mid)+" seconds")
    t3 = time()
    sim = length_of_plane_curves(f, a, b, n, simpson)
    t_sim = time() - t3
    print("Simpson method : "+str(sim)+" in "+str(t_sim)+" seconds")
    t4 = time()
    gaus = length_of_plane_curves(f, a, b, n, gauss)
    t_gaus = time() - t4
    print("Gauss method : "+str(gaus)+" in "+str(t_gaus)+" seconds")
    t5 = time()
    romb = length_of_plane_curves(f, a, b, n, romberg)
    t_romb = time() - t5
    print("Romberg method : "+str(romb)+" in "+str(t_romb)+" seconds")
    print()
    
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

    #f = f
    a = 0.
    b = 4.
    sub = range(9, 80, 2)
    expect = 4.538339629

    ax1 = fig.add_subplot(211)
    ax2 = fig.add_subplot(212)
    ax1.set_ylabel("Execution time")
    ax1.set_xlabel("Iterations")
    ax1.set_yscale('log')
    ax2.set_ylabel("Relative error")
    ax2.set_xlabel("Iterations")
    ax2.set_yscale('log')

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
    
    c = "c"
    speed, accuracy = speed_and_accuracy(f, a, b, gauss, sub, expect)
    ax1.plot(sub, speed, c, label="gauss method")
    ax2.plot(sub, accuracy, c, label="gauss method")
    
    c = "k"
    speed, accuracy = speed_and_accuracy(f, a, b, romberg, sub, expect)
    ax1.plot(sub, speed, c, label="romberg method")
    ax2.plot(sub, accuracy, c, label="romberg method")
    
    plt.legend()
    plt.show()

