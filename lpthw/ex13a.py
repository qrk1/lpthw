# Will import the argv function formt he sys module
from sys import argv
# read the WYSS section for how to run this
# Will 'unpack' the arguments passed in the run command
# to each of the variables assigned program below.
# first variable will be reserved for the script name.

#number is pasing a number value that ener the program as a string
# the next line of code converts the string number to an integer
# value.
bobo, myDog, secondDog, catName, number = argv

#converts number to an integer then assigns the value to number

number = int(number)
print(number + 3)

#Asks the user to enter a name for a dog that will be assigned
# to the variable yourDog.
yourDog = input("What is your dog's name?")

#This line prints the name of the script. You do not put an variable
# in the run line, by default, the first variable is the
# that equals argv is the script name. Additionally, the
# script does not have to used in the program.
print("The script is called:",bobo)

print(f"Wow, {yourDog} is a great name for a Dog!")
print("My dog's name is:", myDog)
print("My other dog's name is:", secondDog)
print("and I have a cat too, his name is:", catName)
