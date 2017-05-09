from math import exp, cos

from scipy import integrate


def romberg(f, a, b, eps=1e-8):
    tmp = [[0.5 * (b - a) * (f(a) + f(b))]] 
    n = 1
    while True:
        h = float(b - a) / 2 ** n
        tmp.append([None] * (n + 1))  
        tmp[n][0] = 0.5*tmp[n-1][0] + h*sum(f(a+(2*k-1)*h) for k in xrange(1, 2**(n-1)+1))
        for m in xrange(1, n+1):
            tmp[n][m] = tmp[n][m-1] + (tmp[n][m-1] - tmp[n-1][m-1]) / (4 ** m - 1)
        if abs(tmp[n][n-1] - tmp[n][n]) < eps:
            return tmp[n][n]
        n += 1


#tests :

def myfunc(t):
    return exp(-t*t) + cos(t)


print "Our implemenation"
print romberg(myfunc, 0, 1)

print "----------"

print "calcul_python_quad"
print integrate.quad(myfunc, 0, 1)[0]
