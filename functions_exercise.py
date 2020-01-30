# function that accepts a single amino acid
def my_function(protein, amino_acid):
    protein_length = len(protein)
    amino_acid_count = protein.upper().count(amino_acid.upper())
    percentage = amino_acid_count / protein_length * 100
    return percentage


# test suite
assert my_function("MSRSLLLRFLLFLLLLPPLP", "M") == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", "r") == 10
assert my_function("msrslllrfllfllllpplp", "L") == 50
assert my_function("MSRSLLLRFLLFLLLLPPLP", "Y") == 0


# function that accepts a list of amino acids
# set default set of amino acids (hydrophobic residues)
def my_function(protein, amino_acids=["A", "I", "L", "M", "F", "W", "Y", "V"]):

    # get the length
    protein_length = len(protein)

    # count for each amino acid how often it occurs
    # and sum those counts
    sum = 0
    for amino_acid in amino_acids:
        upper_case_amino_acid = amino_acid.upper()
        amino_acid_count = protein.upper().count(upper_case_amino_acid)
        sum = sum + amino_acid_count

    # calculate percentage and round to 1 digit
    percentage = sum / protein_length * 100
    rounded_percentage = round(percentage, 1)

    return rounded_percentage


# test suite 2
assert my_function("MSRSLLLRFLLFLLLLPPLP", ["M"]) == 5
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['M', 'L']) == 55
assert my_function("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L']) == 70
assert my_function("MSRSLLLRFLLFLLLLPPLP") == 65
