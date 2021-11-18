def check(txt = None):
        
        if (txt == None):
            return ("Invalid parameter")
        else:
            out = ''
            for i in txt:
                if i.isnumeric() and txt.count(i) > 1 and i not in out:
                    out += i
            return ((" ".join(out)) if len(out) > 0 else "None")

print(check('ab138g579b'))
print(check('h54325b144'))
print(check())
