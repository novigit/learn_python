## A STRING
# store a DNA sequence (a "string", in a "variable")
my_dna = "ATGCATGC"
# my_dna is a variable
# "ATGCATGC" is a string
# print the string
print(my_dna)
# oVerwrite the string and print it
my_dna = "GCATGCAT"
print(my_dna)
# variable names can only contain letters, numbers and underscores
# variable names can not start with a numbers
# variable names can not be words that are used in the python language, like print
## variable names are CASE SENSITIVE
#print(MY_DNA)
#Traceback (most recent call last):
#  File "strings.py", line 18, in <module>
#    print(MY_DNA)
#NameError: name 'MY_DNA' is not defined

## CONCATENATE STRINGS
# concatenate strings
my_dna = "AATT" + "GGCC"
print(my_dna)

## GET THE LENGTH OF A STRING
# measure the length of a strings and store in variable
dna_length = len("ATGC")
# dna_length stores the "return value"
print(dna_length)
# note that the return value is a number.
# PYTHON TREATS NUMBERS AND STRINGS DIFFERENTLY!!
#print("The length of the DNA sequence is " + dna_length)
#Traceback (most recent call last):
#  File "strings.py", line 34, in <module>
#    print("The length of the DNA sequence is " + dna_length)
#TypeError: Can't convert 'int' object to str implicitly
# str object = string objects
# int object = integer or number objects
# Thus, Python is unable to concatenate different type of objects!

## THE STR() AND INT() FUNCTIONS
# use the str() function to convert an integer object (int) into a string object (str)
print ("The length of the DNA sequence is " + str(dna_length))
# if just an int object, print() can print it directly
print(dna_length)
# use the int() function to convert an string object (str) into a integer object (int)
number = 3 + int("4")
# "4" is a str object, which is converted to 4 (int object)
print(number)

## CHANGE CASE
my_dna = "ATGC"
lower_case_my_dna = my_dna.lower()
print(lower_case_my_dna)
# .lower() is a METHOD. Methods apply to particular objects (here str) and return a new object
# in the () you can place arguments or options of the method (not specificied here)
# in other words, the str object hás the method lower(), while int objects do not have that method
upper_case_my_dna = lower_case_my_dna.upper()
print(upper_case_my_dna)

## PATTERN REPLACEMENT
my_protein = "vlspadktnv"
x = my_protein.replace("v", "y")
y = my_protein.replace("vls", "ymt")
print(x + "\n" + y)

## TAKING SUBSTRINGS
my_protein = "vlspadktnv"
# counting starts at 0! print the first residue
print(my_protein[0]) # "v"
# print from position 3 until position, but NOT including position 5.
print(my_protein[3:5]) # "pa"
# print from position 2 until the end
print(my_protein[2:]) # "spadktnv"

## COUNTING AND FINDING SUBSTRINGS
my_protein = "vlspadktnv"
# counting
# count() returns an int object
v_count = my_protein.count("v")
lsp_count = my_protein.count("lsp")
w_count = my_protein.count("w")
print("Valine count: " + str(v_count))
print("lsp count: " + str(lsp_count))
print("Tryptophan count: " + str(w_count))
# finding
# find() returns an int object (the position or index)
print(str(my_protein.find("v"))) # 0
print(str(my_protein.find("kt"))) # 6 (kt starts at index 6)
# if the pattern doesn't exist, it returns -1
print(str(my_protein.find("w"))) # -1

## EXERCISES
# calculate AT content
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
A_count = my_dna.count("A")
T_count = my_dna.count("T")
dna_length = len(my_dna)
AT_perc = ( A_count + T_count ) / dna_length * 100
print("AT content: ", str(AT_perc))

# reverse complement
my_dna = "ACTGATCGATTACGTATAGTATTTGCTATCATACATATATATCGATGCGTTCAT"
complement = my_dna.replace("A","t").replace("T","a").replace("C","g").replace("G","c").upper()
print(complement)
# [begin:end:step]
# [::-1] is a special case that reverses the string
revcomp = complement[::-1]
print(revcomp)

# restriction digestion fragments
my_dna = "ACTGATCGATTACGTATAGTAGAATTCTATCATACATATATATCGATGCGTTCAT"
EcoRI_site = "GAATTC"
cut_position = my_dna.find(EcoRI_site) + 1
print(my_dna)
print(len( my_dna[0:cut_position] ))
print(len( my_dna[cut_position:]  ))

# splicing out introns
# part 1
my_genomic_dna = "ATCGATCGATCGATCGACTGACTAGTCATAGCTATGCATGTAGCTACTCGATCGATCGATCGATCGATCGATCGATCGATCGATCATGCTATCATCGATCGATATCGATGCATCGACTACTAT"
exon1 = my_genomic_dna[0:63]
exon2 = my_genomic_dna[91:]
print(my_genomic_dna)
print(exon1 + exon2)
# part 2
percent_coding = len(exon1 + exon2) / len(my_genomic_dna) * 100
print(percent_coding)
# part 3
intron1 = my_genomic_dna[63:91]
print( exon1.upper() + intron1.lower() + exon2.upper() )
