#!/usr/bin/env python3
"""
Create a measure_time function with integers n and max_delay as
arguments that measures the total execution time for wait_n(n,
max_delay), and returns total_time / n. Your function should
return a float.

args:
    int: n
    int: max_delay

Return:
    float: averageTime
"""
import asyncio
wait_n = __import__ ('1-concurrent_coroutines').wait_n
import time


async def measure_time(n: int, max_delay: int) -> float:
    startTime = time.time()
    resuilts = await wait_n(n, max_delay)
    endTime = time.time
    totalTime = endTime - startTime
    averageTime = totalTime / n
    return  averageTime

if __name__ == "__main__":
    import sys
