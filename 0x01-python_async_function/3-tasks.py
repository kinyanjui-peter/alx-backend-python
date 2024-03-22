#!/usr/bin/env python 3
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """
    Async routine that waits for a random d  n  elay between 0 and max_delay
    (default 10) seconds, then returns it.
    """
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task object
    for the wait_random coroutine, using asyncio.create_task().
    """
    coroutine = wait_random(max_delay)
    return asyncio.create_task(coroutine)
