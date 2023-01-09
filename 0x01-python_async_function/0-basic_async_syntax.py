#!/usr/bin/env python3
"""
Basic async module.

Contains function wait_random
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """that takes in an integer argument and waits for a random delay. """
    rand: float = random.randint(0, max_delay)
    await asyncio.sleep(rand)
    return rand
