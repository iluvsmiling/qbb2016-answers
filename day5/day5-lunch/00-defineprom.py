#!/usr/bin/env python
# Usage: 

#make csv with labeled rows and columns
import sys

#input c_tab


#print "chr", start, end, t_name
good_genes=["3R", "3L", "2R", "2L", "X", "Y", "4"]
for line in sys.stdin:
    if line.startswith("t_id"):
        continue
        
    fields = line.rstrip("\r\n").split("\t")
    if not fields[1] in good_genes:
        continue
    
    if fields[2] == "+":
        print (fields[1] + "\t" 
            + str(int(fields[3]) - int(500)) + "\t"
            + str(int(500) + int(fields[3])) + "\t"
            + (fields[5]))
    else:
        print (fields[1] + "\t" 
            + str(int(fields[3]) + int(500)) + "\t"
            + str(int(fields[3]) - int(500)) + "\t"
            + (fields[5]))
     
