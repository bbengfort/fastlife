# Fast Life

This repository is an experiment to compare different techniques for implementing Conway's game of life to determine performance characteristics of a Python program. The implementations are as follows:

1. Pure Python Sequential
2. Pure Python Multiprocessing
3. C-bindings Sequential
4. C-bindings Parallel

Each of these implementations will be benchmarked with significantly sized worlds and the same random seeds to determine how their performance scales.
