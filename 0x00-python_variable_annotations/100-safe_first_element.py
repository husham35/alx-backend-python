#!/usr/bin/env python3
"""
Augmenting a function with the correct duck-typed annotations.
"""
from typing import Any, Union, Sequence


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the types of the elements of the input"""
    if lst:
        return lst[0]
    else:
        return None
