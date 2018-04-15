#!/usr/bin/env python3

# Created on 4/15/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate basic graphical L-Systems based rule, seed, and generations input
# Explanation: https://en.wikipedia.org/wiki/L-system
from turtle import *

system = []

def drawLSystem():
	global system
	for s in system:
		#forward
		#backward
		#left
		#right

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

def main:
	#get the rules
	#get the seed
	#get the number of generations
	#create the turtle

	#intialize the L-System
	#draw the complete system for n generations

main()