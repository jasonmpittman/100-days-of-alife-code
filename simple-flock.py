#!/usr/bin/env python3

# Created on 05/07/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of two agent flocking behavior
# Explanation:
import pygame
import sys

pygame.init()

window_height = 800
window_width = 600

screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

def main():
    block_size = 20
    block_color = (255,255,255)
    stopped = False
    velocity = [1, 1]
    x = window_width / 2
    y = window_height / 2

    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        

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