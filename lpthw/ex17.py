# Imports the argv function form the sys module
from sys import argv
# Imports the exists function formt he os.path module
from os.path import exists

# Using the the argv function, script will be assigned the program name,
# from_file and # to_file will be assigned the values passed
# to it form the run line.
script, from_file, to_file = argv

# Prints using the format feature, will include from_file and to_file
print(f"Copying from {from_file} to {to_file}")

# We could do these two on one line, how? These two lines
# can be combine into one line by placing a semicolon
# between them. Opens from and assigns it to in_file.
###in_file = open(from_file)
# uses the read program on in_file and assigns that value
# to indata.
###indata = in_file.read()
indata = open(from_file).read()


# Will print (using the format feature) "The input file
# is {len(indata)} bytes long", whcih will also include
# the lenght of indata using the len() command.
print(f"The input file is {len(indata)} bytes long")

# Will print "Does the output file exist?" Followed by the
# a True or False, a Boolean based on the exisits
# function.
print(f"Does the output file exist? {exists(to_file)}")
# prints "Ready, hit RETURN to continue, CTRL-C to abort."
# to the screen.
print("Ready, hit RETURN to continue, CTRL-C to abort.")
# accepts the input (RETURN) from the user to allow the
# program to continue.
input()

# Opens to_file using the w modifier which opens it to write
# truncating it first.
out_file = open(to_file, 'w')
# write the contents of indata to out_file.
out_file.write(indata)

# prints "Allright, a;; done." on the screen.
print("Alright, all done.")
# Closes out_file
out_file.close()
# Closes in_file
#in_file.close()
