import math 
import numpy as np
eps =1e-4
f = lambda x: math.exp(-(x**2))

def romberg(f,a,b,n):
    I = np.zeros((n,n))
    h = b-a
    I[0,0] = 0.5*h*(f(a)+f(b))
    for i in range(1,n):
        h = h/2
        s = 0
        for k in range(1,2**(i-1)+1):
            s += f(a+(2*k-1)*h)
        I[i,0] = 0.5*I[i-1,0]+h*s
        for j in range(1,i+1):
            I[i,j] = I[i,j-1]+(I[i,j-1]-I[i-1,j-1])/(4**j-1)
    return I[n-1,n-1] 
    
    
print(romberg(f,0,1,5))