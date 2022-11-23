

# function that filters vowels
def fun(variable):
    letters = ['a', 'e', 'i', 'o', 'u']
    if (variable in letters):
        return True
    else:
        return False
  
  
# sequence
sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r']
  
# using filter function
filtered = filter(fun, sequence)
  
    
li =[0.2,-1000,1000,33.21,-101.12,0.01,212,0.4,-0.3,-100]
lnew = list(map(lambda x: x+10000 if x>(-0.5) and x<0.5 else x,li)) #1


# print(list((lambda x: 10000+x if -0.5 < x < 0.5 else x)(x) for x in li))

from functools import reduce
x = 100111001

# order = "10011100101"
# print(reduce(lambda x,y: x+1 if y[0] != y[1] else x, zip(order, order[1:]),0))

# a = input()
# print(sum([1 for i in range(len(a)-1) if a[i]!=a[i+1]]))


x = [1,2,3,4,5]
y = [10,20,30,40,50]
z = list(map(lambda x,y: x+y if y == 10 else x+1 ,x,y))
print(z)