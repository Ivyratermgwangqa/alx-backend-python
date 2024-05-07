#!/usr/bin/env python3
"""
Module to create and run multiple asyncio tasks.
"""
import asyncio  # Move import statements to the top
from typing import List
import importlib

# Importing `task_wait_random` at the top
task_wait_random = importlib.import_module("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Creates `n` asyncio tasks and returns the delays in ascending order.

    Args:
        n (int): Number of tasks to create.
        max_delay (int): Maximum delay time.

    Returns:
        List[float]: Sorted list of delays.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
