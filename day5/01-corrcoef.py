#!/usr/bin/env python
# Usage: 

#make csv with labeled rows and columns
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# stringtie stuff
df = pd.read_csv(sys.argv[1], index_col=0)

corr = np.corrcoef(df.values.T)
corr = pd.DataFrame(corr, columns = df.columns)

print corr

plt.figure()
plt.pcolor(corr)
plt.colorbar()
plt.xticks(range(len(corr.columns)), corr.columns)
plt.show()
