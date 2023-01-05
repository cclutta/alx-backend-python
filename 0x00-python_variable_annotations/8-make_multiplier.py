#!/usr/bin/env python3
"""
multiplier module

Contains function multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ returns multiplier by the float """
    return lambda x: multiplier * x
