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
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    resuilts = []
    # loop wait_random n times
    for _ in range(n):
        resuilt = await wait_random(max_delay)
        resuilts.append(resuilt)
    return resuilts
