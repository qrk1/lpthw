#import the argv function from the sys module
from sys import argv

# assigns the variables that argv will use. The first one is
# reserved for the name of the script (program), that variable
# can be any names allowed in Python, does not have to be script.
script, user_name = argv

#creates a variable and assigns the string "> " to it.
prompt = '"'

# The two lines below are part of the program but were added to
# confirm if the syntax below was allowed in Python 3. The syntax
# below assign a=0 and b=1.
a, b = 0, 1
print(f"a={a} and b={b}")
#prints the user_name which was passed through the argv arguement
# this uses the f format feature
print(f"Hi {user_name}, I'm the {script}.")

# Prints "I'd like to ask you a few questions." tot he console
print("I'd like to ask you a few questions.")
# Prints "Do you like me" followed by the user_name that was
# passed at the run command.
print(f"Do you like me {user_name}?")
# Takes the input from the user using the prompt define above.
likes = input(prompt)

# Prints "Where do you live" followed by the user_name
print(f"Where do you live {user_name}?")
#Takes input from the user and assigns it to the variable "lives"
lives = input(prompt)

# prints "What kind of computer do you have?" to the screen.
print("What kind of computer do you have?")
# Takes an input from the user and assigns it to the variable "computer"
computer = input(prompt)

# Prints to the screen using the f format function/feature
# also uses tripple " which allows for the use hard returns
# and spacing.
print(f"""
Alright, so you said {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
