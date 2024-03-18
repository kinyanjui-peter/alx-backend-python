#!/usr/bin/python3
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n, max_delay):
    resuilts = []
    # loop wait_random n times
    for _ in range(n):
        resuilt = await wait_random(max_delay)
        resuilts.append(resuilt)
    return resuilts
