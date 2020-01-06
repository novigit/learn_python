import os
import shutil

# check working directory
print(os.getcwd())
# set working directory
os.chdir("/Users/Joran/Documents/Code/Python/")

# create an empty file
open('old.txt', 'x').close()
# the argument 'x', allows open() to check if the file already exists. If it does, the open() will fail.
os.rename("old.txt","new.txt")
# assumes that old.txt is in the working directory
# also works on directory names
shutil.rmtree("testdir")
os.mkdir("testdir") # create a single directory
os.makedirs("testdir/testx/testy/testz") # create nested directories
# os.makedirs used to be os.mkdirs .

# copy a file
shutil.copy("one.txt","one_copy.txt")
# copy a directory and all its contents and subdirectories
shutil.copytree("testdir", "testdir_copy")
# check if a file exists
if os.path.exists("one.txt"):
    print("File exists!")

# remove a file
os.remove("one_copy.txt")
# remove an empty folder
os.mkdir("emptydir")
os.rmdir("emptydir")
# remove a non-empty folder
shutil.rmtree("testdir_copy")

# list the files of the current working directory
for file_name in os.listdir("."):
    print("I present you, file ", file_name)
# list the files of another directory
for file_name in os.listdir("/Users/Joran/Documents/Code/Rosalind"):
    print("I present you, file ", file_name)

# call an external program
import subprocess
subprocess.call("/bin/date")
# call the program with option and prints output to the screen
# date +"%B" returns July in bash
subprocess.call("date +%B",shell=True)
# call the program and store the returns
current_month = subprocess.check_output("date +%B", shell=True)

# capture program output
