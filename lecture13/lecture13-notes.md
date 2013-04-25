% Hello web: Accessing databases and APIs using Biopython
% Matt Shirley (matt.shirley@jhmi.edu)
% 25 April 2013




# What is Biopython?

- [Biopython](http://biopython.org) is a Python module providing a collection of
useful tools for:
    - parsing bioinformatics file formats
	- structured, object-oriented access to bioinformatics data
	- interfacing with online bioinformatics databases
	- methods for common bioinformatics data manipulations

# Installing Biopython

- Windows
    - Download the [appropriate installer](http://biopython.org/wiki/Download) for your version of Python
- Mac & Linux
    - Easy option: from a terminal execute `sudo pip install Biopython`. If `pip` is not installed, try `easy_install`.
	- Harder option: Download the [source tarball](http://biopython.org/DIST/biopython-1.61.tar.gz) and follow the
compilation instructions.

To test whether you successfully installed Biopython, run `python -c 'import Bio'`. If you don't see an error message,
you're done.

# Simple example: the Seq class


```python
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq('ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG', generic_dna)
print str(dna)

rna = dna.transcribe()
print str(rna)

prot = dna.translate()
print str(prot)
```

```
## ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG
## AUGGGGUUCGAUCGUCCUUUCCCAGCUCUGACUAG
## MGFDRPFPALT
```


# Seq class methods


```python
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq('ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG', generic_dna)
print str(dna)
print str(dna.complement())
print str(dna.reverse_complement())

prot = dna.translate()
print str(prot)
try:
    prot.complement()
except ValueError, e:
    print e
```

```
## ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG
## TACCCCAAGCTAGCAGGAAAGGGTCGAGACTGATC
## CTAGTCAGAGCTGGGAAAGGACGATCGAACCCCAT
## MGFDRPFPALT
## Proteins do not have complements!
```


Why can we not complement a *Protein*? Simple: Biopython Seq objects have an
"alphabet" associated with them that prevents you from doing such silly things.

# Counting bases method: GC content example


```python
from Bio.Seq import Seq
from Bio.Alphabet import generic_dna

dna = Seq('ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG', generic_dna)
comp = dna.complement()
print str(dna)
print [(base, dna.count(base)) for base in ['A','C','T','G']]
print [(base, comp.count(base)) for base in ['A','C','T','G']]
```

```
## ATGGGGTTCGATCGTCCTTTCCCAGCTCTGACTAG
## [('A', 5), ('C', 10), ('T', 11), ('G', 9)]
## [('A', 11), ('C', 9), ('T', 5), ('G', 10)]
```


Note that you don't really need Biopython for this, except for the complement function.

# Querying Entrez


```python
from textwrap import fill
from Bio import Entrez
Entrez.email = 'matt.shirley@jhmi.edu'

query = Entrez.einfo()
result = Entrez.read(query)
keys = result.keys()
print keys
results = ' '.join(result['DbList'])
print fill(results, 60)
```

```
## [u'DbList']
## pubmed protein nuccore nucleotide nucgss nucest structure
## genome assembly gcassembly genomeprj bioproject biosample
## biosystems blastdbinfo books cdd clinvar clone gap gapplus
## dbvar epigenomics gene gds geoprofiles homologene journals
## medgen mesh ncbisearch nlmcatalog omia omim pmc popset probe
## proteinclusters pcassay pccompound pcsubstance pubmedhealth
## seqannot snp sra taxonomy toolkit toolkitall toolkitbook
## unigene unists gencoll
```


Use `einfo()` to list the properties of each database. In this example, we return a
result listing all of the available databases to query.

# Querying a specific database in Entrez


```python
from textwrap import fill
from Bio import Entrez
Entrez.email = 'matt.shirley@jhmi.edu'

query = Entrez.einfo(db='pubmed')
result = Entrez.read(query)
keys = result.keys()
print keys
results = ' '.join(result['DbInfo'])
print fill(results, 60)
print result['DbInfo']['Count']
```

```
## [u'DbInfo']
## Count LastUpdate MenuName Description LinkList FieldList
## DbName
## 22690440
```


# Listing our search terms


```python
from Bio import Entrez
Entrez.email = 'matt.shirley@jhmi.edu'

query = Entrez.einfo(db='pubmed')
result = Entrez.read(query)
fieldlist = result['DbInfo']['FieldList']
for field in fieldlist:
    print '%(Name)s, %(FullName)s, %(Description)s' % field
```

```
## ALL, All Fields, All terms from all searchable fields
## UID, UID, Unique number assigned to publication
## FILT, Filter, Limits the records
## TITL, Title, Words in title of publication
## WORD, Text Word, Free text associated with publication
## MESH, MeSH Terms, Medical Subject Headings assigned to publication
## MAJR, MeSH Major Topic, MeSH terms of major importance to publication
## AUTH, Author, Author(s) of publication
## JOUR, Journal, Journal abbreviation of publication
## AFFL, Affiliation, Author's institutional affiliation and address
## ECNO, EC/RN Number, EC number for enzyme or CAS registry number
## SUBS, Supplementary Concept, CAS chemical name or MEDLINE Substance Name
## PDAT, Date - Publication, Date of publication
## EDAT, Date - Entrez, Date publication first accessible through Entrez
## VOL, Volume, Volume number of publication
## PAGE, Pagination, Page number(s) of publication
## PTYP, Publication Type, Type of publication (e.g., review)
## LANG, Language, Language of publication
## ISS, Issue, Issue number of publication
## SUBH, MeSH Subheading, Additional specificity for MeSH term
## SI, Secondary Source ID, Cross-reference from publication to other databases
## MHDA, Date - MeSH, Date publication was indexed with MeSH terms
## TIAB, Title/Abstract, Free text associated with Abstract/Title
## OTRM, Other Term, Other terms associated with publication
## INVR, Investigator, Investigator
## COLN, Author - Corporate, Corporate Author of publication
## CNTY, Place of Publication, Country of publication
## PAPX, Pharmacological Action, MeSH pharmacological action pre-explosions
## GRNT, Grant Number, NIH Grant Numbers
## MDAT, Date - Modification, Date of last modification
## CDAT, Date - Completion, Date of completion
## PID, Publisher ID, Publisher ID
## FAUT, Author - First, First Author of publication
## FULL, Author - Full, Full Author Name(s) of publication
## FINV, Investigator - Full, Full name of investigator
## TT, Transliterated Title, Words in transliterated title of publication
## LAUT, Author - Last, Last Author of publication
## PPDT, Print Publication Date, Date of print publication
## EPDT, Electronic Publication Date, Date of Electronic publication
## LID, Location ID, ELocation ID
## CRDT, Date - Create, Date publication first accessible through Entrez
## BOOK, Book, ID of the book that contains the document
## ED, Editor, Section's Editor
## ISBN, ISBN, ISBN
## PUBN, Publisher, Publisher's name
## AUCL, Author Cluster ID, Author Cluster ID
## EID, Extended PMID, Extended PMID
```


# Searching PubMed

Use `Entrez.esearch` to actually search one of the databases, providing
a search query term using the fields we identified using `Entrez.einfo`.


```python
from Bio import Entrez
Entrez.email = 'matt.shirley@jhmi.edu'

query = Entrez.esearch(db='pubmed', \
term='Shirley M[AUTH] AND Johns Hopkins School of Medicine[AFFL]')
result = Entrez.read(query)
print result['Count']
print result['IdList']
```

```
## 3
## ['23549483', '23185369', '22374857']
```

Dang. Only three publications as of:


```
## 2013-04-24
```


# Searching Nucleotide

Use `Entrez.efetch` to return a result from an accession number. Here we're grabbing
the FASTA format sequence from a GenBank accession.


```python
from Bio import Entrez
Entrez.email = 'matt.shirley@jhmi.edu'

query = Entrez.efetch(db='nucleotide', \
id='312176363', \
rettype='gb', \
retmode='text')
sequence = query.read()
print sequence
with open('example.gb', 'w') as out:
    out.write(sequence)
```

```
## LOCUS       NM_002072               2215 bp    mRNA    linear   PRI 17-APR-2013
## DEFINITION  Homo sapiens guanine nucleotide binding protein (G protein), q
##             polypeptide (GNAQ), mRNA.
## ACCESSION   NM_002072
## VERSION     NM_002072.3  GI:312176363
## KEYWORDS    .
## SOURCE      Homo sapiens (human)
##   ORGANISM  Homo sapiens
##             Eukaryota; Metazoa; Chordata; Craniata; Vertebrata; Euteleostomi;
##             Mammalia; Eutheria; Euarchontoglires; Primates; Haplorrhini;
##             Catarrhini; Hominidae; Homo.
## REFERENCE   1  (bases 1 to 2215)
##   AUTHORS   Xiang,B., Zhang,G., Stefanini,L., Bergmeier,W., Gartner,T.K.,
##             Whiteheart,S.W. and Li,Z.
##   TITLE     The Src family kinases and protein kinase C synergize to mediate
##             Gq-dependent platelet activation
##   JOURNAL   J. Biol. Chem. 287 (49), 41277-41287 (2012)
##    PUBMED   23066026
##   REMARK    GeneRIF: Src family kinases, PI3 kinase and protein kinase C
##             synergize to mediate Gq-dependent platelet activation
## REFERENCE   2  (bases 1 to 2215)
##   AUTHORS   Daniels,A.B., Lee,J.E., MacConaill,L.E., Palescandolo,E., Van
##             Hummelen,P., Adams,S.M., DeAngelis,M.M., Hahn,W.C., Gragoudas,E.S.,
##             Harbour,J.W., Garraway,L.A. and Kim,I.K.
##   TITLE     High throughput mass spectrometry-based mutation profiling of
##             primary uveal melanoma
##   JOURNAL   Invest. Ophthalmol. Vis. Sci. 53 (11), 6991-6996 (2012)
##    PUBMED   22977135
##   REMARK    GeneRIF: The vast majority of primary large uveal melanomas harbor
##             mutually-exclusive mutations in GNAQ or GNA11, but very rarely have
##             the oncogenic mutations that are reported commonly in other
##             cancers.
##             Publication Status: Online-Only
## REFERENCE   3  (bases 1 to 2215)
##   AUTHORS   Drastichova,Z. and Novotny,J.
##   TITLE     Identification and subcellular localization of molecular complexes
##             of Gq/11alpha protein in HEK293 cells
##   JOURNAL   Acta Biochim. Biophys. Sin. (Shanghai) 44 (8), 641-649 (2012)
##    PUBMED   22710260
##   REMARK    GeneRIF: analysis of molecular complexes of Gq/11alpha protein in
##             HEK293 cells
## REFERENCE   4  (bases 1 to 2215)
##   AUTHORS   Golebiewska,U., Guo,Y., Khalikaprasad,N., Zurawsky,C.,
##             Yerramilli,V.S. and Scarlata,S.
##   TITLE     gamma-Synuclein interacts with phospholipase Cbeta2 to modulate G
##             protein activation
##   JOURNAL   PLoS ONE 7 (8), E41067 (2012)
##    PUBMED   22905097
##   REMARK    GeneRIF: gamma-synuclein has a role in promoting a more robust G
##             protein Galphaq activation of PLCbeta2
## REFERENCE   5  (bases 1 to 2215)
##   AUTHORS   Svensson,L., Stanley,P., Willenbrock,F. and Hogg,N.
##   TITLE     The Galphaq/11 proteins contribute to T lymphocyte migration by
##             promoting turnover of integrin LFA-1 through recycling
##   JOURNAL   PLoS ONE 7 (6), E38517 (2012)
##    PUBMED   22701657
##   REMARK    GeneRIF: Vesicle-associated Galphaq/11 is required for the turnover
##             of LFA-1 adhesion that is necessary for immune cell migration.
## REFERENCE   6  (bases 1 to 2215)
##   AUTHORS   Dong,Q., Shenker,A., Way,J., Haddad,B.R., Lin,K., Hughes,M.R.,
##             McBride,O.W., Spiegel,A.M. and Battey,J.
##   TITLE     Molecular cloning of human G alpha q cDNA and chromosomal
##             localization of the G alpha q gene (GNAQ) and a processed
##             pseudogene
##   JOURNAL   Genomics 30 (3), 470-475 (1995)
##    PUBMED   8825633
## REFERENCE   7  (bases 1 to 2215)
##   AUTHORS   Lesch,K.P. and Manji,H.K.
##   TITLE     Signal-transducing G proteins and antidepressant drugs: evidence
##             for modulation of alpha subunit gene expression in rat brain
##   JOURNAL   Biol. Psychiatry 32 (7), 549-579 (1992)
##    PUBMED   1333286
## REFERENCE   8  (bases 1 to 2215)
##   AUTHORS   Berstein,G., Blank,J.L., Jhon,D.Y., Exton,J.H., Rhee,S.G. and
##             Ross,E.M.
##   TITLE     Phospholipase C-beta 1 is a GTPase-activating protein for Gq/11,
##             its physiologic regulator
##   JOURNAL   Cell 70 (3), 411-418 (1992)
##    PUBMED   1322796
## REFERENCE   9  (bases 1 to 2215)
##   AUTHORS   Shenker,A., Goldsmith,P., Unson,C.G. and Spiegel,A.M.
##   TITLE     The G protein coupled to the thromboxane A2 receptor in human
##             platelets is a member of the novel Gq family
##   JOURNAL   J. Biol. Chem. 266 (14), 9309-9313 (1991)
##    PUBMED   1851174
## REFERENCE   10 (bases 1 to 2215)
##   AUTHORS   Banno,Y., Yada,Y. and Nozawa,Y.
##   TITLE     Purification and characterization of membrane-bound phospholipase C
##             specific for phosphoinositides from human platelets
##   JOURNAL   J. Biol. Chem. 263 (23), 11459-11465 (1988)
##    PUBMED   2841328
## COMMENT     REVIEWED REFSEQ: This record has been curated by NCBI staff. The
##             reference sequence was derived from DB474490.1, BC069520.1,
##             BC057777.1 and CV570171.1.
##             This sequence is a reference standard in the RefSeqGene project.
##             On Nov 17, 2010 this sequence version replaced gi:40254461.
##             
##             Summary: This locus encodes a guanine nucleotide-binding protein.
##             The encoded protein, an alpha subunit in the Gq class, couples a
##             seven-transmembrane domain receptor to activation of phospolipase
##             C-beta. Mutations at this locus have been associated with problems
##             in platelet activation and aggregation. A related pseudogene exists
##             on chromosome 2.[provided by RefSeq, Nov 2010].
##             
##             Publication Note:  This RefSeq record includes a subset of the
##             publications that are available for this gene. Please see the Gene
##             record to access additional publications.
##             
##             ##Evidence-Data-START##
##             Transcript exon combination :: BC057777.1, U43083.1 [ECO:0000332]
##             RNAseq introns              :: single sample supports all introns
##                                            ERS025084 [ECO:0000348]
##             ##Evidence-Data-END##
## PRIMARY     REFSEQ_SPAN         PRIMARY_IDENTIFIER PRIMARY_SPAN        COMP
##             1-1                 DB474490.1         1-1
##             2-1361              BC069520.1         1-1360
##             1362-2098           BC057777.1         1335-2071
##             2099-2099           CV570171.1         220-220
##             2100-2215           BC057777.1         2073-2188
## FEATURES             Location/Qualifiers
##      source          1..2215
##                      /organism="Homo sapiens"
##                      /mol_type="mRNA"
##                      /db_xref="taxon:9606"
##                      /chromosome="9"
##                      /map="9q21"
##      gene            1..2215
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /note="guanine nucleotide binding protein (G protein), q
##                      polypeptide"
##                      /db_xref="GeneID:2776"
##                      /db_xref="HGNC:4390"
##                      /db_xref="MIM:600998"
##      exon            1..204
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=1
##      STS             51..1167
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /db_xref="UniSTS:482300"
##      CDS             69..1148
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /note="guanine nucleotide-binding protein alpha-q"
##                      /codon_start=1
##                      /product="guanine nucleotide-binding protein G(q) subunit
##                      alpha"
##                      /protein_id="NP_002063.2"
##                      /db_xref="GI:40254462"
##                      /db_xref="CCDS:CCDS6658.1"
##                      /db_xref="GeneID:2776"
##                      /db_xref="HGNC:4390"
##                      /db_xref="MIM:600998"
##                      /translation="MTLESIMACCLSEEAKEARRINDEIERQLRRDKRDARRELKLLL
##                      LGTGESGKSTFIKQMRIIHGSGYSDEDKRGFTKLVYQNIFTAMQAMIRAMDTLKIPYK
##                      YEHNKAHAQLVREVDVEKVSAFENPYVDAIKSLWNDPGIQECYDRRREYQLSDSTKYY
##                      LNDLDRVADPAYLPTQQDVLRVRVPTTGIIEYPFDLQSVIFRMVDVGGQRSERRKWIH
##                      CFENVTSIMFLVALSEYDQVLVESDNENRMEESKALFRTIITYPWFQNSSVILFLNKK
##                      DLLEEKIMYSHLVDYFPEYDGPQRDAQAAREFILKMFVDLNPDSDKIIYSHFTCATDT
##                      ENIRFVFAAVKDTILQLNLKEYNLV"
##      exon            205..389
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=2
##      exon            390..544
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=3
##      exon            545..673
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=4
##      exon            674..803
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=5
##      exon            804..957
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=6
##      exon            958..2198
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /inference="alignment:Splign:1.39.8"
##                      /number=7
##      STS             1596..1815
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /standard_name="A002Y36"
##                      /db_xref="UniSTS:59945"
##      STS             1977..2180
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##                      /standard_name="SHGC-53345"
##                      /db_xref="UniSTS:63543"
##      polyA_signal    2168..2173
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
##      polyA_site      2198
##                      /gene="GNAQ"
##                      /gene_synonym="G-ALPHA-q; GAQ"
## ORIGIN      
##         1 gggagggtgt gtgtgcgcgc tgtgagcagg gggtgccggc ggggctgcag cggaggcact
##        61 ttggaagaat gactctggag tccatcatgg cgtgctgcct gagcgaggag gccaaggaag
##       121 cccggcggat caacgacgag atcgagcggc agctccgcag ggacaagcgg gacgcccgcc
##       181 gggagctcaa gctgctgctg ctcgggacag gagagagtgg caagagtacg tttatcaagc
##       241 agatgagaat catccatggg tcaggatact ctgatgaaga taaaaggggc ttcaccaagc
##       301 tggtgtatca gaacatcttc acggccatgc aggccatgat cagagccatg gacacactca
##       361 agatcccata caagtatgag cacaataagg ctcatgcaca attagttcga gaagttgatg
##       421 tggagaaggt gtctgctttt gagaatccat atgtagatgc aataaagagt ttatggaatg
##       481 atcctggaat ccaggaatgc tatgatagac gacgagaata tcaattatct gactctacca
##       541 aatactatct taatgacttg gaccgcgtag ctgaccctgc ctacctgcct acgcaacaag
##       601 atgtgcttag agttcgagtc cccaccacag ggatcatcga ataccccttt gacttacaaa
##       661 gtgtcatttt cagaatggtc gatgtagggg gccaaaggtc agagagaaga aaatggatac
##       721 actgctttga aaatgtcacc tctatcatgt ttctagtagc gcttagtgaa tatgatcaag
##       781 ttctcgtgga gtcagacaat gagaaccgaa tggaggaaag caaggctctc tttagaacaa
##       841 ttatcacata cccctggttc cagaactcct cggttattct gttcttaaac aagaaagatc
##       901 ttctagagga gaaaatcatg tattcccatc tagtcgacta cttcccagaa tatgatggac
##       961 cccagagaga tgcccaggca gcccgagaat tcattctgaa gatgttcgtg gacctgaacc
##      1021 cagacagtga caaaattatc tactcccact tcacgtgcgc cacagacacc gagaatatcc
##      1081 gctttgtctt tgctgccgtc aaggacacca tcctccagtt gaacctgaag gagtacaatc
##      1141 tggtctaatt gtgcctccta gacacccgcc ctgcccttcc ctggtgggct attgaagata
##      1201 cacaagaggg actgtatttc tgtggaaaac aatttgcata atactaattt attgccgtcc
##      1261 tggactctgt gtgagcgtgt ccacagagtt tgtagtaaat attatgattt tatttaaact
##      1321 attcagagga aaaacagagg atgctgaagt acagtcccag cacatttcct ctctatcttt
##      1381 tttttaggca aaaccttgtg actcagtgta ttttaaattc tcagtcatgc actcacaaag
##      1441 ataagacttg tttctttctg tctctctctc tttttctttt ctatggagca aaacaaagct
##      1501 gatttccctt ttttcttccc ccgctaattc atacctccct cctgatgttt ttcccaggtt
##      1561 acaatggcct ttatcctagt tccattcttg gtcaagtttt tctctcaaat gatacagtca
##      1621 ggacacatcg ttcgatttaa gccatcatca gcttaattta agtttgtagt ttttgctgaa
##      1681 ggattatatg tattaatact tacggtttta aatgtgttgc tttggataca cacatagttt
##      1741 cttttttaat agaatatact gtcttgtctc actttggact gggacagtgg atgcccatct
##      1801 aaaagttaag tgtcatttct tttagatgtt taccttcagc catagcttga ttgctcagag
##      1861 aaatatgcag aaggcaggat caaagacaca caggagtcct ttcttttgaa atgccacgtg
##      1921 ccattgtctt tcctcccttc tttgcttctt tttcttaccc tctctttcaa ttgcagatgc
##      1981 caaaaaagat gccaacagac actacattac cctaatggct gctacccaga acctttttat
##      2041 aggttgttct taattttttt gttgttgttg ttcaagcttt tcctttcttt tttttcttgg
##      2101 tgtttgggcc acgattttaa aatgactttt attatgggta tgtgttgcca aagctggctt
##      2161 tttgtcaaat aaaatgaata cgaacttaaa aaataaaaaa aaaaaaaaaa aaaaa
## //
```


# Converting file types


```python
from Bio import SeqIO
count = SeqIO.convert('example.gb', 'genbank', 'example.fasta', 'fasta')
print 'converted {0} records'.format(count)
```

```
## converted 1 records
```


# Reading sequence files


```python
from textwrap import fill
from Bio import SeqIO
with open('example.fasta', 'rU') as infile:
    sequence = SeqIO.read(infile, 'fasta')
print sequence.id
print fill(str(sequence.seq))
```

```
## NM_002072.3
## GGGAGGGTGTGTGTGCGCGCTGTGAGCAGGGGGTGCCGGCGGGGCTGCAGCGGAGGCACTTTGGAAGAAT
## GACTCTGGAGTCCATCATGGCGTGCTGCCTGAGCGAGGAGGCCAAGGAAGCCCGGCGGATCAACGACGAG
## ATCGAGCGGCAGCTCCGCAGGGACAAGCGGGACGCCCGCCGGGAGCTCAAGCTGCTGCTGCTCGGGACAG
## GAGAGAGTGGCAAGAGTACGTTTATCAAGCAGATGAGAATCATCCATGGGTCAGGATACTCTGATGAAGA
## TAAAAGGGGCTTCACCAAGCTGGTGTATCAGAACATCTTCACGGCCATGCAGGCCATGATCAGAGCCATG
## GACACACTCAAGATCCCATACAAGTATGAGCACAATAAGGCTCATGCACAATTAGTTCGAGAAGTTGATG
## TGGAGAAGGTGTCTGCTTTTGAGAATCCATATGTAGATGCAATAAAGAGTTTATGGAATGATCCTGGAAT
## CCAGGAATGCTATGATAGACGACGAGAATATCAATTATCTGACTCTACCAAATACTATCTTAATGACTTG
## GACCGCGTAGCTGACCCTGCCTACCTGCCTACGCAACAAGATGTGCTTAGAGTTCGAGTCCCCACCACAG
## GGATCATCGAATACCCCTTTGACTTACAAAGTGTCATTTTCAGAATGGTCGATGTAGGGGGCCAAAGGTC
## AGAGAGAAGAAAATGGATACACTGCTTTGAAAATGTCACCTCTATCATGTTTCTAGTAGCGCTTAGTGAA
## TATGATCAAGTTCTCGTGGAGTCAGACAATGAGAACCGAATGGAGGAAAGCAAGGCTCTCTTTAGAACAA
## TTATCACATACCCCTGGTTCCAGAACTCCTCGGTTATTCTGTTCTTAAACAAGAAAGATCTTCTAGAGGA
## GAAAATCATGTATTCCCATCTAGTCGACTACTTCCCAGAATATGATGGACCCCAGAGAGATGCCCAGGCA
## GCCCGAGAATTCATTCTGAAGATGTTCGTGGACCTGAACCCAGACAGTGACAAAATTATCTACTCCCACT
## TCACGTGCGCCACAGACACCGAGAATATCCGCTTTGTCTTTGCTGCCGTCAAGGACACCATCCTCCAGTT
## GAACCTGAAGGAGTACAATCTGGTCTAATTGTGCCTCCTAGACACCCGCCCTGCCCTTCCCTGGTGGGCT
## ATTGAAGATACACAAGAGGGACTGTATTTCTGTGGAAAACAATTTGCATAATACTAATTTATTGCCGTCC
## TGGACTCTGTGTGAGCGTGTCCACAGAGTTTGTAGTAAATATTATGATTTTATTTAAACTATTCAGAGGA
## AAAACAGAGGATGCTGAAGTACAGTCCCAGCACATTTCCTCTCTATCTTTTTTTTAGGCAAAACCTTGTG
## ACTCAGTGTATTTTAAATTCTCAGTCATGCACTCACAAAGATAAGACTTGTTTCTTTCTGTCTCTCTCTC
## TTTTTCTTTTCTATGGAGCAAAACAAAGCTGATTTCCCTTTTTTCTTCCCCCGCTAATTCATACCTCCCT
## CCTGATGTTTTTCCCAGGTTACAATGGCCTTTATCCTAGTTCCATTCTTGGTCAAGTTTTTCTCTCAAAT
## GATACAGTCAGGACACATCGTTCGATTTAAGCCATCATCAGCTTAATTTAAGTTTGTAGTTTTTGCTGAA
## GGATTATATGTATTAATACTTACGGTTTTAAATGTGTTGCTTTGGATACACACATAGTTTCTTTTTTAAT
## AGAATATACTGTCTTGTCTCACTTTGGACTGGGACAGTGGATGCCCATCTAAAAGTTAAGTGTCATTTCT
## TTTAGATGTTTACCTTCAGCCATAGCTTGATTGCTCAGAGAAATATGCAGAAGGCAGGATCAAAGACACA
## CAGGAGTCCTTTCTTTTGAAATGCCACGTGCCATTGTCTTTCCTCCCTTCTTTGCTTCTTTTTCTTACCC
## TCTCTTTCAATTGCAGATGCCAAAAAAGATGCCAACAGACACTACATTACCCTAATGGCTGCTACCCAGA
## ACCTTTTTATAGGTTGTTCTTAATTTTTTTGTTGTTGTTGTTCAAGCTTTTCCTTTCTTTTTTTTCTTGG
## TGTTTGGGCCACGATTTTAAAATGACTTTTATTATGGGTATGTGTTGCCAAAGCTGGCTTTTTGTCAAAT
## AAAATGAATACGAACTTAAAAAATAAAAAAAAAAAAAAAAAAAAA
```


# Writing sequence files


```python
from Bio import SeqIO
with open('example.fasta', 'rU') as infile:
    sequence = SeqIO.read(infile, 'fasta')
sequence.seq = sequence.seq.translate()
print sequence.seq[:36]
with open('example_prot.fasta', 'w') as out:
    SeqIO.write(sequence, out, 'fasta')
```

```
## GRVCVRAVSRGCRRGCSGGTLEE*LWSPSWRAA*AR
```


Reading our example FASTA file, translating it to protein,
then writing a new FASTA file.

# Questions?

There's no homework this week. Let's use this extra time to discuss your
final project proposals and go through any issues with last week's homework.
