#!/usr/bin/env python3
import asyncio
from typing import List
from 0-basic_async_syntax import wait_random  # Importing from 0-basic_async_syntax

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `n` instances of `wait_random` and returns the delays in ascending order.

    Args:
        n (int): Number of times to spawn `wait_random`.
        max_delay (int): Maximum delay time.

    Returns:
        List[float]: Sorted list of delays.
    """
    delays = await asyncio.gather(*[wait_random(max_delay) for _ in range(n)])
    return sorted(delays)  # Returns sorted list of delays
