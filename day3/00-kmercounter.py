#!/usr/bin/env python
"""
read sequences from a FASTA file, count the number of times each k-mer occurs across 
samples and print
kmers and counts.

usage: 00-kmercounter.py k > fasta_file

"""

# read each sequence from FASTA, parse parameters, k 
# read data, FASTA parser
# where to store kmer counts
# length = n
# kmer = sequence[i:i+k]
## 
#kmer_counts = dictionary{}

import sys
import fasta2

#command line arguments
k = int(sys.argv[1]) 
kmercounts = {}

#i have the kmer at position i, if ive seen the kmer, it sets to 0. if i have seen it, 
for ident, sequence in fasta2.FASTAReader(sys.stdin):
    sequence = sequence.upper()
    for i in range(0, len(sequence)-k):
        kmer = sequence[i: i+k]
        if kmer not in kmercounts:
            kmercounts[kmer] = 0
        else:
            kmercounts[kmer] += 1

for kmer in sorted(kmercounts, key = kmercounts.get, reverse = True):
    print kmer, kmercounts[kmer]

# for kmer in kmer_counts:
#     print kmer, count
    
 

