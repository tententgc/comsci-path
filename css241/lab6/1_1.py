import math
eps = 1e-4
def f(x): return math.exp(-(x**2))


def recursive_trapezoid(f, a=0, b=1, n=60):
    def trapezoid(f, a, b, n):
        h = (b - a) / n
        s = 0.5 * (f(a) + f(b))
        for i in range(1, n):
            s += f(a + i * h)
        return s * h

    s = trapezoid(f, a, b, n)
    s1 = trapezoid(f, a, b, 2 * n)
    if abs(s1 - s) < eps:
        return s1
    else:
        return recursive_trapezoid(f, a, b, 2 * n)
    
