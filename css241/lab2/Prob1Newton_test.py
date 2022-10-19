import Prob1Newton;

def test_newton1():
    eps =1e-4
    ans = 0.347296354
    assert ans-eps <= Prob1Newton.newton(0.1) <= ans+eps

def test_newton2():
    eps =1e-4
    ans = -1.87938
    assert ans-eps <= Prob1Newton.newton(-1.1) <= ans+eps
    
    
def test_newton3():
    eps =1e-4
    ans = 1.532088
    assert ans-eps <= Prob1Newton.newton(1.1) <= ans+eps
