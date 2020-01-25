from sys import argv
from os.path import exists
#os is the module path is the subset of the module. We import the path section and import a single function that exists

script, from_file, to_file = argv #they are string object (from file) to_file

print(f"Copying from {from_file} to {to_file}")

 # we could do these two on one line, how?
in_file = open(from_file) #infile is a file handle,
indata = in_file.read() #indata is just a data string

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
out_file.write(indata) #this is when we want to write the string

print("Alright, all done.")

out_file.close()
in_file.close()
