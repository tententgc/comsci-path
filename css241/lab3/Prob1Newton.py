def newton(x,xi,yi):
    
    #x is a floating number, eg. x=10.23
    #xi is a list of x values, eg. xi=[10,20,30]
    #yi is a list of f(x) values, eg. yi=[1,2,3]
    
    n=len(xi)
    y=0
    for i in range(n):
        t=yi[i]
        for j in range(n):
            if j!=i:
                t=t*(x-xi[j])/(xi[i]-xi[j])
        y=y+t
    return y


# 64090500404 ธัญพิสิษฐ์ บัวประคอง
