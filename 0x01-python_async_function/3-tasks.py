#!/usr/bin/env python3
"""
Module that defines a function to create asyncio tasks.
"""
import asyncio
import importlib

# Dynamically import `wait_random` from `0-basic_async_syntax`
wait_random = importlib.import_module("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task wrapping `wait_random`.

    Args:
        max_delay (int): Maximum delay time.

    Returns:
        asyncio.Task: An asyncio task representing the coroutine.
    """
    return asyncio.create_task(wait_random(max_delay))
