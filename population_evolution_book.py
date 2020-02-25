#!/usr/bin/env python

import random


class Allele(object):
    def __init__(self, name, fitness):
        self.name = name
        self.fitness = fitness

# a Locus object is a list of Allele objects
class Locus(object):
    def __init__(self, name):
        self.name = name
        self.alleles = []

    def add_allele(self, allele):
        self.alleles.append(allele)

    def get_random_allele(self):
        return random.choice(self.alleles)

# define all 3 loci with their allele alternatives and their fitness scores
## Note that here a 'locus' is not a biological, physical entity
## Rather its an information entity that contains all possible alleles it can contain
locus1 = Locus('Locus One')
locus1.add_allele(Allele('A', 1))
locus1.add_allele(Allele('a', .94))

locus2 = Locus('Locus Two')
locus2.add_allele(Allele('B', 1))
locus2.add_allele(Allele('b', .76))

locus3 = Locus('Locus Three')
locus3.add_allele(Allele('C', 1))
locus3.add_allele(Allele('c', .81))

all_loci = [locus1, locus2, locus3]

class Individual(object):
    def __init__(self, alleles):
        self.alleles = alleles

    def get_genotype(self):
        result = ''
        for a in self.alleles:
            result = result + a.name
        return result

    def get_fitness(self):
        # a nice way to get the product of a list
        final_fitness = 1
        for a in self.alleles:
            final_fitness = final_fitness * a.fitness
        return final_fitness


def create_individual(loci):
    alleles_for_individual = []
    for locus in loci:
        alleles_for_individual.append(locus.get_random_allele())
    i = Individual(alleles_for_individual)
    return i


def create_population(size, loci):
    all_individuals = []
    for i in range(size):
        all_individuals.append(create_individual(loci))
    return all_individuals


def get_allele_frequency(population, allele):
    allele_count = 0
    for indiv in population:
        if allele in indiv.alleles:
            allele_count += 1
    return allele_count / len(population)


def summarize_population_alleles(population, loci):
    for locus in loci:
        for allele in locus.alleles:
            print(allele.name, get_allele_frequency(population, allele))
my_population = create_population(100, all_loci)

# for ind in my_population:
#     print(ind.get_genotype(), ind.get_fitness())

print(get_allele_frequency(my_population, locus1.alleles[0]))
summarize_population_alleles(my_population, all_loci)
