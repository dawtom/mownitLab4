import numpy as np
from sympy import *
import scipy.misc as scm

#
# x = Symbol('x')
#
# y = x**5 + 2 * x**4
# yprime = y.diff(x)
#
# print(yprime(5))


def dx(f,x):
    return abs(0-f(x))

def f(x):
    return x**3

def newtonsMethod(f,x0,e):
    delta = dx(f,x0)
    while(delta > e):
        x0 = x0 - (f(x0)/scm.derivative(f,x0,0.000001))
        delta = dx(f,x0)
    print("Root is at ", x0)
    print('f(x) at root is: ', f(x0))

newtonsMethod(f,5,0.0000001)



print(scm.derivative(f,5,0.001))
