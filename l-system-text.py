#!/usr/bin/env python

# Created on 4/11/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate text-based L-Systems based on rule and seed input
# Explanation: https://en.wikipedia.org/wiki/L-system

import sys

rules = []
antecedents = []
subsequents = []
seed = "empty"

def process_rules():
	antecedents, subsequents = zip(*(r.split(" -> ") for r in rules))
	
def print_rules():
	print(antecedents) 
	print(subsequents)


print("Please enter rules in the format of A -> B one at a time. Use Ctrl+Z and Enter to end rule input.")
while True:
	try:
		rules.append(input('> '))
	except EOFError:
		break

print("Please enter the seed for the system.")
seed = input('> ')

process_rules()


