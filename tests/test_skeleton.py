#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
from solve_led.skeleton import fib

__author__ = "Robert De Bhal"
__copyright__ = "Robert De Bhal"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
