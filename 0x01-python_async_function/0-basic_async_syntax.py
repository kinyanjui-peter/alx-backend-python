#!/usr/bin/python3
import asyncio
import random

"""asynchronous coroutine that takes in an integer argument (max_del00ay,
    with a default value of 10) named wait_random that waits for a random
    delay between 0 and max_delay (included and float value) seconds and
    eventually returns it.

    args:
        float: max_delay
    Returns:
        float: delayTime
    """


async def wait_random(max_delay=10):
    delayTime = random.uniform(0, max_delay)
    await asyncio.sleep(delayTime)
    return delayTime
