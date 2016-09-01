#!/usr/bin/env python

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""input1: stringtie file """

df_n1 = pd.read_table(sys.argv[1]) 

# filter for gene_name = "Sxl"
df_gn = df_n1["gene_name"] == "Sxl"
df_gn_f = df_n1[df_gn] 

#Take Sxl and filter for FPKM>0
df_fpkm = df_gn_f["FPKM"]>0
df_fpkm_f = df_gn_f[df_fpkm]

#Calculate log of FPKM
#Attribute error as : 'int' object has no attribute 'log'
df_log = np.log(df_fpkm_f["FPKM"])


"""####Repeat for sys.argv[2]"""
df_n2 = pd.read_table(sys.argv[2]) 

# filter for gene_name = "Sxl"
df_gn2 = df_n2["gene_name"] == "Sxl"
df_gn_f2 = df_n2[df_gn2] 

#Take Sxl and filter for FPKM>0
df_fpkm2 = df_gn_f2["FPKM"]>0
df_fpkm_f2 = df_gn_f2[df_fpkm2]

#Calculate log of FPKM
#Attribute error as : 'int' object has no attribute 'log'
df_log2 = np.log(df_fpkm_f2["FPKM"])

"""PLOT""" 
df_combo = (df_log, df_log2)
labels_x = sys.argv[1], sys.argv[2]
plt.ylabel("FPKM")
plt.boxplot(df_combo, labels = labels_x)
plt.show()




