import lecture12

with lecture12.fastqReader('1000_reads.fastq') as fq, lecture12.fastqWriter('outputfile.fastq') as fw:
    for read in fq:
        fw.write(read)
