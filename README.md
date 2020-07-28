# Fast Life

[![Build Status](https://travis-ci.com/bbengfort/fastlife.svg?branch=master)](https://travis-ci.com/bbengfort/fastlife)
[![codecov](https://codecov.io/gh/bbengfort/fastlife/branch/master/graph/badge.svg)](https://codecov.io/gh/bbengfort/fastlife)
[![Documentation Status](https://readthedocs.org/projects/fastlife/badge/?version=latest)](https://fastlife.readthedocs.io/en/latest/?badge=latest)

Fast Life is an experiment in Python simulation performance. Python has many excellent simulation frameworks including [SimPy](https://simpy.readthedocs.io/en/latest/) and [MESA](https://mesa.readthedocs.io/en/master/index.html), which make it easy to conduct simulations for research and experimental purposes. Fast Life is not intended to be a simulation framework in the same way, instead Fast Life is designed to answer the question: "Can Python be used to create extremely large scale simulations"? To this end, Fast Life implements a seemingly simple simulation: [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) -- but scales it up to massive proportions. We then explore several different implementations including:

1. Pure Python Sequential
2. Pure Python Multiprocessing
3. C-bindings Sequential
4. C-bindings Parallel

Each of these implementations will be benchmarked with significantly sized worlds and the same random seeds to determine how their performance scales. Please see [fastlife.readthedocs.io](https://fastlife.readthedocs.io/en/latest/) for more details and the complete write up on the documentation.

## Quick Start

Install the package and the command line tool using the Python package manager as follows:

```
$ pip install fastlife
```

Alternatively, if you're interested in development, you can download the repository, cd into it and install locally with:

```
$ git clone https://github.com/bbengfort/fastlife.git
$ cd fastlife
$ pip install -e .
```

Note that if you're developing, you should probably set up a virtualenv and all of that good stuff before doing this step. Once done, you should have a CLI script `fastlife` installed on your path, check it out as follows:

```
$ fastlife --help
```

To run a simulation and see the animated action, you would use `fastlife run -a` - you can play with the various settings and commands to see different implementations of the simulation.
