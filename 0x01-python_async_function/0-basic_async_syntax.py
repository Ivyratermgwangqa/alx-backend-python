#!/usr/bin/env python3
"""
Module defining a basic asynchronous coroutine.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits for a random delay and returns it.

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        float: The random delay.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
