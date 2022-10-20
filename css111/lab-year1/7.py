a = input()
def fun(a): 
    temp = int(a[0]) 
    res = 0 
    
    for i in range(1,len(a)): 
        if int(a[i])>temp: 
            res += 1 
            temp = int(a[i])
        else: 
            res += -1
            temp = int(a[i])
    
    if res>=-1 and res<=1: 
        return True 
    else : 
        return False 
    
print(fun(a)) 