#!/usr/bin/env python3
"""
This module measures the runtime of multiple asynchronous comprehensions.
"""

import asyncio
from time import time
import importlib  # Dynamic import to handle module names with dashes

# Importing the `async_comprehension` coroutine
async_comprehension = importlib.import_module("1-async_comprehension").async_comprehension

async def measure_runtime() -> float:
    """Measure total runtime for executing async_comprehension 4times parallel"""
    start_time = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end_time = time()
    return end_time - start_time
