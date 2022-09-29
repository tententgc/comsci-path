def temperature(start,end): 
    if (start <= end ): 
        res = (start*9/5)+32
        print (f'{start} degrees Celsius is {res} degrees Fahrenheit')
        temperature(start+1,end)
    

start = int(input())
end = int(input())
temperature(start,end)