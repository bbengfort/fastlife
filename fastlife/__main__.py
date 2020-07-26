# fastlife
# CLI program for running fastlife benchmarks and simulations.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 26 11:30:13 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: __main__.py [] benjamin@bengfort.com $

"""
CLI program for running fastlife benchmarks and simulations.
"""

##########################################################################
## Imports
##########################################################################

import argparse

from .version import get_version
from .exceptions import ConsoleError


##########################################################################
## Module Variables
##########################################################################

PROG = "fastlife"
DESCRIPTION = "experiments in Conway's Game of Life performance"
EPILOG = "please report any bugs on GitHub issues"
VERSION = f"{PROG} v{get_version()}"


##########################################################################
## Console Commands
##########################################################################

def run(args):
    """
    Run a game of life simulation.
    """
    raise ConsoleError("not implemented yet")


def bench(args):
    """
    Run game of life benchmarks.
    """
    raise ConsoleError("not implemented yet")



##########################################################################
## Main Method and Argument Parsing
##########################################################################

def make_wide(formatter, width=120, max_help_position=42):
    """
    Increase space between arguments and help text, if possible.
    See: https://stackoverflow.com/questions/5462873/
    """
    try:
        # ensure formatter can be used
        kwargs = {"width": width, "max_help_position": max_help_position}
        formatter(None, **kwargs)

        # return function to create formatter
        return lambda prog: formatter(prog, **kwargs)
    except TypeError:
        # return originally sized formatter
        return formatter


def main():
    cmds = {
        "run": {
            "func": run,
            "description": "run a game of life simulation",
            "args": {},
        },
        "bench": {
            "func": bench,
            "description": "run game of life benchmarks",
            "args": {},
        }
    }

    parser = argparse.ArgumentParser(prog=PROG, description=DESCRIPTION, epilog=EPILOG)
    parser.add_argument("-v", "--version", action="version", version=VERSION)
    subparsers = parser.add_subparsers(title="commands")

    for cmd, cmdargs in cmds.items():
        subp = subparsers.add_parser(
            name=cmd,
            description=cmdargs["description"],
            formatter_class=make_wide(argparse.ArgumentDefaultsHelpFormatter),
        )
        subp.set_defaults(func=cmdargs["func"])

        for pargs, kwargs in cmdargs["args"].items():
            if isinstance(pargs, str):
                pargs = (pargs,)
            subp.add_argument(*pargs, **kwargs)

    args = parser.parse_args()
    if "func" in args:
        try:
            args.func(args)
        except ConsoleError as e:
            parser.error(e)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()