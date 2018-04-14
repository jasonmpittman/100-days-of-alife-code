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
	ruleNum = 1
	while True:
		try:
			print('Enter the antecendent of rule {0}'.format(ruleNum))
			antecedents.append(input('> '))

			print('Enter the subsquent of rule {0}'.format(ruleNum))
			subsequents.append(input('> '))

			ruleNum += 1
		except EOFError:
			break
	
def print_rules():
	print(rules)
	print(antecedents) 
	print(subsequents)

#where an entry in the system matches an antecedent, change it to the corresponding subsequent
def processsystem():
	del tempSystem[:]
	global system

	for s in system:
		pos = 0
		for a in antecedents:
			if s == a:
				tempSystem.append(subsequents[pos])
			pos += 1

	system = ''.join(tempSystem)
	print('system is {0}'.format(system)) 

process_rules()

if seed == "empty":
	print("Please enter the seed for the system.")
	seed = input('> ')
	system = seed

#need 'main' loop for generator
while repeat:

	print("Would you like to generate the next sequence in the system? [Y]es or [N]o: ")
	choice = input()

	if choice == "Y":
		processsystem()
		print("Continuing...")
	else:
		print("Ending..")
		repeat = False






