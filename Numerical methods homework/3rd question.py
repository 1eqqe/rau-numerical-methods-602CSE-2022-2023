import numpy as np
from sympy import *
def f(x):
    return 0
def g(x):
    return -0
def newton(x0):
    step = 1
    flag = 1
    condition = True
    while condition:
        if g(x0) == 0.0:
            break
    x1 = x0 - f(x0) / g(x0)
    x0 = x1
    step = step + 1
    if step > N:
        flag = 0
        break