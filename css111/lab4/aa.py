import numpy as np 

r = 10
n = 4

header= ["period"]
header1= (x for x in range(1,r + 1 ))
header2 = header.extend(header1)
print(header2)