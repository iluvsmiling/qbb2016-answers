#!/usr/bin/env python

#how did we look through a file; use for loop
# then split on delimiter

import sys
import pandas as pd

# returning df object, df has three files, which can referr to as positoin or name

df = pd.read_csv(sys.argv[1])

#how would you refer to sample -- string
print df["samples"]
print df[0:5] 
print df["sample"][0:5]

#how do you find the rows that have female, 
#boolean filter
# cmd forward slash
# i want to look at the sex column
# for a given row, does it equal female
print df["sex"] == "female"


#for line in enumerate (sys.argv[1]):
#	if i == 0:
#		continue
#	fields = line.rstrip("\r\n").split(",")
#	print fields[0]

#look at data/fastq/samples
# .py ~/data/fastq/samples.csv

file.close()
