#!/usr/bin/env python3
import asyncio
import sys
sys.path.append('.')

from 4-tasks import task_wait_n


n = 5
max_delay = 6
print(asyncio.run(task_wait_n(n, max_delay)))
