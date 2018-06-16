#!/usr/bin/env python3

# Created on 06/15/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: demonstrate simple 2 layer backpropogation neural network that predicts output of 0 || 1 based on three inputs of 0 || 1
# Explanation: 
import numpy as np

def sigmoid(x, deriv = False):
    if (deriv == True):
        return x*(1 - x)
    
    return 1/(1 + np.exp(-x))

x = np.array([ [0,0,1], [0,1,1], [1,0,1], [1,1,1] ])
y = np.array([[0,0,1,1]]).T

np.random.seed(1)

synapse_0 = 2*np.random.random((3,1)) - 1


for i in range(10000):
    layer_0 = x
    layer_1 = sigmoid(np.dot(layer_0, synapse_0))

    layer_1_error = y - layer_1

    layer_1_delta = layer_1_error * sigmoid(layer_1, True)

    synapse_0 += np.dot(layer_0.T, layer_1_delta)


print("\n")
print("After training: {0}".format(layer_1))