dna = "AATGATGAACGAC"
dinucleotides = ['AA','AT','AG','AC',
                 'TA','TT','TG','TC',
                 'GA','GT','GG','GC',
                 'CA','CT','CG','CT']
# declare dictionary
all_counts = {}
# build dictionary with dinucleotides with >0 counts
for dinucleotide in dinucleotides:
    count = dna.count(dinucleotide)
    if count > 0:
        # keys: dinucleotides, values: counts
        all_counts[dinucleotide] = count
# print dictionary
print(all_counts)

# print all values of the key 'TG'
print(all_counts['TG']) # 2
#print(all_counts['TA']) # returns KeyError, because it didnt exist in the dict

# get()
# gets the value associated with the requested key
# so in principle same as using ['TG']
print(all_counts.get('TG')) # 2
print(all_counts.get('TA')) # now returns None
# the second argument of get() specifies the value to return when the requested key is not found
print(all_counts.get('TA'),0) # returns None 0

print("count for TG is " + str(all_counts.get('TG', 0)))
print("count for TT is " + str(all_counts.get('TT', 0)))
print("count for GC is " + str(all_counts.get('GC', 0)))
print("count for CG is " + str(all_counts.get('CG', 0)))
# so get is very useful to check retrieve values from requested keys
# if keys don't exist, you get an appropriate output

# loop over keys of a dictionary
for dinucleotide in all_counts.keys():
    if all_counts.get(dinucleotide) == 2:
        print(dinucleotide)
## !! dicts are inherently unordered !!
# sort the list of keys if you want to loop orderly over the keys of the dict
for dinucleotide in sorted(all_counts.keys()):
    if all_counts.get(dinucleotide) == 2:
        print(dinucleotide)

# an item is a key value pair!
for dinucleotide, count in all_counts.items():
    if count == 2:
        print(dinucleotide, "\t", count)
