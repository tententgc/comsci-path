a=input()

def showinput(a):
    x = int(a[0])
    temp = [x]
    res = 0
    for i in range(1,len(a)):
        if int(temp[-1])-int(a[i])>0: 
            temp.append(a[i]) 
            res += 1
            
        elif int(temp[-1])-int(a[i])==0:
            print(res)
            break
            
        else: 
            temp.append(a[i])
            res += -1

    if res ==0 or res == -1 or res == 1: 
        return True
    else: 
        return False
print(showinput(a) )



