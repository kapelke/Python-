from sys import argv
from os.path import exists
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

#we could do these two on one line, how?

in_file = open(from_file)

print(">>>> in_file=", repr(in_file))
indata = in_file.read()

print(f"The input file is {len(indata)} byes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, Hit CTRL-C to cancel or enter to continue.")
input()

out_file = open(to_file, 'w')
out_file.write(indata)

print ("Alright, all done.")

out_file.close
in_file.close
