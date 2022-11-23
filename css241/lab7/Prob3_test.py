import Prob3 as p3
import numpy as np


def test_1():
    d = np.ones((4,), dtype=np.float64)
    a = 0.5*np.ones((3,), dtype=np.float64)
    c = 0.5*np.ones((3,), dtype=np.float64)
    b = np.array([1.5, 2, 2, 1.5], dtype=np.float64)
    x = p3.Problem3(a, d, c, b)
    assert (np.absolute(x - np.array([1.,  1., 1.,  1.])) < 1e-5).all()


def test_2():
    d = np.ones((100,), dtype=np.float64)
    a = 0.5*np.ones((99,), dtype=np.float64)
    c = 0.5*np.ones((99,), dtype=np.float64)
    b = np.array(
        [1.5 if i == 0 or i == 99 else 2.0 for i in range(100)], dtype=np.float64)
    x = p3.Problem3(a, d, c, b)
    assert (np.absolute(x - np.ones((100,), dtype=np.float64)) < 1e-5).all()
