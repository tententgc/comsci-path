name = input("Please enter your name: ") 
age = int(input("please enter your age: ")) 

def checkTicket(name, age):
    Price = 15
    priceout = 0 
    
    def checkVIP(name): 
        vip = ["Tony","Peter","Mark","Kim","James","Kanny"]
        if name in vip: 
            x = True
            return x 
        else:
            x = False
            return x 
    
    if checkVIP(name) == True: 
        if age < 15: 
            priceout = 3.75
        else: 
            priceout = 7.5 
    else: 
        if age < 15: 
            priceout = 7.5 
        else: 
            priceout = 15.0
            
    print("The price for",name,"is",priceout)
    
    
    
checkTicket(name, age) 