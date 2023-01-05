#!/usr/bin/env python3
"""
element_length module

Contains function element_length
"""
from typing import Iterable, Sequence, Union, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ return values with the appropriate types. """
    return [(i, len(i)) for i in lst]
