import numpy as np
def x1(x):
    y = (x**2 - 1)/(x - 1)
    return y
y1 = x1(0)
def x2(x):
    y = (x**2 - 25)/(x + 5)
    return y
y2 = x2(-4.99999999)
def x3(x):
    y = (x**2 - 2 * x - 8)/(x - 4)
    return y
y3 = x3(3.9999999)
def x4(x):
    y = 25/x
    return y
y4 = x4(-1e3)
y5 = x4(0.00000001)
def x(x):
    y = (x**2 + 2*x + 2)
    return y
y = x(-1)
yy = x(-1.00001)
S = (yy - y)/(-1.00001 - -1)
def diff(f, x, delta):
    return (f(x + delta) - f(x)) / delta
deltas = [1, 0.1, 0.01, 0.001, 0.0001, 0.000001, 0.0000001]
for delta in deltas:
    print(diff(f, 2, delta))



