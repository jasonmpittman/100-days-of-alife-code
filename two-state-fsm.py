#!/usr/bin/env python3

# Created on 4/25/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: Demonstrate a simple two state finite state machine
from enum import Enum
import time
import random

class state_type(Enum):
    state_off = "the light is turned off."
    state_on = "the light is turned on."

class state_machine:

	def __init__(self, initial_state):
		self.state = initial_state

	def current_state(self):
		if self.state == state_type.state_on:
			return state_type.state_on.value

		if self.state == state_type.state_off:
			return state_type.state_off.value

	def update_state(self, state):
		if state == state_type.state_on:
			self.state = state_type.state_off
				
		if state == state_type.state_off:
			self.state = state_type.state_on

def main():
	light = state_machine(state_type.state_off)
	print("Light is starting off")

	while True:
		try:
			flip = random.randint(0,1)		

			if flip == 0:
				light.update_state(state_type.state_off)
			
			if flip == 1:
				light.update_state(state_type.state_on)

			print("The light is currently: {0}".format(light.current_state()))
			time.sleep(5)
		except EOFError:
			break

main()