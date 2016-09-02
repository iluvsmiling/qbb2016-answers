"""
Usage: <SRR072893> <SRR072915>
"""

#!/usr/bin/env python


import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#open SRR files of interest
df_n1 = pd.read_table(sys.argv[1])
df_n2 = pd.read_table(sys.argv[2])

#create an array of fpkm values

fpkm_n1 = df_n1["FPKM"].values
fpkm_n2 = df_n2["FPKM"].values

#m = (fpkm_log1 - fpkm_log2)
#a = ( 0.5 * (fpkm_log + fpkm_log2) )
#OH WAIT, can i do this:

M_n1 = np.log(fpkm_n1 + 1) - np.log(fpkm_n2 + 1)
A_n1 = 0.5*(np.log(fpkm_n1 + 1) + np.log(fpkm_n2 + 1)

#error with plt.figure()

plt.figure()
plt.scatter(A_n1, M_n1)
plt.ylabel("M")
plt.xlabel("A")
plt.title("MA Plot of SRR072893 and SRR072915 Expression")


plt.savefig("p3_MA_res.png")
plt.close()