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
    # Prints "Get a blanket." but will not carraige return.
    print("Get a blanket.")

print("We can just give the function numbers directly:")
cheese_and_crackers (20, 30)

print("OR, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
