#!/usr/bin/env python3

# Created on 06/11/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: demonstrate simple genetic algorithm to evolve a match to a given string
# Explanation: 
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def compute_survival(x, y, world):
    num_neighbors = np.sum(world[x - 1 : x + 2, y - 1 : y + 2]) - world[x, y]

    if world[x, y] and not 2 <= num_neighbors <= 3:
        return 0
    elif num_neighbors == 3:
        return 1
    
    return world[x, y]

def compute_generation(world):
    new_world = np.copy(world)

    for i in range(world.shape[0]):
        for j in range(world.shape[1]):
            new_world[i, j] = compute_survival(i, j, world)
    
    return new_world

def run_world():
    generations = 50
    world = np.zeros((6,6))
    beacon = [[1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]]

    world[1:5, 1:5] = beacon

    figure = plt.figure(dpi=200)
    plt.axis("off")
    ims = []

    for i in range(generations):

        ims.append((plt.imshow(world, cmap='binary'),))
        world = compute_generation(world)

    im_ani = animation.ArtistAnimation(figure, ims, interval=300, repeat_delay=3000, blit=True)
    #write the gif

run_world()


