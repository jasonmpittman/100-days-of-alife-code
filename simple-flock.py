#!/usr/bin/env python3

# Created on 05/07/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of two agent flocking behavior
# Explanation:
import pygame
import sys
import random

class agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = random.randint(1,10) / 10.0
        self.velocityY = random.randint(1,10) / 10.0

pygame.init()

window_height = 800
window_width = 600
black = (0,0,0)
white = (255,255,255)

max_velocity = 10
num_agents = 25
agents = []

for i in range(num_agents):
    agents.append(agent(random.randint(0, window_width), random.randint(0, window_height)))

screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()


def main():
    block_size = 20
    stopped = False
    velocity = [1, 1]
    x = window_width / 2
    y = window_height / 2

    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        x += velocity[0]
        y += velocity[1]

        if x + block_size > window_width or x < 0:
            velocity[0] = -velocity[0]
        
        if y + block_size > window_height or y < 0:
            velocity[1] = -velocity[1]

        screen.fill((0,0,0))
        pygame.draw.rect(screen, block_color, [x, y, block_size, block_size])
        
        pygame.display.update()
        clock.tick(60)



main()