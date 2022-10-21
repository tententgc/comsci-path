import math
eps =1e-4
f = lambda x: math.exp(-(x**2))

def recursive_trapezoid(f,a=0,b=1,n=60):
    
    if n == 0:
        return (1/2)*(b-a)*(f(a)+f(b))
    m = 0 
    h = (b-a)/(2**n)
    for i in range(1,2**(n-1)+1):
        m += f(a+(2*i-1)*h)
    return 1/2*recursive_trapezoid(f,a,b,n-1)+h*m

print(recursive_trapezoid(f,0,1,5)) 