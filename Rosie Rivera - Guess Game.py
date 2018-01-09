import random

# Initializing Variables
number = random.randint(1, 50)
right_guess = False
turns_left = 5

# Describes exactly ONE turn. The while loop is the Game Controller.
while turns_left and right_guess is False:
    answer = int(input("The number I'm thinking of is 1-50. GUESS IT! "))
    if answer == number:
        print("GOOD JOB!")
        right_guess = True
    elif answer >=  number:
        print("lower")
        turns_left -= 1
    elif answer <= number:
        print("higher")
        turns_left -= 1
    if turns_left is 0:
        print("OOOOOOOOHHHHHHH You were close but not really the answer was %s..." % number)



# Generate a number
# Get a number (input) from the user
# Compare number to input
# Add "higher" or "lower"
# Add 5 guesses
