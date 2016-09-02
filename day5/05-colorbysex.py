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
# df = df.T
pca = PCA()
fit = pca.fit(df)
x = pca.transform(df)


#color by sex
colors = []
for name in df.columns:
        if "female" in name:
            colors.append("purple") 
        else:
            colors.append("orange")
plt.figure()
plt.plot(fit.components_.T[:,:2], label =[])
plt.scatter(x[:0], x[:1], c=colors, edgecolor = "None")
            
colnames = df.T.columns
for i in range(l(colnames)):
    plt.annotate(colnames[i], (x[i,1], x[i,2]))



plt.legend()
plt.show()

#statsmodels, linear regression, ols function least squares
# 4 files that contain signals from his mod
# bigwig
# does the level of histone mod predict gene expression
# my gtf files - find TSS. 
    integral around it
    
# 500 bp expand, give you a region.




