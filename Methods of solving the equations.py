from math import cos, exp, sin

def func(x):
    y = (x + 3) * cos(x - 5) - 2 * exp(x / 10)
    return y

def f(x):
    return func(x) + x

def appr(eps, a, b):
    x1 = a
    y1 = f(x1)
    y2 = y1
    x2 = y2
    y1 = f(x2)

    while abs(y1 - y2) > eps:
        y2 = y1
        x1= x2
        x2 = y2
        y1 = f(x2)

    return f'{x1} : {x2}'

def tangent_dot(x):
    return x - (func(x) / derivative(x))

def derivative(x):
    return (func(x + 0.000001) - func(x)) / 0.000001

def newt(eps, a, b):
    steps = [i / 100 for i in range(-100, 300)]
    first_suited_value = True
    for xn in steps:
        i = 0
        while True:
            i += 1

            if derivative(xn) == 0:
                break

            xn = tangent_dot(xn)

            if xn < a or xn > b:
                break

            if abs(func(xn)) <= eps:
                first_suited_value = False
                break

        if not first_suited_value:
            return xn

eps = 0.001
a = -1
b = 3

print(newt(eps, a, b))
print(appr(eps, a, b))