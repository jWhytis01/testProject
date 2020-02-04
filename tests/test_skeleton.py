# -*- coding: utf-8 -*-

import pytest
from testproject.skeleton import fib

__author__ = "jwhytis01"
__copyright__ = "jwhytis01"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
