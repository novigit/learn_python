#!/usr/bin/env python

'''
Store gene expression data from different metal exposures in a dict of sets
Calculate all pairwise gene expression distances and store in a dict of dicts
'''

gene_expression_data = {
    'arsenic': {1, 2, 3, 4, 5, 6, 8, 12},
    'cadmium': {2, 12, 6, 4},
    'copper': {7, 6, 10, 4, 8},
    'mercury': {3, 2, 4, 5, 1}
}


def get_distance(set1, set2):
    intersect = set1 & set2
    union = set1 | set2
    dist = len(intersect) / len(union)
    return dist


def calc_distance_matrix(dict_of_sets):
    # declare dict
    distance_matrix = {}
    for metal1, gene_set1 in dict_of_sets.items():
        # declare dict of dict
        distance_matrix[metal1] = {}
        for metal2, gene_set2 in dict_of_sets.items():
            if metal1 != metal2:
                # calculate distance and store in dict of dict
                distance = get_distance(gene_set1, gene_set2)
                distance_matrix[metal1][metal2] = distance
    return distance_matrix


# calculate distance matrix
matrix = calc_distance_matrix(gene_expression_data)
print(matrix['arsenic']['cadmium'])
print(matrix['cadmium']['copper'])
print(matrix)
