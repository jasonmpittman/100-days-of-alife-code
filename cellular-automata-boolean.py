#!/usr/bin/env python3

# Created on 4/18/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate simple boolean cellular automata
# Explanation: 
generations = 0
seed = []
currentCA = []
ca = []

def process_seed():
    global seed

    while True:
        try:
            print('Current seed is: {0}'.format(''.join(ca)))
            print('Please enter the seed for the CA')
            ca.append(input('> '))
        except EOFError:
            break

def process_generations():
    global generations

    while True:
        try:
            print('Please enter the number of generations to run')
            generations = input('> ')
        except EOFError:
            break 

def process_cellular_automata():
    global currentCA
    global ca
    length = len(ca)
    currentCA = ca

    #process a single generation using rules
    for cell in currentCA:  

        #deal with left edge
        if currentCA.index(cell) == 0:
            leftNeighbor = len(ca) - 1
        else:
            leftNeighbor = currentCA.index(cell) - 1

        #deal with right edge
        if cell.index == len(ca) - 1:
            rightNeighbor = 0
        else:
            rightNeighbor = currentCA.index(cell) + 1

        print (currentCA.index(cell))
        print (leftNeighbor)
        print (rightNeighbor)

        #if a cell is on and both neighbors are off, turn off
        if cell == 1 and currentCA[rightNeighbor] == 0 and currentCA[leftNeighbor] == 0:
            ca[currentCA.index(cell)] == 0
        
        #if a cell is on and at least one neighbor is off, leave it be
        if cell == 1 and currentCA[rightNeighbor] == 0 or currentCA[leftNeighbor] == 0:
            ca[currentCA.index(cell)] == 1

        #if a cell is off and both neighers are on, turn it on
        if cell == 0 and currentCA[rightNeighbor] == 1 and currentCA[leftNeighbor] == 1:
            ca[currentCA.index(cell)] == 1

        #if a cell is off and at least one neighbor is on, leave it be
        if cell == 0 and currentCA[rightNeighbor] == 1 or currentCA[leftNeighbor] == 1:
            ca[currentCA.index(cell)] == 0

    #print the new CA
    print(ca)

def main():
    process_seed()
    process_generations()
    global generations

    while int(generations) > 0:

        process_cellular_automata()
        generations = int(generations) - 1

main()