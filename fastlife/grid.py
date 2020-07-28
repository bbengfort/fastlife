# fastlife.grid
# A wrapper for the matrix that describes the game of life grid world.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 26 12:12:30 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: grid.py [] benjamin@bengfort.com $

"""
A wrapper for the matrix that describes the game of life grid world.
"""

##########################################################################
## Imports
##########################################################################

import numpy as np
import matplotlib.pyplot as plt

from .exceptions import FastlifeValueError, FastlifeTypeError


VON_NEUMANN = "von neumann"
MOORE = "moore"

VNIP = np.asarray([-1, 0, 1, 0])
VNJP = np.asarray([0, 1, 0, -1])
MRIP = np.asarray([-1, -1, 0, 1, 1, 1, 0, -1])
MRJP = np.asarray([0, 1, 1, 1, 0, -1, -1, -1])


class Grid(object):
    """
    The game of life world is a 2-dimensional grid that is represented by a numpy matrix
    whose cells are False (dead) or True (alive). The grid provides wrapper functions
    for neighborhood calculations, partitioning, and other operations required for
    parallel implementations of cellular automata.

    Parameters
    ----------
    width, height : int
        The shape of the underlying grid world.

    adjacency : str, default: "moore"
        The type of neighborhood, either "von neumann" or "moore"
    """

    __slots__ = ["_world", "_adjacency"]

    def __init__(self, width=100, height=100, adjacency=MOORE):
        self._world = np.zeros((height, width), dtype=np.int8)
        self.adjacency = adjacency

    @property
    def adjacency(self):
        return self._adjacency

    @adjacency.setter
    def adjacency(self, val):
        val = val.lower().replace("_", " ").strip()
        if val != MOORE and val != VON_NEUMANN:
            raise FastlifeValueError(f"'{val}' is not a valid adjacency")
        self._adjacency = val

    @property
    def shape(self):
        return self._world.shape

    def neighborhood(self, i, j):
        """
        Returns the neighborhood of the cell specified at the x, y coords as a generator
        of values that the caller can iterate over. This mechanism is the fastest way
        to collect all of the individual values of the neighbors. Note that neighbors
        are returned from the top neighbor (e.g. the neighbor directly above) clockwise.

        Parameters
        ----------
        i, j : int
            The position of the cell in the world to get the neighbors for.
        """
        ip, jp = (MRIP, MRJP) if self.adjacency == MOORE else (VNIP, VNJP)

        for id, jd in zip(ip, jp):
            try:
                yield self._world[i+id,j+jd]
            except IndexError:
                yield 0

    def neighborhood_sum(self, i, j):
        """
        Returns the sum of all cells in the neighborhood of i,j without yielding them
        as a generator. This is the fastest performing method to get the total number of
        neighbors if the cellular automata uses 1s and 0s for state.

        Parameters
        ----------
        i, j : int
            The position of the cell in the world to get the neighbors for.
        """
        total = 0
        ip, jp = (MRIP, MRJP) if self.adjacency == MOORE else (VNIP, VNJP)

        for id, jd in zip(ip, jp):
            try:
                total += self._world[i+id,j+jd]
            except IndexError:
                continue
        return total

    def neighborhood_array(self, i, j):
        """
        Returns the neighborhood of the cell specified at the x, y coords as a numpy
        array whose shape is determined by the adjacency. Note that this is not as fast
        as using the generator or sum methods above and should only be used if more
        extensive computations are required for the neighborhood array. Neighbors are
        returned from the top neighbor (e.g. the neighbor directly above) clockwise.

        Parameters
        ----------
        i, j : int
            The position of the cell in the world to get the neighbors for.
        """
        if self.adjacency == MOORE:
            ip, jp = MRIP, MRJP
            vals= np.zeros(8)
        else:
            ip, jp = VNIP, VNJP
            vals = np.zeros(4)

        im, jm = self._world.shape
        for v, (id, jd) in enumerate(zip(ip, jp)):
            ic, jc = i+id, j+jd
            if ic >= 0 and jc >=0 and ic < im and jc < jm:
                vals[v] = self._world[ic,jc]

        return vals

    def plot(self, ax=None):
        if ax is None:
            _, ax = plt.subplots(figsize=(8,8))
        ax.imshow(self._world, aspect="equal")
        ax.set_xticks([])
        ax.set_yticks([])
        return ax

    def __getitem__(self, ij):
        if not isinstance(ij, tuple) or len(ij) != 2:
            raise FastlifeTypeError("specify i, j position as a two-tuple")
        return self._world[ij[0], ij[1]]

    def __setitem__(self, ij, val):
        if not isinstance(ij, tuple) or len(ij) != 2:
            raise FastlifeTypeError("specify i, j position as a two-tuple")

        if not isinstance(val, (int, np.int8)) or val > 127 or val < -128:
            raise FastlifeValueError("invalid game of life value")
        self._world[ij[0], ij[1]] = val
