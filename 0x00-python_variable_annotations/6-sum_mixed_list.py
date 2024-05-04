#!/usr/bin/env python3
"""type-annotated function sum_mixed_list
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of the list as a float"""
    return float(sum(mxd_lst))
