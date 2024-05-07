#!/usr/bin/env python3
"""
Module that defines a function to run multiple tasks concurrently
"""
import asyncio
from typing import List
import sys
sys.path.append('.')

from 3-tasks import task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronously spawn `n` instances of `task_wait_random`.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
