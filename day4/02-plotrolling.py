#!/usr/bin/env python

import sys
import pandas as pd
import matplotlib.pyplot as plt

#how does expression of diff transcripts track along the chr

#use readtable so you dont have to specify tabs
df = pd.read_table( sys.argv[1] )

#just chr 3; another boolean select.

df_roi = df["chr"] == "3L"
df_chrom = df[df_roi]

#rolling size = 200, and what FPKM values
#calculate a mean for every step of 200
smoothed = df_chrom['FPKM'].rolling(200).mean()

#print smoothed

plt.figure()
plt.plot(smoothed)
plt.title("Chrom 3L, FPKM rolling mean 200")
plt.show()
plt.savefig("smoothed.png")

#
# plt.close()

#calculate some stat over that window, use mean
