#!/usr/bin/env python3
"""
Contains an asynchronous coroutine that takes in an integer argument  with
a default value of 10 that waits for a random delay between 0 and max_delay
(included and float value) seconds and eventually returns it
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    waits for a random time period between o and max_delay and returns it
    """
    wait = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
