import random

str()
number = random.randint(1, 50)
print(number)

response = ""
while response != number:
    response = input("Guess the Number ")
