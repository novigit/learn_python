## LISTS
# examples of lists
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla"]
conserved_sites = [24, 56, 132]
# lists have elements that start counting at 0
print(apes[2])
first_site = conserved_sites[2]

# index() returns the index of an element you know the value of, but not the index
chimp_index = apes.index("Pan troglodytes")
# chimp_index is now 1

# negative indices start counting from the last element to the first elements
print(apes[-1]) # prints the last element
print(apes[-2]) # prints the second-to-last element

# subset a list
ranks = ["kingdom","phylum", "class", "order", "family"]
lower_ranks = ranks[2:5]
# it is possible to simply print lists
print(ranks)
print(lower_ranks)

# append a list
apes.append("Pan paniscus")
print(apes)
# note that append actually changes the apes list itself

# return the length of a lists
print(len(apes))

# change the order of a list
# note that it changes the list itself
ranks = ["kingdom","phylum", "class", "order", "family"]
# flip the order through reverse()
ranks.reverse()
print(ranks)
# sort alphabetically with sort()
ranks.sort()
print(ranks)
# sort() sorts by default a->z, and 0->9

## LOOPS
apes = ["Homo sapiens", "Pan troglodytes", "Gorilla gorilla","Pan paniscus"]
for ape in apes:
    print(ape + " is an ape")
# we are not allowed to change the list while inside the loop

# example of looping/iterating over a list
for ape in apes:
    name_length = len(ape)
    first_letter = ape[0]
    print(ape + " is an ape. Its name starts with " + first_letter)
    print("Its name has " + str(name_length) + " letters")
# python is strict about indentation!
# for ape in apes:
#    name_length = len(ape)
#   first_letter = ape[0]
#    print(ape + " is an ape. Its name starts with " + first_letter)
#    print("Its name has " + str(name_length) + " letters")
# IndentationError: unindent does not match any outer indentation level

# example of looping/iterating over a string
name = "Homo Sapiens"
for char in name:
    print("one character is " + char)

# split a string into a list
names = "melanogaster,simulans,yakuba,ananassae"
species = names.split(",")
print(str(species))

## PARSE A FILE
# line by line
file = open("sequences.fasta")
for line in file:
    # do something with the line
    print(line.strip("\n"))

# character by character
file = open("sequences.fasta")
contents = file.read()
# .read() puts all the contents of all the lines in the file in one long string
# so when you loop over 'contents' object, you iterate character by character
for line in contents:
    # warning: line contains just a single character!
    print(line)

## once a file object is iterated over, it can't be iterated over again
## see below:
# print the length of each line
file = open("sequences.fasta")
for line in file:
    print("The length is " + str(len(line)))

# print the first character of each line
for line in file:
    print("The first character is " + line[2])
# the second loop is executed, but 'file' is exhausted so there is nothing to loop over

## a solution would be to close the file before reopening it
## print the length of each line
file = open("sequences.fasta")
for line in file:
    print("The length is " + str(len(line)))
file.close()

# print the first character of each line
file = open("sequences.fasta")
for line in file:
    print("The first character is " + line[2])
file.close()

## a more elegant solution is to use the .readlines() method
## it stores the lines of the file object into a list
file = open("sequences.fasta")
all_lines = file.readlines()

# print the lengths
for line in all_lines:
    print("The length is " + str(len(line)))

# print the first characters
for line in all_lines:
    print("The first character is " + line[0])

# range() returns a list of numbers
for number in range(2, 14, 4):
    print(number) # 2, 6, 10
# note that it doesn't report 14.
# it works similar to index in string[start:end] or list[start:end] in this way
