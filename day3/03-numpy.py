#! /usr/bin/env python

import sys
import numpy as np

fpkm_values = []
for i, line in enumerate(sys.stdin):
	if i==0:
		continue
	fields = line.rstrip("\r\n").split("\t")
	fpkm = float(fields[11])
	fpkm_values.append(fpkm)

print fpkm_values

a = np.array(fpkm_values)

print a
print a.shape
print a.dtype
##.py < ctab
