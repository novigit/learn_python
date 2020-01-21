#!/usr/bin/env python
import sys

def parse_and_write(filein):
    
    with open(filein, 'r') as file:
        for line in file:

            # capture prefix
            line_contents = line.strip('\n').split('\t')
            prefix = line_contents[1].split('_')[0]

            # append to outfile
            ## note this is in-efficient because you open the same file each time you iterate over the loop
            with open('%s.split.tsv'% prefix, 'a') as fileout:
                fileout.write(line)
            
        return None

filein = sys.argv[1]
parse_and_write(filein)