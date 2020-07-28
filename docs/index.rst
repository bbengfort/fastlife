.. -*- mode: rst -*-
.. Fastlife documentation master file, created by
   sphinx-quickstart on Sun Jul 26 09:24:01 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Fast Life
=========

Fast Life is an experiment in Python simulation performance. Python has many excellent simulation frameworks including `SimPy <https://simpy.readthedocs.io/en/latest/>`_ and `MESA <https://mesa.readthedocs.io/en/master/index.html>`_, which make it easy to conduct simulations for research and experimental purposes. Fast Life is not intended to be a simulation framework in the same way, instead Fast Life is designed to answer the question: "Can Python be used to create extremely large scale simulations"? To this end, Fast Life implements a seemingly simple simulation: `Conway's Game of Life <https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life>`_ -- but scales it up to massive proportions. We then explore several different implementations including:

1. Pure Python Sequential
2. Pure Python Multiprocessing
3. C-bindings Sequential
4. C-bindings Parallel

And run benchmarks to see what is the simplest mechanism to combine the ease of Python programming with the performance required to generate massive worlds. All implementations are designed with the best effort in mind, using numpy where possible and where it enhances performance, and details matter with function profiling and more.

This work is still in progress and is a bit of a journey. If you're reading this, stay tuned, there is more coming! If you're interested in contributing, we'd also be happy to have you join, let us know how you'd like to participate!

Table of Contents
-----------------

.. toctree::
   :maxdepth: 2

   notes/index
   api/index


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
