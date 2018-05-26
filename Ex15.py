# Imports the argv module/function from the sys module.
from sys import argv

# Assigns the values that were passed in to variable that can
# be used in the program, first variable, the name of the script,
# does not have to be passed but has to be included in the list
# of variables. In this program the filename to be passed
# is the actual file name to be used in program/script
script, filename = argv

# Opens the filename that was passed into the variable filename and
# assigns it to the variable txt.
txt = open(filename)

# Prints, "Here's your file" immediately followed by the filename passed
# uses the f format feature.
print(f"Here's your file {filename}:")

# This lines prints the value of txt after it reads it from the
# files. txt by itself will give information about the files
# to get the contents of the file to print to the screen
# you have to invoke the .read() command.
print(txt.read())

# Will print "Type the filename again:" to the screen
print("Type the filename again:")

# Will assign the user input of the filename to the variable
# file_again.
file_again = input("> ")

# Assigns the contents to the file input by the user to
# the variable txt_again.
txt_again = open(file_again)

# Will print txt_again after it reads the file (not just give
# information on it).
print(txt_again.read())
