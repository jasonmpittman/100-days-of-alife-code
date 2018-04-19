#!/usr/bin/env python3

# Created on 4/18/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate simple boolean cellular automata
# Explanation: 
generations = 0
seed = []
currentCA = []

def process_seed():
    global seed

    while True:
        try:
            print('Current seed is: {0}'.format(''.join(seed)))
            print('Please enter the seed for the CA')
            seed.append(input('> '))
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
    #define rules
    #process a single generation using rules
    #print the new CA
    print('Hi')

def main():
    process_seed()
    process_generations()

main()