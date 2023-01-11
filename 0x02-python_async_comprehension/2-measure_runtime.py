#!/usr/bin/env python3
"""
Measure runtime module.

Contains function measure runtime
"""

import asyncio
from time import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Return
    """
    start: float = time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    total_time: float = time() - start

    return total_time
