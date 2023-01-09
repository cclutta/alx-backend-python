#!/usr/bin/env python3
"""
Concurrent module.

Contains function task_wait_n
"""
from typing import List
from asyncio import gather

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """will spawn wait_random n times with the specified max_delay. """
    return sorted(
        await gather(*[task_wait_random(max_delay) for i in range(n)]))
