#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields random numbers.

The `async_generator` coroutine loops 10 times, waits for 1 second asynchronously,
and yields a random floating-point number between 0 and 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yield 10 random numbers asynchronously"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
