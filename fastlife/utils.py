# fastlife.utils
# Utility functions and helpers for the fastlife module
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Jul 27 16:13:03 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: utils.py [] benjamin@bengfort.com $

"""
Utility functions and helpers for the fastlife module
"""

##########################################################################
## Imports
##########################################################################

import cProfile

from pstats import Stats
from functools import wraps


try:
    import pandas as pd
except ImportError:
    pd = None


def sprofile(func):
    """
    Decorator that performs a speed/stack profile of the time spent in each function
    call from the stack below the wrapped function. Prints the results when done.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()

        result = func(*args, **kwargs)

        pr.disable()
        Stats(pr).strip_dirs().sort_stats('cumulative').print_stats(20)
        return result

    return wrapper


def load_mprofile(path, name=None):
    """
    Load a memory profile from disk for plotting and comparison.
    """
    if pd is None:
        raise ImportError("pandas is required to load the memory profile")

    ref = None
    times, values = [], []
    with open(path, 'r') as f:
        for line in f:
            if line.startswith("CMDLINE"):
                if name is None:
                    name = line.rstrip("CMDLINE").strip()

            if line.startswith("MEM"):
                parts = line.split()
                val, ts = float(parts[1]), float(parts[2])
                if ref is None:
                    ref = ts

                times.append(ts-ref)
                values.append(val)

    return pd.Series(values, index=times, name=name)
