from math import *

def product(a): 
    p = 1
    for i in a: p*=i
    return p
    
def Lagrange(u,x,y):
    r = range(len(y)) 
    a = [y[i]/product(x[i]-x[ j] for j in r if j!=i) for i in r]
    print(a)
    return sum(a[i]*product(u-x[ j] for j in r if j!=i) for i in r)


# f(x) = 2/x+2 .  ---> สูตรคิด f(x) Lagrange
a = (8, -2, 5)
fa = (9, 2, 13)
print(Lagrange(-1,a,fa ))
# 64090500404 ธัญพิสิษฐ์ บัวประคอง
