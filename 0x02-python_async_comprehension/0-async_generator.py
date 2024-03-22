#!/usr/bin/env python3
import asyncio
import random
# from list import generator


async def async_generator() #-> float #generator[float, None, None]:
    # """
    # coroutine called async_generator that takes no arguments.

    # The coroutine will loop 10 times, each time asynchronously
    # wait 1 second, then yield a random number between 0 and 10.
    # Use the random module.

    # Yields:
    #     float: A random float between 0 and 10
    #  """
    for i in range(10):
        # each loop wait for 1 sec
        await asyncio.sleep(1)
        randomNumber = random.uniform(0, 10)
        yield(randomNumber)
