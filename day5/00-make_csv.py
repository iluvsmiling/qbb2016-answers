#!/usr/bin/env python
# Usage: 

#make csv with labeled rows and columns
import sys
import pandas as pd

# stringtie stuff
base = sys.argv[1]
df = pd.read_csv(base + "/fastq/samples.csv")

d ={}

#something we havent done 
for _, sample, sex, stage in df.itertuples():
    #make a new dataframe with all my fpkm, 
    # i want meaningful column and row names -- 
    d[sex + "_" + stage] = pd.read_table(base + "/results/stringtie/" + sample + "/t_data.ctab",
        index_col = "t_name")["FPKM"]
    
df = pd.DataFrame( d )
df.to_csv(sys.stdout)

