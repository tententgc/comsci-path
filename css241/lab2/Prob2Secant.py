def f(x):
    return x**3-3*x+1

def secant(x0, x1):
    e = 0.000001
    N = 100
    step = 1
    condition = True
    while condition:
        if f(x0) == f(x1):
            break

        x2 = x0 - (x1-x0)*f(x0)/(f(x1) - f(x0))
        x0 = x1
        x1 = x2
        step = step + 1

        if step > N:
            break

        condition = abs(f(x2)) > e

    return x2

#64090500404 ธัญพิสิษฐ์ บัวประคอง