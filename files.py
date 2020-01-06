# open a file
my_file = open("dna.txt")

# read a file
#file_contents = my_file.read()
#print (file_contents)

# read dna file
my_dna = my_file.read()
# calculate length
dna_length = len(my_dna)
# print
print("sequence is " + my_dna + "and length is " + str(dna_length))
# my_dna contains "\n" and has the wrong length ("\n" is counted)

# strip string of newline character
my_file = open("dna.txt")
my_file_contents = my_file.read()
# remove newline character
my_dna = my_file_contents.rstrip("\n")
dna_length = len(my_dna)
print("sequence is " + my_dna + " and length is " + str(dna_length))

# read the dna string and remove newline char in one line
my_dna = my_file.read().rstrip("\n")

# opening files that do not exist
# my_file = open("nonexistant.txt")
#Traceback (most recent call last):
#  File "files.py", line 28, in <module>
#    my_file = open("nonexistant.txt")
#FileNotFoundError: [Errno 2] No such file or directory: 'nonexistant.txt'

# writing output to a new file
my_out_file = open("output.txt", "w")
# open() has an additional optional argument, which can be
# "r", read an existing file
# "w", write to a new file
# "a", append to an existing file
# write a string to the new file
my_out_file.write("Hello World")
# write() can containing anything that returns a string
# write "abcdef"
my_out_file.write("abc" + "def")
# write "8"
my_out_file.write(str(len('AGTGCTAG')))
# write "TTGC"
my_out_file.write("ATGC".replace('A', 'T'))
# write "atgc"
my_out_file.write("ATGC".lower())

# closing an opened file
# this is important as not closing files can lead to errors that are hard to track down
my_out_file.close()

# open() can open files from anywhere on the computer
# you have to provide the absolute path
my_file = open("/Users/Joran/Documents/Code/Python/dna.txt")

# EXERCISES
# split genomic dna
my_file = open("genomic_dna.txt","r")
my_genomic_dna = my_file.read().rstrip("\n")
exon1 = my_genomic_dna[0:63]
exon2 = my_genomic_dna[91:]
intron1 = my_genomic_dna[63:91]
my_coding_file = open("coding_dna.txt","w")
my_noncoding_file = open("noncoding_dna.txt","w")
my_coding_file.write(">exon1" + "\n" + exon1 + "\n")
my_coding_file.write(">exon2" + "\n" + exon2 + "\n")
my_noncoding_file.write(">intron1" + "\n" + intron1 + "\n")

# a FASTA file
abc123 = "ATCGTACGATCGATCGATCGCTAGACGTATCG"
def456 = "actgatcgacgatcgatcgatcacgact"
hij789 = "ACTGAC-ACTGT--ACTGTA----CATGTG"
my_fasta_file = open("sequences.fasta", "w")
my_fasta_file.write(">ABC123" + "\n" + abc123.upper().replace("-","") + "\n")
my_fasta_file.write(">DEF456" + "\n" + def456.upper().replace("-","") + "\n")
my_fasta_file.write(">HIJ789" + "\n" + hij789.upper().replace("-","") + "\n")

# create multiple FASTA files
my_abc123_file = open("ABC123.fasta","w")
my_def456_file = open("DEF456.fasta","w")
my_hij789_file = open("HIJ789.fasta","w")
my_abc123_file.write(">ABC123" + "\n" + abc123.upper().replace("-","") + "\n")
my_def456_file.write(">DEF456" + "\n" + def456.upper().replace("-","") + "\n")
my_hij789_file.write(">HIJ789" + "\n" + hij789.upper().replace("-","") + "\n")
