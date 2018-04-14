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
	#print(rules)
	print(antecedents) 
	print(subsequents)

#where an entry in the system matches an antecedent, change it to the corresponding subsequent
def process_system(system):
	del tempSystem[:]
	pos = 0

	for s in system:
		#print(s)
		for a in antecedents:
			#print(a)
			if s == a:
				#print(subsequents[pos])
				#tempSystem.append(re.sub(r's', subsequents[pos], s))
				tempSystem.append(subsequents[pos])
			pos += 1

	#print(tempSystem)
	system = ''.join(tempSystem)

	print(system)

process_rules()
#print_rules()

print("Please enter the seed for the system.")
seed = input('> ')
system = seed

#need 'main' loop for generator
while repeat:

	process_system(system)

	print("Would you like to generate the next sequence in the system? [Y]es or [N]o: ")
	choice = input()

	if choice == "Y":
		#process the system
		print("Continuing...")
	else:
		print("Ending..")
		repeat = False






