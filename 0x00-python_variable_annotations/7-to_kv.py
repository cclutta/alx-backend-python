#!/usr/bin/env python3
"""
to_kv module

Contains function to_kv
"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ returns a k,v. """
    v_1: float = v ** 2
    return (k, v_1)
