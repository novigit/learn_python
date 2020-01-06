import re

# example
dna = "ATCGCGAATTCAC"
if re.search(r"GAATTC", dna):
    print("restriction site found!")
# r"" -> any backslash within the string is treated literally
# thus all regex special meanings are kept!

# example of using a regexp
# (A|G) is example of a alternation regexp
dna = "ATCGGGACCTCAC"
if re.search(r"GG(A|T)CC", dna):
    print("restriction site found!")
# or more explicit
avaII = r"GG(A|T)CC"
dna = "ATCGGGTCCTCAC"
if re.search(avaII, dna):
    print("restriction site found!")

# [ATGC] is example of a character group regexp
dna = "ATCGCGGCTCAC"
bisI = r"GC[ATGC]GC"
if re.search(bisI, dna):
    print("restriction site found!")

# re.search() technically returns a 'match object'
# which is interpreted as True in the conditional context
dna = "CGATNCGGAACGATC"
m = re.search(r"[^ATGC]", dna)

# m is now a 'match object'
# a match object contains the captured substring
if m:
    print("ambiguous base found!")
    ambig = m.group()
    print("the base is " + ambig)

# try in 1 go
dna = "CGATNCGGAACGATC"
ambig = re.search(r"[^ATGC]", dna).group()
print(ambig)

# capturing different parts of a matched string
scientific_name = "Homo sapiens"
m = re.search("(.+) (.+)", scientific_name)
if m:
    genus = m.group(1)
    species = m.group(2)
    print("genus is " + genus + ", species is " + species)

# a match object also contains the matched position indices
dna = "CGATNCGGAACGATC"
m = re.search(r"[^ATGC]", dna)
if m:
    print("ambiguous base found!")
    print("at position " + str(m.start()))

# or in 1 go
dna = "CGATNCGGAACGATC"
start = re.search(r"[^ATGC]", dna).start()
end = re.search(r"[^ATGC]", dna).end()
print(str(start))
print(str(end)) # remember 'end' is not included in Python

# find multiple matches
dna = "CGCTCNTAGATGCGCRATGACTGCAYTGC"
matches = re.finditer(r"[^ATGC]", dna)
for m in matches:
    base = m.group()
    pos  = m.start()
    print(base + " found at position " + str(pos))

# what if multiple matches, and you use re.search()
dna = "CGCTCNTAGATGCGCRATGACTGCAYTGC"
match = re.search(r"[^ATGC]", dna)
print(match.group(0))
# re.search() only returns a single match object, the first it encounters

# return all matched strings (a list of strings)
dna = "CTGCATTATATCGTACGAAATTATACGCGCG"
result = re.findall(r"[AT]{6,}", dna)
print(result)

# split a string into a list of strings using a regexp
# base split() doesn't allow for this
# re.split() does!
dna = "ACTNGCATRGCTACGTYACGATSCGAWTCG"
runs = re.split(r"[^ATGC]", dna)
print(runs)
