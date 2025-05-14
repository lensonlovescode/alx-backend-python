#!/usr/bin/env python3
"""
Annotates the below function’s parameters
and returns values with the appropriate types
"""
from typing import Iterable, Sequence, Any, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    the function to be annotated
    """
    return [(i, len(i)) for i in lst]
