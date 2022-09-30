f = open("lab5/multiply.txt", "x")
def temperature(start,end): 

    if (start <= end ): 
        res = (start*9/5)+32
        f.write(str(start) + "C = " + str(res) + "F \n")
        temperature(start+1,end)
    

start = int(input())
end = int(input())
res = temperature(start,end)