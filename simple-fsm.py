#!/usr/bin/env python3

# Created on 05/01/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: example of a simple finite state machine with a text-based game agent
# Explanation:
from enum import Enum
import time
import random

class state_type(Enum):
    state_run = "Run Away"
    state_patrol = "Patrol"
    state_attack = "Attack"

class enemy_type(Enum):
    state_strong = "I'm a strong enemy"
    state_weak = "I'm a weak enemy"
    state_present = "I'm an enemy"
    state_missing = "There is no enemy"

class simple_agent:

    def __init__(self, initial_state):
        self.state = initial_state

    def current_state(self):
        return self.state

    def change_state(self, state, enemy_state):
        if state == state_type.state_patrol:
            if enemy_type.state_strong:
                self.state = state_type.state_run
            elif enemy_type.state_weak:
                self.state = state_type.state_attack
            elif enemy_state.state_missing:
                self.state = state_type.state_patrol        
        #elif state == state_type.state_run:
            #if enemy_type.state_present:
            #    self.state = state_type.state_run
            #elif enemy_type.state_missing:
            #    self.state = state_type.state_patrol
        elif state == state_type.state_attack:
            if enemy_type.state_strong:
                self.state = state_type.state_run
            elif enemy_type.state_weak:
                self.state = state_type.state_patrol

    def run(self, enemy_strong):
        #do run
        if enemy_strong == True:
            print("Running away...")
        
        if enemy_type.state_present:
            self.state = state_type.state_run
        elif enemy_type.state_missing:
            self.state = state_type.state_patrol

    def patrol(self, enemy_present):
        #do patrol
        if enemy_present == False:
            print("Patroling...")
        elif enemy_present == True:
            print("Oh no! Enemy is here...")

    def attack(self, enemy_weak):
        #do attack
        if enemy_weak == True:
            print("Attacking...")
        else:
            self.run(True)

def is_enemy_present():
    present = random.randint(0,1)

    if present == 0:
        presence = False
    elif present == 1:
        presence = True

    return presence

def main():
    #create the agent object and set default state to patrol
    agent = simple_agent(state_type.state_patrol)

    #loop until we quit
    while True:
        try:
            if agent.current_state() == state_type.state_patrol:
                agent.patrol(is_enemy_present())
                agent.change_state(agent.current_state, enemy_type.state_weak)
                
            time.sleep(5)
        except EOFError:
            break

main()