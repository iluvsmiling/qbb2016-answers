#!/usr/bin/env python

"""
Create a histogram showing FPKM values for SRR072893. 
Show positive values, then plot log of values

Usage: <.py> ~/data/results/stringtie/SRR072893/t_data.ctab
"""


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_n1 = pd.read_table(sys.argv[1])
df_fpkm = df_n1["FPKM"] > 0
fpkm_sel = df_n1[df_fpkm]["FPKM"]
fpkm_log = np.log10(fpkm_sel)
      

# yay! plot packages!

plt.figure()
plt.hist(fpkm_log)                  
minimum = np.min(fpkm_log)
maximum = np.max(fpkm_log)   

#plt.figure()                   
plt.title("Expression of SRR072893") 
plt.hist(fpkm_log, bins=30, range =[minimum, maximum], normed = True)                           
plt.ylabel("Frequency")   
plt.xlabel("log")        
plt.savefig("p2_histogram_res.png") 
plt.close()    

