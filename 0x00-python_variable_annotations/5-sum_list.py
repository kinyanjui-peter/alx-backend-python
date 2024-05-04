#!/usr/bin/env python3
"""type-annotated function sum_list.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''returns  sum as a float
    '''
    return float(sum(input_list))
