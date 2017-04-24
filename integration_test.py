## Integration tests ##
# coding: utf-8

from integration import *

def test_integ(integ, f, a, b):
    return integ(f, a, b)


def Test_integration():
    f = lambda x: x**3
    a = 0
    b = 1
    print("#####################")
    print("#    Integration    #")
    print("#####################")
    print("===> Integration test <===")
    print("f(x) = x**3 on ["+str(a)+", "+str(b)+"]")
    trap = test_integ(trapeze, f, a, b)
    print("Trapze method : "+str(trap))
    mid_p = test_integ(middle_point, f, a, b)
    print("Middle point method : "+str(mid_p))
    sim = test_integ(simpson, f, a, b)
    print("Simpson method : "+str(trap))


Test_integration()
