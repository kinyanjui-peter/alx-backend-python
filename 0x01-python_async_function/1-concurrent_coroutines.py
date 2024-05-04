#!/usr/bin/env python3
"""
 return the list of all the delays (float values). The list of the delays
 should be in ascending order without using sort() because of concurrency.
 args:
    int: n
    int: max_delay
 Return:
    float: averageTime
 """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawn wait_random n times"""
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
