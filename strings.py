# store a DNA sequence (a "string", in a "variable")
my_dna = "ATGCATGC"
# my_dna is a variable
# "ATGCATGC" is a string

# print the string
print(my_dna)

# overwrite the string and print it
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

# concatenate strings
my_dna = "AATT" + "GGCC"
print(my_dna)

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

# use the str() function to convert an integer object (int) into a string object (str)
print ("The length of the DNA sequence is " + str(dna_length))
# if just an int object, print() can print it directly
print(dna_length)

# use the int() function to convert an string object (str) into a integer object (int)
number = 3 + int("4")
# "4" is a str object, which is converted to 4 (int object)
print(number)
