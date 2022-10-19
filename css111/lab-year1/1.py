a=input()
b=input()
c=input()

def myreplace(a,b,c): 
    a = a.split(" ")
    n = 0
    for i in range(len(a)): 
        
        if a[i] == b:
            a[i] = c
            n+=1
        if b in a[i]:
            q = a[i].find(b) 
            a[i] = a[i][:q] + c + a[i][q+len(b):]
            n+=1
            
    print(" ".join(a))
    print(n)     
    
    
    
myreplace(a,b,c)