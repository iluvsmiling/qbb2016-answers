#!/usr/bin/env python
## This is a copy of someone's code to see if I still get pandas error

import sys
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#open SRR files of interest
df = pd.read_table(sys.argv[1])
df2 = pd.read_table(sys.argv[2])

#create an array of fpkm values

fpkm = df["FPKM"].values


fpkm2 = df2["FPKM"].values

#determine log of fpkm values
fpkm_log = np.log(fpkm + 1)
fpkm_log2 = np.log(fpkm2 + 1)

#define m and a as follows:
m = (fpkm_log - fpkm_log2)
a = (.5*(fpkm_log + fpkm_log2))

# print m
# print a

#format and print graph
plt.figure()
plt.title("MA-plot of SRR072893 and SRR072915")
#plt.xscale()
#plt.yscale()
plt.scatter(a, m)
plt.ylabel("M")
plt.xlabel("A")
#plt.hexbin(df["FPKM"] +1, df2["FPKM"]+1) #gives density of points as well
plt.savefig("maplot-homework.png")
plt.close()

##Comment from Nina: still get error from pandas. Must be something wrong with pandas or input file. 
