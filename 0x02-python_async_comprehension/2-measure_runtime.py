#!/usr/bin/env python3
"""
This module defines a coroutine to measure runtime for asynchronous tasks.

The `measure_runtime` coroutine measures the total runtime for executing the 
`async_comprehension` coroutine four times in parallel, using `asyncio.gather`.
"""

import asyncio
from time import time
from 1-async_comprehension import async_comprehension


async def measure_runtime() -> float:
    """Measure the total runtime for executing async_comprehension four times in parallel"""
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    return end_time - start_time
