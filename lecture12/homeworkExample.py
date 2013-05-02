#!/usr/bin/env python

import sys
import argparse
import lecture12

def main():
    """ Read fastq file "fastq", and then calculate the GC content for each read. 
    If the GC content for a read is > 40%, print that read's name, it's GC content, 
    and the GC content of it's reverse complement.
    """
    parser = argparse.ArgumentParser(description='Print the GC contents >XX% in a fastq file')
    parser.add_argument('fastq', help='fastq file to process')
    parser.add_argument('-p', '--percentgc', type=int, default=40, help='percent GC content threshold [default = 40]')
    args = parser.parse_args()

    fastqFile = args.fastq
    percentgc = args.percentgc
    with lecture12.fastqReader(fastqFile) as fq:
        """ Opens the specified fastq file using fastqReader class """
        for read in fq:
            """ Every iteration of this loop returns a read class containing data from fastqFile. 
            Below is pseudocode that gives you a guide for completing the homework. 
            """
            print fastqFile
            print percentgc
            ## calculate GC content for read.seq
            ## if GC content is greater than percentgc then:
                ## print the read name
                ## print the GC content
                ## print the GC content of read.revcomp()

if __name__ == "__main__":
    try:
        main()                                                                                                                                                             
    except KeyboardInterrupt:
        print "keyboard interrupt, exiting"
        sys.exit(1)
