#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""
# wait_n = __import__("1-concurrent_coroutines").wait_n
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    tasks = []  # List to store asyncio tasks
    results = []  # List to store results

    # Create tasks for wait_random
    for _ in range(n):
        # Create task for wait_random
        task = asyncio.create_task(task_wait_random(max_delay))
        tasks.append(task)  # Add task to the list

    # Gather results from completed tasks
    for task in tasks:
        result = await task  # Await the task to get the result
        results.append(result)  # Add result to the list
    return results
