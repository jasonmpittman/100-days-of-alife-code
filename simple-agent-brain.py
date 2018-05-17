#!/usr/bin/env python3

# Created on 05/17/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: simple agent 'brain' output of flocking behavior
# Explanation:
import random
from enum import Enum

num_agents = 2
agents = []

class facing(Enum):
    north = "North"
    south = "South"
    west = "West"
    east = "East"

class agent:
    def __init__(self, x, y, agent_id, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.agent_id = agent_id
        self.distance = 0

    def get_position(self):
        print("Agent {0} is at: {1} {2}".format(self.agent_id, self.x, self.y))

    def get_facing(self):
        if self.facing == 'North':
            sprite = '^'
        
        if self.facing == 'South':
            sprite = 'v'
        
        if self.facing == 'West':
            sprite = '<'

        if self.facing == 'East':
            sprite = '>'

        return sprite

    def is_close(self):
        return True

    def calc_distance(self, agent):
        return self.distance

    def get_distance(self, agents):
        for agent in agents:
            distance = calc_distance(agent)
        
        return distance

    def move_away(self):
        if self.x and self.y < 4:
            self.x += 1
            self.y += 1

    def move_closer(self): 
        if self.x and self.y > 4:
            self.x -= 1
            self.y -= 1      

def main():

    for i in range(num_agents):
        agents.append(agent(random.randint(1,20), random.randint(1,20), i, face)) 

main()