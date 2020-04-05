#!/usr/bin/env python
import re

# store blast results as list of tuples
blast_file = open("blast_result.txt")
hsps = []
for hsp in blast_file.readlines():
    if not hsp.startswith('#'):
        # tuple() creates a tuple from an iterable (here a list)
        # tuples are good to store immutable, heterogeneous data
        fields = tuple(hsp.rstrip("\n").split("\t"))
        # create list of tuples
        hsps.append(fields)
blast_file.close()
# now we have 'hsps', a list which we can iterate over

# but we may as well can use the file object, which is also an iterable (line-by-line even)
## however the top lines that start with # are a nuisance so we want to omit them
## note that a filter object is a lazy iterable, so you can only call it once
## since here we want to call on hit_lines multiple times, its more suitable to store it as a list
hit_lines = list(filter(lambda line: not line.startswith('#'), open("blast_result.txt")))

'''
How many hits have fewer than 20 mismatches? 25
'''
# return a list (map object) of all mismatches
## the 'x' in the lambda function holds
## each element in the 'hsps' list (a tuple)
mismatches = map(lambda x: x[4], hsps)
# return a list (filter object) of all hsps
# with fewer than 20 mismatches
## 'mismatches' is a list of strings
## thus convert to integer
few_mismatches = filter(lambda x: int(x) < 20, mismatches)
# can not return len() on a filter object
# thus needed to convert filter object to a list
# print(len(list(few_mismatches)))

## Alternative solution


def has_few_mismatches(hit):
    mismatch_count = hit.rstrip("\n").split("\t")[4]
    return int(mismatch_count) < 20


few_mismatch_hits = filter(has_few_mismatches, hit_lines)
print(len(list(few_mismatch_hits)))


'''
Identify the ten hits with the lowest %id and list their subject names
'''


def get_perc_id(hit):
    perc_id = hit.rstrip("\n").split("\t")[2]
    return float(perc_id)


def get_subj_name(hit):
    subj_name = hit.rstrip('\n').split('\t')[1]
    return subj_name


hit_lines_sorted_by_id = sorted(hit_lines, key=get_perc_id)
subj_names_low_id = map(get_subj_name, hit_lines_sorted_by_id[0:10])
print(list(subj_names_low_id))


'''
List the start position divided by the match length for all 'COX1' hits
'''


def get_proportion(hit):
    fields = hit.rstrip("\n").split("\t")
    aln_length, start_pos = fields[3], fields[6]
    proportion = int(start_pos) / int(aln_length)
    return proportion


# re.search() returns True or False
cox1_hits = list(filter(lambda hit: re.search(r'COX1', hit), hit_lines))
proportion_list = list(map(get_proportion, cox1_hits))
print(proportion_list)
