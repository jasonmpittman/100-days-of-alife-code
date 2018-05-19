#!/usr/bin/env python3

# Created on 05/17/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: simple agent 'brain' output of flocking behavior
# Explanation:
import random
import time
from enum import Enum

num_agents = 2
agents = []
running = True

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
        print("Agent {0} is at {1} {2} facing {3}".format(self.agent_id, self.x, self.y, self.facing))

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
            agent.distance = 1
        
    def move_away(self):
        if self.x and self.y < 4:
            self.x += 1
            self.y += 1

    def move_closer(self): 
        if self.x and self.y > 4:
            self.x -= 1
            self.y -= 1      

def elect_leader():
    leader_index = random.randint(0, num_agents - 1)
    return leader_index
    
def main():
    face = facing.north.value
    followers = []
    leader = []
    lead_agent = elect_leader()

    for i in range(num_agents):
        agents.append(agent(random.randint(1,20), random.randint(1,20), i, face))

    #separate agents into leader and followers
    leader = agents[lead_agent]
    agents.pop(lead_agent)
    followers = agents


    while running:
        for follower in followers:
            follower.get_position()
            
            time.sleep(3)
        
        leader.get_position()
        #if distance between agents is 'big', move closer.
        #if distance between agents is 'small', move away.
        #otherwise, just move together 

main()