#!/usr/bin/env python3
"""
This module zoom_array function
"""

from typing import Tuple, List, cast


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
       Returns a tuple
    """

    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(cast(Tuple, array))

zoom_3x = zoom_array(cast(Tuple, array), int(3.0))
