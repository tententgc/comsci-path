import numpy as np

def triband(a,d,c,b):
    n = len(b)
    for i in range(1,n):
        mult = a[i-1]/d[i-1]
        d[i] = d[i] - mult*c[i-1]
        b[i] = b[i] - mult*b[i-1]
    x = d
    x[-1] = b[-1]/d[-1]
    for i in range(n-2,-1,-1):
        x[i] = (b[i] - c[i]*x[i+1])/d[i]
    return x 

def Problem3(a,d,c,b):
    return triband(a,d,c,b)