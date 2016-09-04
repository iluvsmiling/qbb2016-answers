"""
Usage: xxx.py <FlyBase.txt> <c_tab_StringTie> 
Purpose: Find corresponding translation between files. 
-- A: If found, print corresponding line from c_tab with ident
-- B: if not found, skip line.
"""

import sys


FlyID = open(sys.argv[1])
c_tab = open(sys.argv[2])

## Find AC (col 0) in gene_name (col 9) 
## if matched, print line from c_tab

Fly_dic = {}

for line in FlyID:
	field = line.rstrip("\r\n").split()
	Uniprot_col1 = field[1]
	ID_col0	= field[0]
	Fly_dic[ID_col0] = Uniprot_col1

for line in c_tab:
	match = line.rstrip("\r\n").split()
	gene_name = match[8]
	if gene_name in Fly_dic:
		print match 
	else:
		print "No match"





