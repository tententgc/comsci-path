def check(txt=0):

    try:
        out = set()
        for i in txt:
            if i.isnumeric() and txt.count(i) > 1:
                out.add(i)
        return((" ".join(out)) if len(out) > 0 else "None")
    except:
        return ("Invalid parameter")



print(check('ab138g579b') )
print(check('h54325b1'))
print(check())
print(check(''))
