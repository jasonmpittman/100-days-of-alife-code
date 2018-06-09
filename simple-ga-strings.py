#!/usr/bin/env python3

# Created on 06/08/2018
# @author: Jason M. Pittman
# @license: MIT-license
# Purpose: demonstrate simple genetic algorithm to evolve a match to a given string
# Explanation: 
import random

def generate_initial_genome(genes, length):
    genome = []
    
    while length >= 1:
        genome.extend(random.sample(genes, 1))
        length -= 1
    
    return ''.join(str(g) for g in genome)

def compute_fitness(target, genome):
    return sum(1 for expected, actual in zip(target, genome)
    if expected == actual)

def mutate_genome(genome, genes):
    new_gene = random.sample(genes, 1)
    location = random.randint(0, (len(genome) - 1))
    print("Inserting new gene {0} at location {1}".format(new_gene, location))

    mutated_genome = (list(genome))
    
    mutated_genome[location] = ''.join(new_gene)

    return ''.join(str(m) for m in mutated_genome)

def main():
    genes = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    target = "Hello World"
    
    first_generation = generate_initial_genome(genes, len(target))
    fitness = compute_fitness(target, first_generation)
    mutated_genome = mutate_genome(first_generation, genes)

    print(first_generation)
    print(fitness)
    print(mutated_genome)

main()