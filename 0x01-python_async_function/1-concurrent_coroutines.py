#!/usr/bin/env python3
"""
Module to define a function that creates and runs multiple asyncio tasks.
"""
import asyncio  # Imports at the top
from typing import List  # Imports at the top

# Importing `task_wait_random` from `3-tasks`
import importlib
task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates `n` asyncio tasks with `task_wait_random` and returns the delays.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay time.

    Returns:
        List[float]: A list of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
