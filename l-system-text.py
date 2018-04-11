#!/usr/bin/env python

# Created on 4/11/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate text-based L-Systems based on rule and seed input
# Explanation: https://en.wikipedia.org/wiki/L-system

import sys

rules = []

print("Please enter rules in the format of A -> B one at a time. Use Ctrl+Z and Enter to end rule input.")
while True:
	try:
		rules.append(input('> '))
	except EOFError:
		break




#def process_rules():


#def get_seed():


