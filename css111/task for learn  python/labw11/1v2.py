
# a=  'ab138g579b'
a= 'h54325b1'

n = 0
num  = [] 
for i in a: 
    if i.isnumeric() and a.count(i)> 1:
        n +=1 
        if i in num:
            continue
        num.append(i)
if n > 0:
    print(*num)
else:
    print("None")