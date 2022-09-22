import Prob2Secant;

def test_secant1():
    eps =1e-4
    ans = 0.347296354
    assert ans-eps <= Prob2Secant.secant(0.4,1) <= ans+eps

def test_secant2():
    eps =1e-4
    ans = -1.87938
    assert ans-eps <= Prob2Secant.secant(-1,-2) <= ans+eps
    
    
def test_secant3():
    eps =1e-4
    ans = 1.532088
    assert ans-eps <= Prob2Secant.secant(4,1) <= ans+eps
