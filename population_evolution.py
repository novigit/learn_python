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
    'locus1': {'alleleA': 0.50, 'alleleB': 0.50},
    'locus2': {'alleleA': 0.50, 'alleleB': 0.50},
    'locus3': {'alleleA': 0.50, 'alleleB': 0.50}
}

# dict of dict to store fitness scores of the alleles
allele_fitness_scores = {
    'locus1': {'alleleA': 0.60, 'alleleB': 0.90},
    'locus2': {'alleleA': 0.90, 'alleleB': 0.60},
    'locus3': {'alleleA': 0.90, 'alleleB': 0.90}
}


class Individual(object):
    def __init__(self, allele_scores, allele_freqs):
        self.allele_scores = allele_scores
        self.allele_freqs = allele_freqs

    def alleles(self):
        # make a dict that maps locus to a random allele
        locus2allele = {}
        for locus in self.allele_freqs.keys():
            # random.choices() returns a list of one or more elements
            # from a list where each element has a defined probability
            allele_names = list(self.allele_freqs.get(locus).keys())
            allele_weights = list(self.allele_freqs.get(locus).values())
            allele = random.choices(population=allele_names, weights=allele_weights, k=1)[0]
            locus2allele[locus] = allele
        return locus2allele

    def death_chance(self):
        # random.random() returns a random float between 0.0 and 1.0
        chance = random.random()
        return chance

    def fitness_score(self):
        allele_scores = []
        # get locus-to-allele mapping
        for locus, allele in self.alleles().items():
            allele_scores.append(self.allele_scores[locus][allele])
        # calculate overall fitness score
        [allele1_score, allele2_score, allele3_score] = allele_scores
        fitness_score = allele1_score * allele2_score * allele3_score
        return fitness_score


class Population(object):
    def __init__(self, popul):
        self.size = len(popul)
        self.popul = popul

    def allele_frequencies(self):
        # define dict of dict with count zeros
        locus_allele_frequencies = {}
        for locus in ['locus1', 'locus2', 'locus3']:
            locus_allele_frequencies[locus] = {}
            for allele in ['alleleA', 'alleleB']:
                locus_allele_frequencies[locus][allele] = 0

        # count locus-allele combinations and store in dict of dict
        for indiv in self.popul:
            for locus, allele in indiv.alleles().items():
                locus_allele_frequencies[locus][allele] += 1 / self.size
        return locus_allele_frequencies


def generate_population(size, allele_freqs):
    list_of_individuals = []
    for i in range(size):
        list_of_individuals.append(Individual(allele_fitness_scores, allele_freqs))
    p = Population(list_of_individuals)
    return p


def kill_phase(p_obj):
    survivors = []
    for indiv in p_obj.popul:
        if indiv.fitness_score() > indiv.death_chance():
            survivors.append(indiv)
    s = Population(survivors)
    return s


def reproduction_phase(p_obj):
    # the new population consist of the survivors ...
    new_population = p_obj.popul
    # ... and are complemented with new individuals
    # new indiduals get alleles based on survivor frequencies
    survs_allele_freqs = p_obj.allele_frequencies()
    popul_size = p_obj.size
    while popul_size < 100:
        new_indiv = Individual(allele_fitness_scores, survs_allele_freqs)
        new_population.append(new_indiv)
        popul_size += 1
    n = Population(new_population)
    return n


def run_evolution(init_popul, generations):
    # generation counter
    i = 0
    # list of dicts to store freqs per generation in:
    allele_frequencies_per_generation = []
    # start with first generation
    popul = init_popul
    while i < generations:
        # first the kill phase:
        surv_popul = kill_phase(popul)
        # then reproduction phase:
        new_popul = reproduction_phase(surv_popul)
        # report new allele frequencies
        new_allele_freqs = new_popul.allele_frequencies()
        allele_frequencies_per_generation.append(new_allele_freqs)
        popul = new_popul
        i += 1
    return allele_frequencies_per_generation


p1 = generate_population(100, initial_allele_frequencies)
gens = run_evolution(p1, 200)
# for gen in gens:
#     print(gen)

# plot results
import matplotlib.pyplot as plt

locus1_alleleA_freqs = []
locus1_alleleB_freqs = []
for gen in gens:
    alleleA_freq = gen['locus1']['alleleA']
    alleleB_freq = gen['locus1']['alleleB']
    locus1_alleleA_freqs.append(alleleA_freq)
    locus1_alleleB_freqs.append(alleleB_freq)

print(locus1_alleleA_freqs)
print(locus1_alleleB_freqs)

locus2_alleleA_freqs = []
locus2_alleleB_freqs = []
for gen in gens:
    alleleA_freq = gen['locus2']['alleleA']
    alleleB_freq = gen['locus2']['alleleB']
    locus2_alleleA_freqs.append(alleleA_freq)
    locus2_alleleB_freqs.append(alleleB_freq)

locus3_alleleA_freqs = []
locus3_alleleB_freqs = []
for gen in gens:
    alleleA_freq = gen['locus3']['alleleA']
    alleleB_freq = gen['locus3']['alleleB']
    locus3_alleleA_freqs.append(alleleA_freq)
    locus3_alleleB_freqs.append(alleleB_freq)

plt.subplot(3, 1, 1)
plt.plot(locus1_alleleA_freqs, 'r-')
plt.plot(locus1_alleleB_freqs, 'r:')
plt.legend(['alleleA', 'alleleB'], loc='upper left')
plt.ylabel('Allele frequency')
plt.title('Locus1')


plt.subplot(3, 1, 2)
plt.plot(locus2_alleleA_freqs, 'b-')
plt.plot(locus2_alleleB_freqs, 'b:')
plt.legend(['alleleA', 'alleleB'], loc='upper left')
plt.ylabel('Allele frequency')
plt.title('Locus2')


plt.subplot(3, 1, 3)
plt.plot(locus3_alleleA_freqs, 'g-')
plt.plot(locus3_alleleB_freqs, 'g:')
plt.legend(['alleleA', 'alleleB'], loc='upper left')
plt.ylabel('Allele frequency')
plt.title('Locus3')


plt.ylim(0, 1)
plt.xlabel('Generations')
plt.show()
    