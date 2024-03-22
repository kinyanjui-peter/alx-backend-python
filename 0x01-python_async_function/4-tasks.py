#!/usr/bin/python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
# wait_n = __import__("1-concurrent_coroutines").wait_n
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n, max_delay):
    resuilts = []
    # loop wait_random n times
    for _ in range(n):
        resuilt = await task_wait_random(max_delay)
        resuilts.append(resuilt)
    return resuilts
