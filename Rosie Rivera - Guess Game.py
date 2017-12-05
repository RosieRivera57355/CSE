import random

str()
number = random.randint(1, 50)
print(number)

response = ""
while response != number:
    response = input("Guess the Number ")

print(number == str(random.randint(1, 50)))

# Generate a number
# Get a number (input) from the user
# Compare number to input
# Add "higher" or "lower"
# Add 5 guesses
