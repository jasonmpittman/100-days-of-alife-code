#!/usr/bin/env python3

# Created on 06/11/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: demonstrate simple genetic algorithm to evolve a match to a given string
# Explanation: 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def compute_survival(x, y, universe):
    num_neighbors = np.sum(universe[x - 1 : x + 2, y - 1 : y + 2]) - universe[x, y]

    if universe[x, y] and not 2 <= num_neighbors < = 3:
        return 0
    elif num_neighbors == 3:
        return 1
    
    return universe[x, y]


universe = np.zeros((6,6))
beacon = [[1, 1, 0, 0],
        [1, 1, 0, 0],
        [0, 0, 1, 1],
        [0, 0, 1, 1]]

universe[1:5, 1:5] = beacon

plt.imshow(universe, cmap='binary')
plt.show()


