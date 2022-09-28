import numpy as np

def newton_coeffcient(x,y):
    n = len(x)
    x = np.array(x) 
    a = np.array(y)
    for i in range(1,n): 
        a[i:n] = (a[i:n]-a[i-1])/(x[i:n]-x[i-1])
    return a
        

def newton(x,xi,yi):
    a = newton_coeffcient(xi,yi)
    print(a)
    n = len(xi) - 1 
    p = a[n] 
    for i in range(1,n+1):
        p = a[n-i] + (x-xi[n-i])*p
    return p

#create polynomial
# def poly(xi,yi):
#     a = newton_coeffcient(xi,yi)
#     n = len(xi) - 1 
#     p = str(a[n]) 
#     for i in range(1,n+1):
#         p = str(a[n-i]) + " + (" + str(x) + " - " + str(xi[n-i]) + ") * (" + p + ")"
#     return p

a = (1, 2, 3, -4, 5)
fa = (2, 48, 272, 1182, 2262)
x = -1
print(newton(x, a, fa))
# print(poly(a, fa))
# 64090500404 ธัญพิสิษฐ์ บัวประคอง
