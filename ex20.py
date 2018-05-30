# Imports the argv function from the sys module
from sys import argv
# Takes the passed values from when the program was called
# and assigns the prgram name to scripts and the passed
# file name to input_file.
script, input_file = argv

# Defines a functions called print_all which passed the
# parameter f. The parameter that is passed to the function
# is unique to the function. When called you would code
# print_all(input_file), input_file would be passed and
# used as f in the function.
def print_all(f):
    # Prints f (the file) with the read command.
    print(f.read())

# Defines a function called rewind. and passes a parameter, f.
def rewind(f):
    # Applies the seek command to the parameter (file)
    # that is passed into the function. The seek() method
    # sets the file current position. In this case will
    # go to the first position, "0".
    f.seek(0)

# Defines the function print_a_line and passes two
# parameters, line_count and f.
def print_a_line(line_count, f):
    # Will print the line_count and will read a line
    # in the file f (will go to EOF, since nothing is in the (),
    # readline will go to the EOL???.
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
