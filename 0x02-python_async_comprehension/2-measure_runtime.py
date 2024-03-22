#!/usr/bin/env python3
"""
This coroutine function that will execute async_comprehension four times
in parallel using asyncio.gather.
"""
import asyncio
import random
import datetime import timedelta
from typing import Generator
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> timedelta:
    """  A ffunction taht return async comprehension and time"""
    startTime = time.time()
    allTask = await asyncio.gather(async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension(),
                                   async_comprehension())
    endTime = time.time()
    timeConsumed = endTime - startTime
    return timeConsumed
