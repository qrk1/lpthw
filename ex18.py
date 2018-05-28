# This one is like your scripts with argv
# Creates a function called "print_two" which passes argsself.
# The *args functions like argv but for functions, *args must
# be in praenthesis to function. Unlike argv, the values for the variable are
# not passed at the command line when the program is run, rather they are passed
# when the function is called. This becomes a a two step (excessive process)
# (*args) will receives all parameters passed then see next line.

def print_two(*args):
# the passed parameters are then assigned to variables.
  arg1, arg2 = args
# Will print the value of each variable next to the the printed variable name.
  print(f"arg1: {arg1}, arg2: {arg2}")
# Ok, that *args is actually pointless, we can just This
# Here we define a function with passes two parameters.
def print_two_again(arg1, arg2):
# and we print the two values next to their name like function "print_two"
# this funciton is cleaner and uses less code.
    print(f"arg1: {arg1}, arg2: {arg2}")

# This just takes one arguement that is passed when called.
def print_one(arg1):
    # prints "arg1" with the actual value of arg1.
    print(f"arg1: {arg1}")

# This one takes no arguments, passes no values, prints a line of text,
# then returns nothing.
def print_none():
    print("I got nothin'.")

# call the print_two function and passes it the string values of
# "Zed" and "Shaw"
print_two("Zed", "Shaw")
# Calls the print_two_again and passes the the "Zed" "Shaw" parameters.
print_two_again("Zed", "Shaw")
# Calles the print_one function and passes the string value of "First!"
print_one("First!")
# Calls the function print_one and passes no parameters.
print_none()
