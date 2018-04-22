#!/usr/bin/env python3

# Created on 4/15/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: generate basic graphical L-Systems based rule, seed, and generations input
# Explanation: https://en.wikipedia.org/wiki/L-system
import turtle

system = []
antecedents = []
subsequents = []
seed = "empty"
angle = 60
distance = 5
#generations = 0

def drawLSystem(myTurtle, angle, distance):
    #system = 'A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A-A-A++A-A-A-A++A-A++A-A++A-A-A-A++A-A'
    global system
    for element in system:
        #forward
        if element == "A":
            myTurtle.forward(distance)
        #backward
        if element == "B":
            myTurtle.backward(distance)
        #left
        if element == "+":
            myTurtle.right(angle)
        #right
        if element == "-":
            myTurtle.left(angle)

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

def process_seed():
    global seed
    while True:
        try:
            print('Enter the seed for the system')
            seed = input('> ')
    
        except EOFError:
            break
'''    
def process_generations():
    global generations
    while True:
        try:
           print('Enter the number of generations to process')
           generations = input('> ')
        except EOFError:
            break
'''
def main():
    global system

    #get the rules
    process_rules()
    
    #get the seed
    process_seed()

    system = seed

    #get the number of generations
    #process_generations()

    #create the turtle
    tort = turtle.Turtle()
    screen = turtle.Screen()

    tort.up()
    tort.back(200)
    tort.down()
    tort.speed(9)

    #intialize the L-System
    drawLSystem(tort, angle, distance)

    screen.exitonclick()
        
main()