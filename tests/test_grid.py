# tests.test_grid
# Tests for the grid world helper functionality.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Sun Jul 26 12:36:38 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: test_grid.py [] benjamin@bengfort.com $

"""
Tests for the grid world helper functionality.
"""

##########################################################################
## Imports
##########################################################################

import pytest
import numpy as np

from fastlife.grid import *
from fastlife.exceptions import *


class TestGrid(object):

    @pytest.mark.parametrize("adjacency", [VON_NEUMANN, MOORE])
    def test_valid_adjacency(self, adjacency):
        """
        Test case-insensitive adjacency parameter
        """
        cases = [
            adjacency, adjacency.title(), adjacency.upper(), adjacency.lower()
        ]
        for case in cases:
            try:
                Grid(adjacency=adjacency)
            except FastlifeValueError:
                pytest.fail(f"'{case}' adjacency is valid but not accepted")

    def test_invalid_adjacency(self):
        """
        Test invalid adjacency raises exception
        """
        with pytest.raises(FastlifeValueError):
            Grid(adjacency="foo")

    def test_indexing(self):
        """
        Test indexing of a grid world
        """
        grid = Grid()
        assert grid._world.sum() == 0
        assert grid[42,19] == 0

        grid[42, 19] = 1
        assert grid[42,19] == 1
        assert grid._world.sum() == 1

    def test_bad_indexing(self):
        """
        Test bad indexing
        """
        grid = Grid()
        with pytest.raises(FastlifeTypeError):
            grid["foo"]

        with pytest.raises(FastlifeTypeError):
            grid["foo"] = 32

        with pytest.raises(FastlifeValueError):
            grid[32, 78] = "foo"

        with pytest.raises(FastlifeValueError):
            grid[32, 78] = 1292

    @pytest.mark.parametrize("adjacency,expected", [
        (VON_NEUMANN, np.asarray([2, 6, 8, 4])),
        (MOORE, np.asarray([2, 3, 6, 9, 8, 7, 4, 1])),
    ])
    def test_neighborhood_internal(self, adjacency, expected):
        """
        Test neighborhood generation inside the world
        """
        grid = Grid(adjacency=adjacency)
        grid[24, 24] = 1
        grid[24, 25] = 2
        grid[24, 26] = 3
        grid[25, 24] = 4
        grid[25, 25] = 5
        grid[25, 26] = 6
        grid[26, 24] = 7
        grid[26, 25] = 8
        grid[26, 26] = 9

        assert (list(grid.neighborhood(25,25)) == expected).all()
        assert (grid.neighborhood_array(25,25) == expected).all()

    @pytest.mark.parametrize("adjacency,expected", [
        (VON_NEUMANN, np.asarray([0, 6, 8, 0])),
        (MOORE, np.asarray([0, 0, 6, 9, 8, 0, 0, 0])),
    ])
    def test_neighborhood_top_corner(self, adjacency, expected):
        """
        Test neighborhood generation on a corner
        """
        grid = Grid(adjacency=adjacency)
        grid[0, 0] = 5
        grid[0, 1] = 6
        grid[1, 0] = 8
        grid[1, 1] = 9

        assert (list(grid.neighborhood(0,0)) == expected).all()
        assert (grid.neighborhood_array(0,0) == expected).all()

    @pytest.mark.parametrize("adjacency,expected", [
        (VON_NEUMANN, np.asarray([2, 6, 0, 4])),
        (MOORE, np.asarray([2, 3, 6, 0, 0, 0, 4, 1])),
    ])
    def test_neighborhood_bottom_row(self, adjacency, expected):
        """
        Test neighborhood generation on a corner
        """
        grid = Grid(adjacency=adjacency)
        grid[98, 49] = 1
        grid[98, 50] = 2
        grid[98, 51] = 3
        grid[99, 49] = 4
        grid[99, 50] = 5
        grid[99, 51] = 6

        with pytest.raises(IndexError):
            grid[100,50] = 8

        assert (list(grid.neighborhood(99, 50)) == expected).all()
        assert (grid.neighborhood_array(99, 50) == expected).all()
