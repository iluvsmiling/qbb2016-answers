#!/usr/bin/env python

import sys


file_name_ctab=sys.argv [1]
file_name_FlyBase_out = sys.argv[2]

#first, define dictionary 
fly_dict = {}

# add to dictionary; compare ctab
### unsure whethere to use ("\t") or () char
for line in file_name_ctab:
	ID_Fly = line.rstrip("\r\n").split("\t")[8]
	if ID_Fly not in fly_dict:
		ctab_d[(ID_Fly)] = line.rstrip("\r\n").split("\t")

#compare with FlyBase_py_output
sun = 0

for line2 in file_name_FlyBase_out: 
	FlyID = line2.rstrip("\r\n").split("\t")[0]
	AC_uniprot = line2.rstrip("\r\n").split("\t)[1]
	if FlyID in fly_dict:
		print(
	
