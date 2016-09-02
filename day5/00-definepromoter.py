#!/usr/bin/env python
# Usage: 

#make csv with labeled rows and columns
import sys
import pandas as pd

#input c_tab


#print "chr", start, end, t_name
for line in sys.stdin.readline().rstrip("\r\n").split("\t")[2]:
    if line == "+":
        print (line.split("\t")[1] + "\t" 
            + (int(line.split("\t")[3]) - int(500)) + "\t"
            + (int(500) + int(line.split("\t")[3])) + "\t"
            + (line.split("\t")[5])
    else:
        print (line.split("\t")[1] + "\t" 
            + (int(line.split("\t")[3]) + int(500)) + "\t"
            + (int(line.split("\t")[3]) - int(500)) + "\t"
            + (line.split("\t")[5])
     