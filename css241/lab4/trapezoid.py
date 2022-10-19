import math

def trapezoid(f, a, b, n):
    h = (b-a)/n
    s = 0.5*(f(a)+f(b))
    for i in range(1,n):
        s += f(a+i*h)
    return s*h


def f(x): return math.exp(-(x**2))

print(trapezoid(f,0,1,60))