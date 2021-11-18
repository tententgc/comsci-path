# txt = input('str = ')
# txt = 'ab138g579b'

txt = 'h54325b16'

out = ''
for i in txt:
    if i.isnumeric() and txt.count(i) > 1 and i not in out:
        out += i
print((" ".join(out)) if len(out) > 0 else "None")
