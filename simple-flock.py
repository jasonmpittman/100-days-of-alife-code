#!/usr/bin/env python3

# Created on 05/07/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of two agent flocking behavior
# Explanation:

import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((640,800))
clock = pygame.time.Clock()

stopped = False

while not stopped:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stopped = True
    
        print(event)
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()