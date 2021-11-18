def check(txt=0):
    if type(txt) == int:
        return "Invalid parameters"
    count = 0
    listnum = []
    
    for i in txt:
        if i.isnumeric() and txt.count(i) > 1:
            count += 1
            if i in listnum:
                continue
            listnum.append(i)
    return ((" ".join(listnum)) if count > 0 else "None")


print(check('ab138g579b'))
print(check('h54325b144'))
print(check())
print(check(""))
