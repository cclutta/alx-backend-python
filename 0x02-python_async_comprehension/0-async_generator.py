#!/usr/bin/env python3
"""
Async generator module.

Contains function async_generator
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """ Looping coroutine yield a random number between 0 and 10. """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
