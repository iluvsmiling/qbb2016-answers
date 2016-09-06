#find how predictive each is of gene expression to each modification
# pair Histone marks with FPKM
# input .ctab 
import sys
import numpy as np
import statsmodels.api as sm

ctab = open(sys.argv[1])
btab = open(sys.argv[2])

y = []
x = []
good_genes=["3R", "3L", "2R", "2L", "X", "Y", "4"]

for line in ctab:
    if line.startswith ("t_id"):
        continue
        
    fields = line.rstrip("\r\n").split("\t")
    if not fields[1] in good_genes:
        continue
        
    #filters out chromsomes
    fields = line.rstrip("\r\n").split("\t")
    yy = float(fields[-1])
    y.append(yy)


for line in btab:
    Bfields = line.rstrip("\r\n").split("\t")
    xx = float(Bfields[-1])
    x.append(xx)

y_ = np.array(y)
x_ = np.array(x)

print len(x_), len(y_)

model = sm.OLS(y_, x_)

results = model.fit()

print results.summary()
