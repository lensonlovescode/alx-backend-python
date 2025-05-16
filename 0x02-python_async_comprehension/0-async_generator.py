#!/usr/bin/env python3
"""
Contains a coroutine called async_generator that takes no arguments.
that loop 10 times, each time asynchronously wait 1 second, then yield
a random number between 0 and 10
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    the async generator producing a random number between
    1 and 10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
