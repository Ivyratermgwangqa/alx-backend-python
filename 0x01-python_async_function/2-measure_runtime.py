#!/usr/bin/env python3
"""
Module that defines a function to run multiple coroutines concurrently
"""
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn `n` instances of `wait_random` and return the delays in ascending order.
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
