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

max_velocity = 10
num_agents = 2
agents = []

class agent:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocityX = random.randint(1,10) / 10.0
        self.velocityY = random.randint(1,10) / 10.0

    def update_pos(self, x, y):
        self.x = x
        self.y = y
'''
    def away(self, agents, min_distance):
        if len(agents) < 1:
            return
        
        distance_x = 0
        distance_y = 0
        num_close = 0

        for agent in agents:
            distance = self.distance(agent) 
    
    def move(self):
        self.x += self.velocityX
        self.y += self.velocityY
'''

screen = pygame.display.set_mode((window_width,window_height))
clock = pygame.time.Clock()

for i in range(num_agents):
    agents.append(agent(random.randint(0, window_width), random.randint(0, window_height)))


def main():
    block_size = 10
    stopped = False
    velocity = [1, 1]
    #x = window_width / 2
    #y = window_height / 2

    while not stopped:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill((0,0,0))
        
        for agent in agents:
            agent = pygame.draw.rect(screen, white, [agent.x, agent.y, block_size, block_size])

            agent.x += velocity[0]
            agent.y += velocity[1]

            if agent.x + block_size > window_width or agent.x < 0:
                velocity[0] = -velocity[0]
            
            if agent.y + block_size > window_height or agent.y < 0:
                velocity[1] = -velocity[1]


        pygame.display.update()
        clock.tick(60)

main()