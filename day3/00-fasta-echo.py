#!/usr/bin/env python

"""
Parse a single FASTA record from stdin and print it
"""


import sys

# whenever i create a new line object, a cursor pointing to first , 
# end of line "\n"
# gives me that line and moves cursor to next limit

#read 1 line from std input
line = sys.stdin.readline()

# Verify is header line; make sure that line starts with >
assert line.startswith(">")

#take everything from that line 
#Extract ID -- whole line
#identifier = line[1:].rstrip("\r\n")

identifier = line[1:].split()[0]
sequences=[]
while True:
	line = sys.stdin.readline().rstrip("\r\n")
	if line.startswith(">") or line == "":
		break
	else:
		sequences.append(line)

print identifier, "". join(sequences)

