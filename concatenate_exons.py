exon_file_obj = open("exons.txt","r")
genome_file_obj = open("genomic_dna_exercise.txt","r")
concat_file_obj = open("concatenated_exons.txt", "w")

genome = genome_file_obj.read().rstrip("\n")
print(genome)

for line in exon_file_obj:

    # extract and store start and end exon coordinates
    [start_str,end_str] = line.rstrip("\n").split(",")
    start_int = int(start_str)
    end_int   = int(end_str)
    exon = genome[start_int:end_int]

    # write the exon to the outfile
    # it should automatically concatenate if you omit newlines
    concat_file_obj.write(exon)
