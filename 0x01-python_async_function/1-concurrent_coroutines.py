#!/usr/bin/env python3
"""
Measure runtime module.

Contains function measure_runtime
"""
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay) -> List[float]:
    """will spawn wait_random n times with the specified max_delay. """
    return sorted(await gather(*[wait_random(max_delay) for i in range(n)]))
