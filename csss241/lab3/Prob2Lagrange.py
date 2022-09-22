from math import *

def product(a): 
    p = 1
    for i in a: p*=i
    return p
    
def Lagrange(u,x,y):
    r = range(len(y)) 
    a = [y[i]/product(x[i]-x[ j] for j in r if j!=i) for i in r]
    return sum(a[i]*product(u-x[ j] for j in r if j!=i) for i in r)

# 64090500404 ธัญพิสิษฐ์ บัวประคอง
