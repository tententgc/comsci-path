import numpy as np 


def Problem1(x, xi, yi):
     
    nx = len(xi)
    ny = len(yi)

    z = [0]
    q = list()

    for i in range(1,nx):
        q = (yi[i] - yi[i-1]) / (xi[i] - xi[i-1]) 
        z.append(-z[i-1] + 2 * q)

    eq_list = []
    ans = 0

    for i in range(nx - 1):
        a = 0.5 * (z[i+1] - z[i]) / (xi[i+1] - xi[i])
        b = -2 * a * xi[i] + z[i]
        c = a*xi[i]**2 - z[i] * xi[i] + yi[i]
        eq_list.append((a, b, c))
        
    for i in range(nx - 1):
        if xi[i] <= x <= xi[i+1]:
            ans = eq_list[i][0] * (x-xi[i])**2 + z[i]*(x-xi[i]) + yi[i]
            break
    return ans