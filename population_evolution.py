#!/usr/bin/env python

'''
Write a program that tracks the allele frequencies of three loci in a population of 100 individuals
The program must be object oriented

- The individuals are haploid
- Each locus has two alleles
- Each allele has a fitness_score (between 0 and 1)
- Each allele in an allele pair has only slightly different fitness_score
- overall_fitness of an individual is the product of the three alleles fitness_score

- Each new generation has two phases
-- A killing phase
--- Each individual gets a death_score between 0 and 1
--- Individual dies when death_score > fitness_score
-- A reproduction phase
--- Population gets repopulated to a 100 individuals
--- Allele frequency after killing phase = allele frequency new population

Track allele frequencies of all three loci per generation
Plot allele frequencies over time
'''

import random


# dict of dict to store initial allele frequencies
initial_allele_frequencies = {
    'locus1': {'allele_a': 0.50, 'allele_b': 0.50},
    'locus2': {'allele_a': 0.50, 'allele_b': 0.50},
    'locus3': {'allele_a': 0.50, 'allele_b': 0.50}
}

# dict of dict to store fitness scores of the alleles
allele_fitness_scores = {
    'locus1': {'allele_a': 0.85, 'allele_b': 0.75},
    'locus2': {'allele_a': 0.90, 'allele_b': 0.80},
    'locus3': {'allele_a': 0.95, 'allele_b': 1.00}
}


class Individual(object):
    def __init__(self, allele_scores, allele_freqs):
        self.allele_scores = allele_scores
        self.allele_freqs = allele_freqs

    def alleles(self):
        # make a dict that maps locus to a random allele
        locus2allele = {}
        for locus in list(self.allele_scores.keys()):
            # random.choice() returns a random element from a list
            allele = random.choice(list(self.allele_scores.get(locus).keys()))
            locus2allele[locus] = allele
        return locus2allele

    def death_chance(self):
        # random.random() returns a random float between 0.0 and 1.0
        chance = random.random()
        return chance

    def fitness_score(self):
        allele_fitness_scores = []
        # get locus-to-allele mapping
        for locus, allele in self.alleles().items():
            allele_fitness_scores.append(self.allele_scores[locus][allele])
        # calculate overall fitness score
        [allele1_score, allele2_score, allele3_score] = allele_fitness_scores
        fitness_score = allele1_score * allele2_score * allele3_score
        return fitness_score


class Population(object):
    def __init__(self, popul, allele_scores):
        self.size = len(popul)
        self.allele_scores = allele_scores
        self.popul = popul
        
    def allele_frequencies(self):
        # define dict of dict with count zeros
        locus_allele_frequencies = {}
        for locus in self.allele_scores.keys():
            locus_allele_frequencies[locus] = {}
            for allele in self.allele_scores[locus].keys():
                locus_allele_frequencies[locus][allele] = 0

        # count locus-allele combinations and store in dict of dict
        for indiv in self.popul:
            for locus, allele in indiv.alleles().items():
                locus_allele_frequencies[locus][allele] += 1 / self.size
        return locus_allele_frequencies


def generate_population(size, allele_freqs):
    list_of_individuals = []
    for i in range(size):
        list_of_individuals.append(Individual(allele_fitness_scores, initial_allele_frequencies))
    p = Population(list_of_individuals, allele_fitness_scores)
    return p


def kill_phase(p_obj):
    survivors = []
    for indiv in p_obj.popul:
        if indiv.fitness_score() > indiv.death_chance():
            survivors.append(indiv)
    s = Population(survivors, allele_fitness_scores)
    return s


def reproduction_phase(p_obj):
    # the new population consist of the survivors ...
    new_population = p_obj.popul
    # ... and are complemented with new individuals
    # new indiduals get alleles based on survivor frequencies
    survs=allele_freqs = p_obj.allele_frequencies()
    popul_size = p_obj.size
    while popul_size < 100:
        new_indiv = Individual(allele_fitness_scores, survs_allele_freqs)
        new_population.append(new_indiv)
        popul_size += 1
    n = Population(new_population)
    return n

p1 = generate_population(100)
print(p1.size)
print(p1.allele_frequencies())
s1 = kill_phase(p1)
print(s1.size)
print(s1.allele_frequencies())
# [Individual(locus_allele_fitness_scores, i) for i in range(self.size)]
# def fate(self):
#     kill_chance = self.death_chance()
#     fitness_score = self.fitness_score()
#     if fitness_score > kill_chance:
#         return 'Survives'
#     else:
#         return 'Dies'


# def survivors(self):
#     survivors = []
#     for indiv in self.popul:
#         fate = indiv.fate()
#         #print('Individual number: ', str(indiv.number))
#         #print('Fate: ', fate)
#         if fate == 'Survives':
#             survivors.append(indiv)
#     return survivors

# def repopulate(self):
#     next_generation = []
#     survs = self.survivors()
#     survs_count = len(survs)
#     print(survs_count)
#     survs_allele_freqs = survs.allele_frequencies()
#     print(survs_allele_freqs)
#     return next_generation



# i1 = Individual(locus_allele_fitness_scores)
# print('Locus-to-allele mapping: ', i1.alleles())
# print('Death chance: %4.3f' % (i1.death_chance()))
# print('Fitness score: ', i1.fitness_score())
# print('Fate of this individual: ', i1.fate())