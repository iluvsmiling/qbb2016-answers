#!/usr/bin/env python

import sys
import pandas as pd

df_ctab = pd.read_csv(sys.argv[1], sep="\t")
print df_ctab.head()
print df_ctab.describe()

#how to find FPKMs that are greater than 1000
# why cant we just print instead of assigning

df_roi = df_ctab["FPKM"] > 100
print df_ctab[df_roi]

df_x = df_ctab["gene_name"] == "fzo"
print df_ctab[df_x]

df_high_exp = df_ctab[df_roi]
print df_high_exp["gene_name"]
df2_roi = df2_ctab["FPKM"] > 1000

#Calculate the intersection
# df_high_exp = df
# df2_high_exp = df2_ctab[df2_roi]
# df_

#what would be a method to look at the first 10 
#cmd: ./xxx.py ~/data/results/stringtie...t_data




