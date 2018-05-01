#!/usr/bin/env python3

# Created on 05/01/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of a simple finite state machine with a text-based game agent
# Explanation:
from enum import Enum

class state_type(Enum):
    state_run = "Run Away"
    state_patrol = "Patrol"
    state_attack = "Attack"

class simple_agent:
    
    def __init__(self, id, state):
        self.id = id
        self.state = state

    def change_state(self):
        #change agent state from current to new

def evade():
    #do evasion

def patrol():
    #do patrol

def attack():
    #do attack

def change_state():
    #do state change

def update_state(current_state):
    if current_state = state_type.state_run:
        evade()
    elif current_state = state_type.state_patrol:
        patrol()
    elif current_state = state_type.state_attack:
        attack()

def main():
    #create the agent object
    agent = simple_agent(
        1,
        state_type.state_patrol
    )

    #loop until we quit

main()