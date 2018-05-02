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

    def __init__(self, initial_state):
        self.state = initial_state

    def current_state(self):
        return self.state

    def change_state(self, state):
        #change agent state from current to new
        print("Changing state to {0}".format(state))
        self.state = state

    def run(self, enemy_strong):
        #do run
        if enemy_strong == True:
            print("Running away...")

    def patrol(self, enemy_present):
        #do patrol
        print("Patroling...")

    def attack(self, enemy_weak):
        #do attack
        if enemy_weak == True:
            print("Attacking...")
        else:
            self.run(True)
'''
def update_state(agent, current_state):
    if current_state == state_type.state_run:
        #run()
    elif current_state == state_type.state_patrol:
        #patrol()
    elif current_state == state_type.state_attack:
        #attack()
'''
def main():
    #create the agent object
    agent = simple_agent(state_type.state_patrol)

    #loop until we quit
    while True:
        try:
            agent.patrol
        except EOFError:
            break


main()