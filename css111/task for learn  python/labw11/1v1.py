# txt = input('str = ')
txt = 'ab138g579b'

txt = 'h54325b16'
out = set()
for i in txt:
    if i.isnumeric() and txt.count(i) > 1:
        out.add(i)
print((" ".join(out)) if len(out) > 0 else "None")

