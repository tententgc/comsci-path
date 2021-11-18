def check(a=None):
    if a == None:
        return "Invalid parameter"
    else:
        n = 0
        num = []
        for i in a:
            if i.isnumeric() and a.count(i) > 1:
                n += 1
                if i in num:
                    continue
                num.append(i)
        if n > 0:
            return (" ".join(num))
        else:
            return "None"


print(check('ab138g579b'))
print(check('h54325b1'))
print(check())
