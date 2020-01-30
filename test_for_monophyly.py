#!/usr/bin/env python

'''
Write a function that tests whether two taxa are more closely related
to each other, than either of them is to a third taxon, given a tree

Define tree as a nested list
'''

# build tree
from ete3 import Tree
t = Tree(
    "((Trimastix,(Monocercomonoides,Paratrimastix)),"
    "((Tritrichomonas,(Trichomonas,Pentatrichomonas)),"
    "(Carpediemonas,(Ergobibamus,(Adunciculcus,((Chilomastix_cu,Chilomastix_ca),"
    "(Kipferlia,(Dysnectes,(Giardia,((Spironucleus_sa,Spironucleus_ba),"
    "(Spironucleus_vo,Trepomonas)))))))))));"
)

print(t)
#       /-Trimastix
#    /-|
#   |  |   /-Monocercomonoides
#   |   \-|
#   |      \-Paratrimastix
# --|
#   |      /-Tritrichomonas
#   |   /-|
#   |  |  |   /-Trichomonas
#   |  |   \-|
#    \-|      \-Pentatrichomonas
#      |
#      |   /-Carpediemonas
#      |  |
#       \-|   /-Ergobibamus
#         |  |
#          \-|   /-Adunciculcus
#            |  |
#             \-|      /-Chilomastix_cu
#               |   /-|
#               |  |   \-Chilomastix_ca
#                \-|
#                  |   /-Kipferlia
#                  |  |
#                   \-|   /-Dysnectes
#                     |  |
#                      \-|   /-Giardia
#                        |  |
#                         \-|      /-Spironucleus_sa
#                           |   /-|
#                           |  |   \-Spironucleus_ba
#                            \-|
#                              |   /-Spironucleus_vo
#                               \-|
#                                  \-Trepomonas

# convert to nested list format
metamonad_tree = [
    [
        'Trimastix',
        [
            'Monocercomonoides', 'Paratrimastix'
        ]
    ],
    [
        [
            'Tritrichomonas',
            [
                'Trichomonas', 'Pentatrichomonas'
            ]
        ],
        [
            'Carpediemonas',
            [
                'Ergobibamus',
                [
                    'Adunciculcus',
                    [
                        [
                            'Chilomastix_cu', 'Chilomastix_ca'
                        ],
                        [
                            'Kipferlia',
                            [
                                'Dysnectes',
                                [
                                    'Giardia',
                                    [
                                        [
                                            'Spironucleus_sa', 'Spironucleus_ba'
                                        ],
                                        [
                                            'Spironucleus_vo', 'Trepomonas'
                                        ]
                                    ]
                                ]
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
]


def has_taxon(clade, taxon):
    '''
    Parse a subtree and return True if
    it contains a taxon.
    Recursive function!
    '''
    result = False
    for node in clade:
        if isinstance(node, list):
            # recursively calling itself
            # on a smaller version of
            # the problem
            if has_taxon(node, taxon):
                result = True
        else:
            # the base case where the
            # function can be resolved
            # without calling itself
            if node == taxon:
                result = True
    return result


def get_subtrees(tree, taxon1, taxon2):
    '''
    Return all subtrees of a given tree
    that contain both specified taxa.
    Recursive function!
    '''
    subtrees = []
    # add tree to subtree list if it has both specified taxa
    if has_taxon(tree, taxon1) and has_taxon(tree, taxon2):
        subtrees.append(tree)
    # iterate recursively over the two daughter trees
    # and check if they have both specified taxa
    for subtree in tree:
        # get_subtrees() requires a list so
        # only feed lists to get_subtrees()
        if isinstance(subtree, list):
            found_subtrees = get_subtrees(subtree, taxon1, taxon2)
            subtrees.extend(found_subtrees)
    return subtrees


def count_taxa(subtree):
    '''
    Count the number of taxa
    associated with a given subtree.
    Recursive function!
    '''
    count = 0
    for subclade in subtree:
        # if subclade is a list,
        # call count_taxa() on a smaller subtree
        if isinstance(subclade, list):
            count = count + count_taxa(subclade)
        # if its not a list, we've reached a leaf!
        # add leaf to count
        else:
            count = count + 1
    return count


def size_smallest_subtree(tree, taxon1, taxon2):
    subtrees = get_subtrees(tree, taxon1, taxon2)

    # for i in subtrees:
    #     print(i)

    # sort subtrees by their associated number of taxa
    sorted_subtrees = sorted(subtrees, key=count_taxa)
    # smallest subtree is the first subtree in sorted_subtrees
    smallest_subtree = sorted_subtrees[0]
    return count_taxa(smallest_subtree)


def are_close_relatives(tree, taxon1, taxon2, taxon3):
    '''
    Given a tree, are taxon1 and taxon2
    more related to each other than either
    of them are to taxon3 ?
    '''
    taxon12_size = size_smallest_subtree(tree, taxon1, taxon2)
    taxon13_size = size_smallest_subtree(tree, taxon1, taxon3)
    taxon23_size = size_smallest_subtree(tree, taxon2, taxon3)
    print('Clade size for ' + taxon1 + ' and ' + taxon2 + ' is: ', taxon12_size)
    print('Clade size for ' + taxon1 + ' and ' + taxon3 + ' is: ', taxon13_size)
    print('Clade size for ' + taxon2 + ' and ' + taxon3 + ' is: ', taxon23_size)
    if taxon12_size < taxon23_size and taxon12_size < taxon23_size:
        return True
    else:
        return False


print(are_close_relatives(metamonad_tree, 'Tritrichomonas', 'Trichomonas', 'Kipferlia'))
