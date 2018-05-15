#!/usr/bin/env python3

# Created on 05/07/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of multiple agent flocking behavior
# Explanation:

import pygame, sys, random, math

pygame.init()

stopped = False
window_height = 800
window_width = 600
black = (0,0,0)
white = (255,255,255)

class agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 10
        self.velocityY = 10


while not stopped:
    ev = pygame.event.get()

    for event in ev:
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            running = False