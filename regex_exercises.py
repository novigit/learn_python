import re

# exercise 1: screen strings for regexp matches
accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

# loop over list of strings
for acc in accessions:

    # has number 5
    if re.search(r'5', acc):
        print('5: ', acc)

    # has d or e
    if re.search(r'[de]', acc):
        print('d or e: ', acc)

    # has d and e in that order
    if re.search(r'd.*e', acc):
        print('d->e: ', acc)

    # has d, then any character, then e
    if re.search(r'd.{1}e', acc):
        print('d.e: ', acc)

    # has d followed by e, or e followed by d
    if re.search(r'(d.*e|e.*d)', acc):
        print('d->e or e->d: ', acc)

    # start with x or y
    if re.search(r'^[xy]', acc):
        print('start with x or y: ', acc)

    # start with x or y and end with e
    if re.search(r'^[xy]', acc):
        print("don't know the answer yet")

# exercise 2: restriction digestion
dna = open("dna_regex.txt").read()

# imaginary restriction enzymes
AbcI = r"A[ATGC]TAAT"
AbcII = r"GC[AG][AT]TG"
# regexp defining AbcI ór AbcII
Abc = r"(A[ATGC]TAAT|GC[AG][AT]TG)"

# find all restriction sites
sites = re.finditer(Abc, dna)

# loop over sites
positions = [0]
for site in sites:

    # identify exact site sequence
    seq = site.group()
    print(seq)

    # identify cleavage site
    if   re.search(AbcI,seq):
        cut_pos = site.start() + 3
    elif re.search(AbcII,seq):
        cut_pos = site.start() + 4

    # add cleavage site to list of positions
    positions.append(cut_pos)
# add final position
positions.append(len(dna))
print(positions)

# loop over position indices
for i in range(1,len(positions)):
    end_pos   = positions[i]
    start_pos = positions[i-1]
    seq = dna[start_pos:end_pos]
    print("Fragment size is: " + str(len(seq)) )
