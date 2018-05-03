#!/usr/bin/env python3

# Created on 4/25/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Demonstrate a simple two state finite state machine
from enum import Enum

class state_type(Enum):
    state_off = "Light turned off."
    state_on = "Light turned on."

class state_machine:

	def __init__(self, initial_state):
		self.state = initial_state

	def current_state(self):
		if self.state == state_type.state_on:
			return state_type.state_on.value

		if self.state == state_type.state_off:
			return state_type.state_off.value

def main():
	light = state_machine(state_type.state_off)
	print("The light is currently: {0}".format(light.current_state()))

main()