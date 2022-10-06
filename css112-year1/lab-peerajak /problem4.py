def p6():
  xi = map(int,input().split()) 
  yi = map(int, input().split())
  zi = [x*y for x,y in zip(xi,yi)] 
  print(*zi)
  
p6()