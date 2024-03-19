#!/usr/bin/env python3
import asyncio
import random

"""
coroutine called async_generator that takes no arguments.

The coroutine will loop 10 times, each time asynchronously
wait 1 second, then yield a random number between 0 and 10.
Use the random module.

"""


async def async_generator():
    # loop 10 times
    for i in range(10):
        # each loop wait for 1 sec
        await asyncio.sleep(1)
        randomNumber = random.uniform(0, 10)
        yield(randomNumber)
