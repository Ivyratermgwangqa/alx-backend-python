#!/usr/bin/env python3
import asyncio
import importlib
from typing import List

sys.path.append('.')  # Ensure the current directory is in `sys.path`

# Dynamic import to avoid syntax issues
basic_module = importlib.import_module("0-basic_async_syntax")

# Import the correct function
wait_random = basic_module.wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn `n` instances of `wait_random` and return the delays.
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)
