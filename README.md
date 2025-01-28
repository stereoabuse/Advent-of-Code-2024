# Advent of Code 2024

We have to find the [Chief Historian](https://adventofcode.com/2024/day/1) in time!  Currently at 34 stars for 2024.

These solutions are relatively straightforward as one expects for AoC: lots of `re` for parsing, plenty of combinatorial stuff via `itertools`, and `collections` for easier dictionaries and counters. One thing I used more than previous years is `networkx` which is useful in a range of different graph-related problems.

The only slightly unusual approach I used with the currently solved days was testing complex numbers (`1+1j`) as grid locations instead of `[row, column]`. This provided no real benefit beyond making adjacency checks and path traversal require slightly less typing.

## Solutions Overview

Day 1: Matching locations using Manhattan distance and frequency counting  
Day 2: Validating number sequences based on monotonicity and differences  
Day 3: Parsing and calculating multiplications with conditional sections  
Day 5: Graph-based sequence validation with bubble sort correction  
Day 7: Evaluating expressions with different operation combinations  
Day 8: Detecting antenna patterns using permutations and set operations  
Day 9: Two-pointer position swapping with weighted sum calculation  
Day 10: NetworkX path finding between height-based nodes  
Day 11: Recursive number transformations with memoization  
Day 13: Solving coordinate systems with linear equations  
Day 14: Tracking modular particle movement and cycle detection  
Day 15: ✅ Completed (Solution not in repository)  
Day 16: Cost-based pathfinding using priority queue  
Day 18: Grid navigation with NetworkX and path breaking  
Day 22: Iterative number transformation with modular arithmetic  
Day 23: Network analysis using triangles and clique detection  
Day 24: Boolean circuit simulation with ordered gate processing  
Day 25: Grid-based schematic compatibility comparison