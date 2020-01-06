in_file_obj  = open("input.txt", "r")
out_file_obj = open("input_output.txt","w")

for line in in_file_obj:
    adapter = line[0:14]
    #print(adapter)
    trimmed_seq = line.rstrip("\n").replace(adapter,"")
    out_file_obj.write(trimmed_seq + "\n")
