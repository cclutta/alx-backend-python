#!/usr/bin/env python3
"""
safely_get_value module

Contains function safely_get_value
"""

from typing import Mapping, Any, Union, TypeVar

T = TypeVar("T")


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
        ReturnsThe value of the key or "default" if nothing is found.
    """

    if key in dct:
        return dct[key]
    else:
        return default
