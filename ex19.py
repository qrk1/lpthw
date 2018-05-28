# Defines the function "cheese_and_crackers" and passes print_two
# parameters, cheese_count and boxes_of_crackers.
def cheese_and_crackers (cheese_count, boxes_of_crackers):
    # Prints the "You have XXX cheese" XXX is the the value
    # of cheese_count passed into the function.
    print(f"You have {cheese_count} cheese!")
    # Prints "You have XXX boxes of crackers" where XXX is the value
    # value of boxes_of_crackers that was passed into the function.
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Prints "Man that's enough for a party!"
    print("Man that's enough for a party!")
    # Prints "Get a blanket." and forces a carraige return.
    print("Get a blanket.\n")

# Will call the function cheese_and_crackers passing it
# the values of 20 and 30 after printing
# We can just give the function numbers directly:"
print("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)

# Will print "OR, we can use variables from our script:"
print("OR, we can use variables from our script:")
# Will assign 10 the variable amount_of_cheese
amount_of_cheese = 10
# Assigns 50 to the variable amount_of_crackers
amount_of_crackers = 50

# Calls the function cheese_and_crackers passing it amount_of_cheese
# values that were just assigned to the variables amount_of_cheese and
# amount_of_crackers.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints "We can even do math inside too:"
print("We can even do math inside too:")
# Calls the function cheese_and_crackers and passed it
# values that are the result of mathematical operations
cheese_and_crackers(10+20, 5+6)

# Prints "And we can combine the two, variables and math:"
print("And we can combine the two, variables and math:")
# Calls cheese_and_crackers and passes parameters that were obtained
# through the use of variables and math.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
