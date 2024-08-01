#!/usr/bin/env python3
"""
Add type annotations to the function
"""
from typing import Mapping, Any, Union, TypeVar, Optional

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default:
                     Optional[T] = None) -> Union[Any, T]:
    """Return dct if key in dct else None"""
    if key in dct:
        return dct[key]
    else:
        return default
