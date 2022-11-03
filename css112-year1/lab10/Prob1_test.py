import Prob1 as p1
import numpy as np


def test_1():
    one3 = p1.Problem1(3)
    assert (one3 == np.array([[1., 0., 0.], [1., 1., 0.], [1., 1., 1.]])).all()


def test_2():
    one4 = p1.Problem1(4)
    assert (one4 == np.array([[1., 0., 0., 0.], [1., 1., 0., 0.], [
            1., 1., 1., 0.], [1., 1., 1., 1.]])).all()
