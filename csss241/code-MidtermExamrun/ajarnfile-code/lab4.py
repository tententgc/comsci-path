import numpy as np
def richardson_diff(x,h=0.75,N=2):
  n = N+1
  func = lambda x:x**6
  table = np.zeros((n,n),dtype=np.float64)
  diff_ = lambda x,h: (func(x+h)-func(x-h))/(2*h)

  for i in range(n):
    table[i,0] = diff_(x,h)
    for j in range(1,i+1):
      table[i][j] = table[i][j-1] + (table[i][j-1]-table[i-1][j-1]) / (4**j-1)
    h/=2
  print(table)

  return table[n-1][n-1]
