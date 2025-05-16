#!/usr/bin/env python3
"""
Contains a measure_time function with integers n and max_delay as arguments
that measures the total execution time for wait_n(n, max_delay), and returns
total_time / n. Your function should return a float.
"""
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measures the total elapsed time for executing the previous function
    """
    timenow = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - timenow

    return elapsed / n
