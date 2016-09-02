#!/usr/bin/env python
# Usage: 

#make csv with labeled rows and columns
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.decomposition import PCA

df = pd.read_csv(sys.argv[1], index_col=0)

n, p = df.shape

#transpose our df
df = df.T


#pca fit
pca=PCA()
fit = pca.fit(df)
#transform data
x = fit.transform(df)



plt.figure()
n_pcs = 8
#plt.subplot 8 stacked, 8 wide, position (start 1 , l to r, t to b)
x2 = x[:,:n_pcs]

for i in range(n_pcs):
    for j in range(n_pcs):
        plt.subplot(n_pcs, n_pcs, i + j*n_pcs + 1)
        plt.scatter(x2[:,i], x2[:j])   


 

plt.show()