a = input()
def fun(a):
    N = [i for i in a]
    for i in range(len(N)-1):
        if i%2 == 0: 
            if N[i] > N[i+1]: 
                return False
        else: 
            if N[i] < N[i+1]:
                return False
    return True 

print(fun(a))