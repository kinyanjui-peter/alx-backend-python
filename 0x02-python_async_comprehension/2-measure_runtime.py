#!/usr/bin/env python3

import asyncio
import random
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    startTime = time.time()
    allTask = await asyncio.gather(async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension())
    endTime = time.time()
    timeConsumed = endTime - startTime
    return timeConsumed
