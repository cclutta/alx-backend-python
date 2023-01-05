#!/usr/bin/env python3
"""
sum_list module

Contains function sum_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ returns the sum of list. """
    sum: float = 0
    for i in input_list:
        sum += i
    return sum
