import importlib
import asyncio
import sys
from typing import List

sys.path.append('.')  # Ensure the current directory is in `sys.path`

# Dynamic import to avoid syntax issues
basic_module = importlib.import_module("0-basic_async_syntax")

wait_random = basic_module.wait_random  # Assign the imported function
