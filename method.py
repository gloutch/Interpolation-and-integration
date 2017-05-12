from math import exp, cos

from scipy import integrate
from scipy.special import legendre
from scipy.special import roots_legendre

def gauss(f, a=-1, b=1, eps=0.1):
    gauss, s, r = eps+1, 0, 0
    while (abs(gauss-s) > eps):
        gauss = s
        s = 0
        r += 1
        Pr = legendre(r, [a, b])
        for i in range(10):
            print(Pr(i))
        print(Pr)
        roots = roots_legendre(r)
        print(roots)
        dPr = Pr.deriv()
        print(dPr)
        for i in range(len(roots)):
            w = 2./((1-roots[i]**2)*(dPr(roots[i])**2))
            s += w * f(roots[i])
    return s

#tests :

def myfunc(t):
    return exp(-t*t) + cos(t)


print("Our implemenation")
print(gauss(myfunc, 0, 1))

print("----------")

print("calcul_python_quad")
print(integrate.quad(myfunc, 0, 1)[0])
