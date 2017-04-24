## Computing the length of plane curves ##
# coding: utf-8

def trapeze(f, a, b):
    return f(a) + f(b)

def middle_point(f, a, b):
    return 2 * f((a + b) / 2.)

def simpson(f, a, b):
    return f(a)/3. + 4 * f((a + b) / 2.)/3. + f(b)/3.

