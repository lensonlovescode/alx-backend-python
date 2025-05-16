#!/usr/bin/env python3
"""
Imports wait_random from the previous python file and writes
an async routine that spawns wait_random n times with the specified max_delay
"""
from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with a specific max_delay
    """
    listio = []
    for i in range(n):
        listio.append(await task_wait_random(max_delay))

    return sorted(listio)
