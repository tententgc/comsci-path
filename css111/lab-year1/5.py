string=input()
old=input()
new1=input()
c=0
def myreplace(string,old,new1,counter):
    while old in string:
        string=string[:string.find(old)]+new1+string[string.find(old)+len(old):]
        counter+=1
    return(string,counter)   

print(*myreplace(string,old,new1,c),sep='\n')