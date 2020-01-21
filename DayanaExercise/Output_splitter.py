#!/usr/bin/env python
import sys
import pandas as pd
from joblib import Parallel, delayed


def writer(tupla):
    name, group = tupla
    group.to_csv('%s.pandas.tsv' % name, sep='\t', header=None, index=False)


def split_diamond_output(output, characters):
    chunksize = 1000 * 10
    init_chunks = pd.read_csv(output, sep='\t', header=None,
                              chunksize=chunksize)
    df = pd.concat(init_chunks).drop_duplicates()
    matching_string = df[1].str[:characters]
    my_groups = df.groupby(matching_string, as_index=False)
    _ = Parallel(n_jobs=-1)(delayed(writer)((name, chunk))
                            for name, chunk in my_groups)
    return None


# ----   Execute ----
'''
To use this script:
source activate python36-generic
Output_splitter.py <diamond_output> <prefix_characters>
'''
infile = sys.argv[1]
prefix_characters = int(sys.argv[2])
_ = split_diamond_output(infile, prefix_characters)
