## CONDITIONAL STATEMENTS
# numerical comparisons that return TRUE or FALSE
print(3 == 5)
print(3 > 5)
print(3 <=5)
print(len("ATGC") > 5)
print("GAATTC".count("T") > 1)

# functions that return TRUE or FALSE
print("ATGCTT".startswith("ATG"))
print("ATGCTT".endswith("TTT"))
print("ATGCTT".isupper())
print("ATGCTT".islower())

# Is String in List ?
print("V" in ["V", "W", "L"])

# == Equals
# > Greater then
# < Less then
# >= Greater or equal then
# <= Less or equal then
# != Not equals
# in Is value in list
# is are two objects the same ?

## IF STATEMENTS
# example: numerical comparison
expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")

# example: .startswith() function
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        print(accession)

## ELSE STATEMENTS
# example: numerical comparison
expression_level = 125
if expression_level > 100:
    print("gene is highly expressed")
else:
    print("gene is lowly expressed")

# example: .startswith() function
file1 = open("one.txt", "w")
file2 = open("two.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    else:
        file2.write(accession + "\n")

## ELIF STATEMENTS
file3 = open("three.txt", "w")
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a'):
        file1.write(accession + "\n")
    elif accession.startswith('b'):
        file2.write(accession + "\n")
    else:
        file3.write(accession + "\n")

# WHILE LOOP
count = 0
# 'while TRUE' do stuff
# loop will end when 'while FALSE'
while count<10:
    print(count)
    count = count + 1
# but in general not used so frequently in Python

# MULTIPLE CONDITIONAL STATEMENTS
# and
# if TRUE and TRUE, do stuff
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a') and accession.endswith('3'):
        print(accession)
# if TRUE and TRUE => TRUE
# if TRUE and FALSE => FALSE
# if FALSE and FALSE => FALSE

# or
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for accession in accs:
    if accession.startswith('a') or accession.startswith('b'):
        print(accession)
# if TRUE or TRUE => TRUE
# if TRUE or FALSE => TRUE
# if FALSE or FALSE => FALSE

# and & or
# usages of parentheses
# (X or Y) and Z : (X or Y) is first resolved, then 'and Z'
# X or (Y and Z) : (Y and Z) is first resolved, then 'X or'
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if (acc.startswith('a') or acc.startswith('b')) and acc.endswith('4'):
        print(acc)

# not
# returns the opposite boolean
# if TRUE and not TRUE => if TRUE and FALSE => FALSE
accs = ['ab56', 'bh84', 'hv76', 'ay93', 'ap97', 'bd72']
for acc in accs:
    if acc.startswith('a') and not acc.endswith('6'):
        print(acc)

# TRUE or FALSE statements in functions
def is_at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count("A")
    t_count = dna.upper().count("T")
    at_content = (a_count + t_count) / length
    if at_content > 0.65:
        return True
    else:
        return False

# test function
print(is_at_rich("ATTATCTACTA"))
print(is_at_rich("CGGCAGCGCT"))
assert is_at_rich("ATTATCTACTA") == True
assert is_at_rich("CGGCAGCGCT")  == False

# compacter version of the function
def is_at_rich(dna):
    length = len(dna)
    a_count = dna.upper().count("A")
    t_count = dna.upper().count("T")
    at_content = (a_count + t_count) / length

    # at_content > 0.65 returns either True or False, which is then returned by the function in turn
    return at_content > 0.65

# now possible to use function in if statement
sequence = "ATTATCTACTA"
if is_at_rich(sequence):
    print(sequence + " is AT rich")
