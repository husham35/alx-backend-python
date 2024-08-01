#!/usr/bin/env python3
"""
Annotating a function’s parameters and return values
with the appropriate types.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]
                   ) -> List[Tuple[Sequence, int]]:
    """Returns i and lst"""
    return [(i, len(i)) for i in lst]
