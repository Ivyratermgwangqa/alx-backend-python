#!/usr/bin/env python3
"""
Module to run multiple coroutines concurrently.
"""
import asyncio
import importlib
import sys  # Importing `sys` module
from typing import List

# Ensure the current directory is in `sys.path`
sys.path.append('.')

# Dynamically import `wait_random`
basic_module = importlib.import_module("0-basic_async_syntax")
wait_random = basic_module.wait_random  # Assign the imported function


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` instances of `wait_random` and returns the delays
    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): Maximum delay time.

    Returns:
        List[float]: Sorted list of delays.
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
