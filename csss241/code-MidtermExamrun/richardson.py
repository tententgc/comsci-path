def richardson_diff(x,h=0.75,N=2):
    def f(x): return x**6 + 4*(x**5)
    
    if N == 0:
        return (f(x+h)-f(x-h))/(h*2)
    print("N",N,"h",h,"x",x)
    return (1/((4**N)-1))*((4**N)*richardson_diff(x,h/2,N-1)-richardson_diff(x,h,N-1))
    
print(richardson_diff(3))
