#!/usr/bin/env python3
"""
Measure runtime module.

Contains function measure_runtime
"""
from asyncio import gather
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n


async def wait_n(n: int, max_delay) -> List[float]:
    """will spawn wait_random n times with the specified max_delay. """
    return sorted(await gather(*[wait_random(max_delay) for i in range(n)]))
