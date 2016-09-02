#!/usr/bin/env python

"""
Usage: <.py> <ctab 893 > 
"""

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

df_n1 = pd.read_table(sys.argv[1])

df_fpkm = df_n1[ "FPKM" ].values 
x = np.linspace(-10, 150, 400)
density = gaussian_kde(x)

#arbitrary?? or intelligent way?


plt.figure()
plt.plot(x, density(x))
plt.title("Kernal Density")
plt.ylabel("Density")
plt.xlabel("FPKM")
plt.savefig("p4_DensityPlot_res.png")
plt.close()