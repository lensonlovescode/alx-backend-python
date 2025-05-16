#!/usr/bin/env python3
"""
Contains a coroutine that executes async_comprehension four times in
parallel using asyncio.gather and measure the total runtime and return it.
"""
import time
import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures runtime for executing async_comprehension
    """
    timenow = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension(), async_comprehension())
    return time.perf_counter() - timenow
