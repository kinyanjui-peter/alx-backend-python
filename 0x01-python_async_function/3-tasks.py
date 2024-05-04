#!/usr/bin/env python 3
"""Asyncio function"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Regular function that returns an asyncio.Task object
    for the wait_random coroutine, using asyncio.create_task().
    """
    return asyncio.create_task(wait_random(max_delay))
