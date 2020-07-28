# fastlife.sequential
# Implements a Game of Life cellular automata in a single, sequential process.
#
# Author:   Benjamin Bengfort <benjamin@bengfort.com>
# Created:  Mon Jul 27 14:02:53 2020 -0400
#
# Copyright (C) 2020 Bengfort.com
# For license information, see LICENSE
#
# ID: sequential.py [] benjamin@bengfort.com $

"""
Implements a Game of Life cellular automata in a single, sequential process.
"""

##########################################################################
## Imports
##########################################################################

import gzip
import numpy as np
import matplotlib.pyplot as plt

from tqdm import tqdm
from matplotlib.animation import FuncAnimation

from .grid import Grid
from .exceptions import FastlifeError


##########################################################################
## Sequential Life Simulation
##########################################################################


class SequentialLife(object):

    def __init__(self, width=512, height=512):
        # Game of Life has two frames, one for the current timestep and one for the next
        # TODO: load initial state
        self.initialized = False
        self.frames = [Grid(width, height), Grid(width, height)]
        self.frame = 0
        self.now = 0

    @property
    def cframe(self):
        return self.frames[self.frame]

    @property
    def nframe(self):
        return self.frames[1-self.frame]

    def load(self, path):
        """
        Load the simulation from a file on disk.
        """
        grid = self.frames[self.frame]
        with gzip.open(path, 'rb') as f:
            for line in f:
                i, j = tuple(map(int, line.split()))
                grid[i,j] = 1

        self.initialized = True

    def randomize(self, seed=None):
        """
        Create a random initial state from a seed value.
        """
        np.random.seed(seed)
        grid = self.cframe
        grid._world = np.random.randint(2, size=grid.shape)
        self.initialized = True

    def step(self):
        """
        Execute the next step in the simulation and swap the current grid.
        """
        cframe = self.cframe
        nframe = self.nframe

        im, jm = cframe.shape
        for i in range(im):
            for j in range(jm):
                # This is the fastest way to accumulate the number of neighbors.
                ngbrs = cframe.neighborhood_sum(i,j)

                if cframe[i,j] == 1:
                    # Living cell - does it survive or die?
                    if ngbrs < 2 or ngbrs > 3:
                        nframe[i,j] = 0
                    else:
                        nframe[i,j] = 1
                else:
                    # Unoccupied cell - does it get born?
                    if ngbrs == 3:
                        nframe[i,j] = 1
                    else:
                        nframe[i,j] = 0


        # Swap the current frame to the next frame and increment the number of steps
        self.now += 1
        self.frame = 0 if self.frame == 1 else 1

    def run(self, steps=100, progress=True):
        """
        Run the simulation for the specified number of steps from the current state.
        """
        if not self.initialized:
            raise FastlifeError("the game of life simulation has not been initialized")

        if progress:
            for _ in tqdm(range(steps)):
                self.step()
        else:
            for _ in range(steps):
                self.step()

    def animate(self, steps=100):
        """
        Animate the simulation for the specified number of steps.
        """
        if not self.initialized:
            raise FastlifeError("the game of life simulation has not been initialized")

        fig, ax = plt.subplots(figsize=(8,8))
        def plot_frame(idx):
            self.step()
            self.cframe.plot(ax)
            ax.set_title(f"Timestep {self.now}")

        _ = FuncAnimation(
            fig, plot_frame, frames=np.arange(steps),
            repeat=False, init_func=lambda: self.cframe.plot(ax),
        )
        plt.show()
