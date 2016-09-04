#!usr/bin/env python

"""
Test if filter works line of code
Count number of "FBgn" appears in line and compare with all lines
"""
import sys
file = open(sys.argv[1])

sun = 0
for line in file.readlines():
	if "FBgn" in line:
		continue
		sun = sun+1

shine = 0
for line in file.readlines():
	shine = += 1

print (sun + "\t" + shine)
		 
