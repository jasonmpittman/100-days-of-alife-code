#!/usr/bin/env python

# Created on 4/11/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate text-based L-Systems based on rule and seed input
# Explanation: https://en.wikipedia.org/wiki/L-system

import sys
import re

rules = []
antecedents = []
subsequents = []
seed = "empty"
system = "empty"
tempSystem = []
repeat = True

def process_rules():
	antecedents, subsequents = zip(*(r.split(" -> ") for r in rules))
	
def print_rules():
	print(antecedents) 
	print(subsequents)

#where an entry in the system matches an antecedent, change it to the corresponding subsequent
def process_system(system):
	for rule in rules:
		for element in system:
			tempSystem.append(re.sub(r'element', 'rule'))

print("Please enter rules in the format of A -> B one at a time. Use Ctrl+Z and Enter to end rule input.")
while True:
	try:
		rules.append(input('> '))
	except EOFError:
		break
process_rules()

print("Please enter the seed for the system.")
seed = input('> ')

#need 'main' loop for generator
while repeat:
	print("Would you like to generate the next sequence in the system? [Y]es or [N]o: ")
	choice = input()

	if choice == "Y":
		#process the system
	else:
		repeat = False





