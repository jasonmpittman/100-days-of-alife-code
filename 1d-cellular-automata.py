#!/usr/bin/env python3

# Created on 4/18/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate simple 1D (boolean) cellular automata
# Explanation: 

rules = {"111": '0', "110": '0', "101": '0', "000": '0', "100": '1', "011": '1', "010": '1', "001": '1'}
seed = ["0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","1","0","0","0",
		"0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0","0"]
generations = 50
ca = []

def getNextGeneration():
	global ca
	nextGeneration = ca
	position = 0

	for cell in ca:
		neighborhood = getCellNeighborhood(ca, position)
		#match neighborhood to rules and change state of current cell
		for rule in rules:
			if neighborhood == rule:
				#change the cell state based on the rule
				nextGeneration[position] = rules[rule]
		position += 1
	ca = nextGeneration

def getCellNeighborhood(c, pos):
	neighbors = []

	#if cell is left edge: left neighbor is right edge
	if pos == 0:
		leftCell = c[len(c) - 1]
		rightCell = c[pos + 1]
	#if cell is right edge: right neighbor is left edge
	elif pos == len(c) - 1:
		rightCell = c[0]
		leftCell = c[pos - 1]
	#otherwise, left is (index - 1) & right neighbor is (index + 1)
	else:
		leftCell = c[pos - 1]
		rightCell = c[pos + 1]

	neighbors = [leftCell, c[pos], rightCell]
	neighborhood = ''.join(neighbors)

	return neighborhood

def main():
	global seed
	global generations
	global ca

	ca = seed
	
	while generations != 0:
		getNextGeneration()
		print(''.join(ca))
		generations = generations - 1

	print("Done.")

main()