#!/usr/bin/env python
import sys


def dic_from_scratch(filein):
    proteomes = {}
    with open(filein, 'r') as I:
        for line in I:
            line_contents = line.strip().split('\t')
            if line_contents:
                prefix = line_contents[1].split('_')[0]
                if not prefix in proteomes:
                    proteomes[prefix] = [line]
                else:
                    proteomes[prefix].append(line)
    return proteomes


def writer(dictionary):
    for key in dictionary.keys():
        with open('%s.basic.split.tsv'% key, 'w') as O:
            for entry in dictionary[key]:
                O.write(entry)
    return None



# ---- Execute ---
'''
To use this script:
source activate python36-generic
Basic1_splitter.py <diamond_output>
'''
infile = sys.argv[1]
dataset = dic_from_scratch(infile)
_ = writer(dataset)
