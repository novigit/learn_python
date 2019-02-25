file_obj = open("data.csv","r")

# store all lines in a list using the .readlines() function
lines = file_obj.readlines()

# make function to retrieve at_content
def get_at_content(dna):
    length = len(dna)
    a_count = dna.upper().count("A")
    t_count = dna.upper().count("T")
    at_content = (a_count + t_count ) / length
    return at_content

assert get_at_content("AATTGGCC") == 0.5

# loop over all lines of the file
for line in lines:

    # store data in string variables
    [species,seq,gene,expr] = line.rstrip("\n").split(",")
    gene_length = len(gene)

    # all genes from melanogaster and simulans
    if species == "Drosophila melanogaster" or species == "Drosophila simulans":
        print(gene + "\t" + species)

    # all genes between 90 and 110 bp long
    if gene_length > 90 and gene_length < 110:
        print(gene + "\t" + str(gene_length) + "\n")

    # all genes of AT-content < 50% and expression level > 200
    if get_at_content(seq) < 0.5 and int(expr) > 200:
        print(gene + " AT-content: " + str(get_at_content(seq)) + " Expression: " + expr)

    # all genes that start with k or h, and are not melanogaster
    if ( gene.startswith("k") or gene.startswith("h") ) and species != "Drosophila melanogaster":
        print(gene + "\t" + species)

    # state whether AT-content is low (<45%) medium (45-65%) or high (>65%)
    if get_at_content(seq) < .45:
        print("The AT-content of " + gene + " is low")
    elif get_at_content(seq) > .45 and get_at_content(seq) < .65:
        print("The AT-content of " + gene + " is medium")
    else:
        print("The AT-content of " + gene + " is high")
