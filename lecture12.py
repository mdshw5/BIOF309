from __future__ import division

class read(object):
    """
    A class to hold features from fastq reads.
    """

    def __init__(self, name, seq, strand, qual):
        self.name = name
        self.seq = seq
        self.strand = strand
        self.qual = qual
        self.dict = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N':'N'}

    def __getitem__(self, key):
        return self.__class__(self.name, self.seq[key], self.strand, self.qual[key])

    def __repr__(self):
        return 'name: {0}\nseq: {1}\nstrand: {2}\nqual: {3}\n'.format(\
        self.name, self.seq, self.strand, self.qual)

    def seqlen(self):
        return len(self.seq)

    def reverse(self):
        """ Reverse the order of self """
        return self.__class__(self.name, self.seq[::-1], self.strand, self.qual[::-1])

    def complement(self):
        """ Take the compliment of read.seq """
        compseq = ''.join(map(lambda x: self.dict[x], self.seq))
        return self.__class__(self.name, compseq, self.strand, self.qual)

class fastqReader:
    """ 
    A class to read the name, sequence, strand and qualities from a fastq file

    file = the file name of a fastq file
    """
    def __init__(self, file):
        self.file = open(file, 'rU')
        self.read = read

    def __iter__(self):
        """ 
        Return read class: (name, sequence, strand, qualities).
        """
        for i, line in enumerate(self.file):
            if i % 4 == 0:
                name = line.strip()[1:]
            elif i % 4 == 1:
                sequence = line.strip()
            elif i % 4 == 2:
                strand = line.strip()
            elif i % 4 == 3:
                qualities = line.rstrip('\n\r')
                yield self.read(name, sequence, strand, qualities)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()

class fastqWriter:
    """ Take a read class object and file name, open file and write read """
    def __init__(self, file):
        self.file = open(file, 'w')

    def write(self, read):
        self.file.write('@' + read.name.split('/')[0] + '\n')
        self.file.write(read.seq + '\n')
        self.file.write(read.strand + '\n')
        self.file.write(read.qual + '\n')

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.file.close()
