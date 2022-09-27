def newton(xstart):
    x = xstart
    
    def f(x): 
        return x**3-3*x+1

    def fprime(x):
        return 3*x**2-3
    
    for i in range(100):
        x = x - f(x)/fprime(x)
        
    return x 

print(newton(20))
#64090500404 ธัญพิสิษฐ์ บัวประคอง