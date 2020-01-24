#!/usr/bin/env python

'''
Exercise: design a function that takes a child-to-parent dictionary and a list of taxa as arguments, and return the last common ancestor of all taxa in the list

Design an iterative function and a recursive function
'''

child_to_parent_dict = {
    'Trepomonas' : 'Diplomonads',
    'Spironucleus' : 'Diplomonads',
    'Giardia' : 'Diplomonads',
    'Diplomonads' : 'Fornicata',
    'Dysnectes' : 'Fornicata',
    'Kipferlia' : 'Fornicata',
    'Chilomastix' : 'Fornicata',
    'Aduncisulcus' : 'Fornicata',
    'Ergobibamus': 'Fornicata',
    'Carpediemonas' : 'Fornicata',
    'Pentatrichomonas' : 'Parabasalia',
    'Trichomonas' : 'Parabasalia',
    'Tritrichomonas' : 'Parabasalia',
    'Paratrimastix' : 'Preaxostyla',
    'Monocercomonoides' : 'Preaxoystyla',
    'Trimastix' : 'Preaxostyla',
    'Fornicata' : 'Metamonads',
    'Parabasalia' : 'Metamonads',
    'Preaxostyla' : 'Metamonads'
}

# break up problem in three functions

# 1. get a list of all ancestors from a taxon
def get_all_ancestors(taxon, root, tree):
    if taxon == root:
        return [taxon]
    else:
        parent = tree.get(taxon)
        parent_ancestors = get_all_ancestors(parent, root, tree)
        
        # add parent to parent_ancestors
        return [parent] + parent_ancestors

# print(get_all_ancestors('Trichomonas','Metamonads', child_to_parent_dict))
# # ['Parabasalia', 'Metamonads', 'Metamonads']

# 2. get the lca of two taxa
def get_lca_two(taxon1, taxon2):
    # get ancestors of both taxon1 and taxon2
    ancestors1 = get_all_ancestors(taxon1, 'Metamonads', child_to_parent_dict)
    ancestors2 = get_all_ancestors(taxon2, 'Metamonads', child_to_parent_dict)
    # loop over ancestors1; the first that also exists in ancestors2 is their lca
    for ancestor in ancestors1:
        if ancestor in ancestors2:
            lca = ancestor
            return lca

# print(get_lca_two('Giardia','Spironucleus')) # Diplomonads
# print(get_lca_two('Giardia','Kipferlia'))    # Fornicata
# print(get_lca_two('Giardia','Trichomonas'))  # Metamonads


# 3. get the lca of a list of taxa
def get_lca_list(taxa):
    if len(taxa) == 2:
        lca = get_lca_two(taxa[0],taxa[1])
        return lca
    else:
        taxon1 = taxa.pop()
        ancestor = get_lca_list(taxa)
        lca = get_lca_two(taxon1,ancestor)
        return lca


taxa = ['Giardia','Spironucleus','Trepomonas']
print(get_lca_list(taxa))

# Example:
## taxa = ['Giardia','Trichomonas','Kipferlia','Spironucleus','Carpediemonas']

# Initial function call
## len = 5
## taxon1 = 'Carpediemonas'
## taxa = ['Giardia','Trichomonas','Kipferlia','Spironucleus']
## ancestor = get_lca_list(taxa) calls itself

# Second function call
## len = 4
## taxon1 = 'Spironucleus'
## taxa = ['Giardia','Trichomonas','Kipferlia']
## ancestor = get_lca_list(taxa) calls itself

# Third function call
## len = 3
## taxon1 = 'Kipferlia'
## taxa = ['Giardia','Trichomonas']
## ancestor = get_lca_list(taxa) calls itself

# Fourth function call
## len = 2
## lca = 'Metamonads'

# Third function call
## len = 3
## taxon1 = 'Kipferlia'
## taxa = ['Giardia','Trichomonas']
### ancestor = get_lca_list(taxa) == 'Metamonads' 
### lca = get_lca('Kipferlia','Metamonads') = Metamonads

# Second function call
## len = 4
## taxon1 = 'Spironucleus'
## taxa = ['Giardia','Trichomonas','Kipferlia']
## ancestor = get_lca_list(taxa) = 'Metamonads' 
### lca = get_lca('Spironucleus','Metamonads') = Metamonads

# Initial function call
## len = 5
## taxon1 = 'Carpediemonas'
## taxa = ['Giardia','Trichomonas','Kipferlia','Spironucleus']
## ancestor = get_lca_list(taxa) = Metamonads
### lca = get_lca('Carpediemonas','Metamonads') = Metamonads

