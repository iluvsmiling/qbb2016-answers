#!/usr/bin/env python

"""
Input: kmer_matcher.py target.fa query.fa k
Output: target_seq_name target_start query_start k 

"""

import sys
import fasta

matchr(open(sys.argv[1]), open(sys.argv[2]), sys.argv[3])

def matchr(target, query, k):
    k = int(k)
    kmer_beg = {}
    target_genetarget_gene = {}

    for ident, sequence in fasta.FASTAReader(query):
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

    for ident, sequence in fasta.FASTAReader(target):
        sequence = sequence.upper()
        for i in range(0, len(sequence) - k):
            kmer = sequence[i:i+k]
            if kmer not in kmer_beg:
                kmer_beg[kmer]= []
                target_gene[kmer] = []
            kmer_beg[kmer].append(i)
            target_gene[kmer].append(ident)
    
    query_n1 = {}
    query_n2 = {}
    
    ## don't know how to do 100 loop???
    #for i, enumerate
    #if i == 1000:
     #   break
    
    for ident in query_match:
        print "Identifier: ", ident
        print "Target_name: ", query_n2[ident]
        print "Target_start: ", kmer_beg[ident]
        print "Query_start: ", query_n1[ident]
    

