#!/usr/bin/env python3
"""
sum__mixed_list module

Contains function sum_mixed_list
"""
from typing import List, Union


def sum_mixed_list(mixd_lst: List[Union[float, int]]) -> float:
    """ returns the sum of list. """
    sum: float = 0
    for i in mixd_lst:
        sum += i
    return sum
