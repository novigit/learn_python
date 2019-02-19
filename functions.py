# Example of a function
# def get_at_content(dna):
#     length = len(dna)
#     a_count = dna.count("A")
#     t_count = dna.count("T")
#     at_content = (a_count + t_count) / length
#     return at_content
# 'dna' holds whatever value it is given when the function is called
# a_count, t_count, at_content only exist within the body of the function

# improve the function
# def get_at_content(dna):
#     length = len(dna)
#
#     # force upper case, so function works with lower case letters
#     a_count = dna.upper().count('A')
#     t_count = dna.upper().count('T')
#     at_content = (a_count + t_count) / length
#
#     # round the output number, so it is always readable
#     return round(at_content, 2)

# generalize the function
# introduce additional argument, (number of significant figures)
# set a default number of significant figures
def get_at_content(dna, sig_figs=2):
    length = len(dna)
    a_count = dna.upper().count('A')
    t_count = dna.upper().count('T')
    at_content = (a_count + t_count) / length

    # additional argument is called here
    return round(at_content, sig_figs)

# call a function very explicitly
at = get_at_content(dna="ATCGTGACTCG", sig_figs=4)
print(str(at))
# remember to execute this function with python3 or higher!
# division doesnt work with vanilla python2

# test a function with 'assert'
assert get_at_content("ATGC") == 0.5
# this answer is wrong, which produces
# AssertionError
assert get_at_content("A") == 1
assert get_at_content("G") == 0
assert get_at_content("ATGC") == 0.5
assert get_at_content("AGG") == 0.33
assert get_at_content("AGG", 1) == 0.3
assert get_at_content("AGG", 5) == 0.33333
