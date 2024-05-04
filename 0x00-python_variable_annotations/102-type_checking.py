#!/usr/bin/env python3
"""Use mypy to validate the following piece of code
and apply any necessary changes.
"""

from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> List[Any]:
    """Zooms into the given tuple by repeating each item by a factor.

    Args:
        lst (Tuple[Any]): The tuple to be zoomed into.
        factor (int, optional): The zoom factor (repeats each item).
        Defaults to 2.

    Returns:
        List[Any]: The zoomed-in list.
    """
    zoomed_in: List[Any] = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array: Tuple[int, int, int] = (12, 72, 91)

zoom_2x: List[int] = zoom_array(array)

zoom_3x: List[int] = zoom_array(array, 3)
