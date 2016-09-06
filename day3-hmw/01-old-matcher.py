#!/usr/bin/env python

"""
Input: 1_d3_matcher.py target.fa query.fa k
Output: target_seq_name target_start query_start k 

"""

import sys
import fasta_fixed


def x (target, query):
    kmer_beg = {}
    target_gene = {}
    query_n1 = {}
    query_n2 = {}
   
    for ident, sequence in fasta_fixed.FASTAReader(query):
        sequence = sequence.upper()

    for i in range(0,len(sequence) - k):
        kmer = sequence[i:i+k]
        if kmer in query_n1:
            query_n1[kmer].append(i)
        if kmer in kmer_beg:
            query_n1[kmer]=[]
            query_n1[kmer].append(i)
            query_n2[kmer]=[]
            query_n2[kmer].append(target_gene[kmer])
print 
   
    for ident, sequence in fasta_fixed.FASTAReader(target):
        sequence = sequence.upper()
        for i in range(0, len(sequence) - k):
            kmer = sequence[i:i+k]
            if kmer not in kmer_beg:
                kmer_beg[kmer]= []
                target_gene[kmer] = []
            kmer_beg[kmer].append(i)
            target_gene[kmer].append(ident)
            
###kmer_loci (kmer =[(ident, i)]); duples

    
    ## don't know how to do 100 loop???
    #for i, enumerate
    #if i == 1000:
     #   break
    
    for ident in query_match:
        print "ID: ", ident
        print "Target Name: ", query_n2[ident]
        print "Target Start: ", kmer_beg[ident]
        print "Query Start: ", query_n1[ident]
    
target = open(sys.argv[1])
query = open(sys.argv[2])
k = int(sys.argv[3])


