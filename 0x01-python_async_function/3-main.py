#!/usr/bin/env python3
import asyncio
import sys
sys.path.append('.')

task_wait_random = __import__('3-tasks').task_wait_random


async def test(max_delay: int) -> float:
    task = task_wait_random(max_delay)
    await task
    return task.__class__


print(asyncio.run(test(5)))
