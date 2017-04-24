## Integration tests ##
# coding: utf-8

from integration import *
import math

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
    print("Simpson method : "+str(trap))
    print()
test_methode()

def  test_integrate():
    a = 0
    b = 4
    n = 10
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
    print("Simpson method : "+str(trap))
    print()
test_integrate()

