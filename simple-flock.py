#!/usr/bin/env python3

# Created on 05/07/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of two agent flocking behavior
# Explanation:
import pygame
import sys
import random
import math

pygame.init()

window_height = 800
window_width = 600
black = (0,0,0)
white = (255,255,255)
block_size = 10
max_velocity = 10
num_agents = 2
agents = []

class agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = 1 #random.randint(1,10) / 10.0
        self.velocityY = 1 #random.randint(1,10) / 10.0

    def move(self, x, y):
        self.x += 1
        self.y += 1

        if self.x + block_size > window_width or self.x < 0:
           self.x = -self.x
                
        if self.y + block_size > window_height or self.y < 0:
            self.y = -self.y

'''
    def away(self, agents, min_distance):
        if len(agents) < 1:
            return
        
        distance_x = 0
        distance_y = 0
        num_close = 0

        for agent in agents:
            distance = self.distance(agent) 
    
'''

screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

for i in range(num_agents):
    agents.append(agent(random.randint(0, window_width), random.randint(0, window_height)))


def main():
    #block_size = 10
    stopped = False
    #velocity = [1, 1]
    #x = window_width / 2
    #y = window_height / 2

    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,0))
        
        for agent in agents:
            agent = pygame.draw.rect(screen, white, [agent.x, agent.y, block_size, block_size])
            
        for agent in agents:
            agent.move(agent.x, agent.y)

        pygame.display.update()
        clock.tick(60)

main()