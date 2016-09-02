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
pca = PCA()
fit = pca.fit(df)

plt.figure()
plt.bar( range(p), fit.explained_variance_ratio_)

plt.show()