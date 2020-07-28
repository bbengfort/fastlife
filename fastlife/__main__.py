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

from .utils import sprofile
from .version import get_version
from .exceptions import ConsoleError
from .sequential import SequentialLife


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
    sim = SequentialLife(args.width, args.height)
    if args.file:
        sim.load(args.file)
    else:
        sim.randomize(args.seed)

    runner = sim.animate if args.animate else sim.run
    runner = sprofile(runner) if args.profile else runner
    runner(steps=args.steps)


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
            "args": {
                ("-W", "--width"): {
                    "type": int, "default": 75, "metavar": "W",
                    "help": "the number of columns in the simulation",
                },
                ("-H", "--height"): {
                    "type": int, "default": 75, "metavar": "H",
                    "help": "the number of rows in the simulation",
                },
                ("-f", "--file"): {
                    "type": str, "default": None, "metavar": "PATH",
                    "help": "initialize the simulation from a data file",
                },
                ("-S", "--seed"): {
                    "type": int, "default": None, "metavar": "N",
                    "help": "random seed to load a randomized world with",
                },
                ("-a", "--animate"): {
                    "action": "store_true",
                    "help": "animate the progress of the simulation",
                },
                ("-P", "--profile"): {
                    "action": "store_true",
                    "help": "profile stack calls for the simulation",
                },
                ("-s", "--steps"): {
                    "type": int, "default": 150, "metavar": "T",
                    "help": "maximum number of steps to simulate",
                },
            },
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