import math 
def adaptive_simpson(f,a,b,eps,level, level_max):
    if level > level_max:
        return 0
    c = (a+b)/2
    h = b-a
    d = (a+c)/2
    e = (c+b)/2
    s1 = h/6*(f(a)+4*f(c)+f(b))
    s2 = h/12*(f(a)+4*f(d)+2*f(c)+4*f(e)+f(b))
    if abs(s2-s1) < 15*eps:
        return s2 + (s2-s1)/15
    return adaptive_simpson(f,a,c,eps/2,level+1,level_max) + adaptive_simpson(f,c,b,eps/2,level+1,level_max)

eps =1e-4
f = lambda x: math.exp(-(x**2))
print(adaptive_simpson(f,0,1,eps,1,7))