import random  # imports should be at the top of your program

# print("Hello World!")
#
# # RosaMariaRivera
#
# print(3+5)
#
# print(5-3)
#
# print(5*3)
#
# print(6/2)
#
# print(3 ** 2)
#
# print() # Creates a blank line
#
# print("See if you can figure this out...")
#
# print(30 % 12)
#
# # Variables
#
# car_name = "Wiebe Mobile"
#
# car_type = "Lamborghini Sesto Elemento"
#
# car_cylinders = 8
#
# car_mpg = 9000.1
#
# # Inline Printing
# #
# print("My car is the %s." % car_name)
#
# print("My car is the %s. It is a %s"  % (car_name, car_type))
#
# # Taking input
#
# name = input("What's your name?")
#
# print("Hello %s." % name)
#
# #print(name)
#
# age = input("How old are you? ")
#
# print("You are %s?" % age)

#
# def print_hw():
#     print("Hello World")
#
#
# print_hw()
#
#
# def say_hi(name):  # name is a "parameter"
#     print("Hello %s." % name)
#     print("I hope you have a fantastic day!")
#
#
# say_hi("Johnny")
#
#
# def birthday(age):
#     age += 1  # age = age + 1
#     print(age)
#
#
# say_hi("John")
# print("John is 15. Next Year:")
# birthday(15)
#
#
# def f(x):
#     return x ** 5 + 4 * x ** 4 - 17 * x ** 2 + 4
#
#
# print(f(3))
# print(f(3) + f(5))
#
# # If statements
#
#
# def grade_calc(percentage):
#     if percentage >= 90:
#         return "A"
#     elif percentage >= 80:  # Else if statement
#         return "B"
#     elif percentage >= 70:
#         return "C"
#     elif percentage >= 60:
#         return "D"
#     elif percentage <= 60:
#         return "F"
#
# # Loops
#
#
# print(range(5))
#
# for num in range(5):
#     print(num + 1)
#
# for letter in "Hello World":
#     print(letter)
#
# a = 1
# while a < 10:
#     print(a)
#     a += 1
#
# response = ""
# while response != "Hello":
#     response = input("Say\"Hello\"")
#
# print("Hello \nWorld")
#
#
# print(random.randint(0, 6))
#
#
# def reverse_order(first_name, last_name):
#     print("%s %s" % (last_name, first_name))
#
#
# def reverse_order():
#     first_name = input("What is your first name?")
#     last_name = input("What is your last name?")
#     print("%s %s" % (last_name, first_name))

# Comparisons
#
# print(1 == 1)  # Two equal signs to compare
#
# print(1 != 2)
# # One is not equal to 2
#
# print(not False)  # This prints True

#
# print(1 == 1 and 5 <= 4)
#
# print(1 < 0 or 5 > 1)
#
# # Recasting
#
# c = '1'
#
# print(c == 1)  # False - C is a string, 1 is an integer
#
# print(int(c) == 1)  # Compares two ints
#
# print(c == str(1))  # Compares two strings

# Lists
#
# the_count = [1, 2, 3, 4, 5]
# characters = ["Graves", "Dory", "Boots", "Dora", "Shrek", "Obi-wan", "Carl"]
# print(characters[4])
#
# print(len(characters))  # Gives you the length of the list
#
# # Going through lists
# for char in characters:
#     print(char)
#
# for num in the_count:
#     print(num ** 2)
#
# len(characters)
# range(3)  # Makes a list of the numbers from 0 to 2
# range(len(characters))  # Makes a list of ALL INDICES
#
# for num in range(len(characters)):
#     char = characters[num]
#     print("The character at index %d is %s" % (num, char))
#
# str1 = "Hello World!"
# listOne = list(str1)
# print(listOne)
# listOne[11] = '.'
# print(listOne)
# newStr = "".join(listOne)
# print(newStr)
#
# # Adding stuff to a list
# characters.append("Ironman/Batman/whomever you want")
# characters.append("Yo Mama")
# print(characters)
#
# # Removing things from a list
# characters.remove("Carl")
# print(characters)
#
# # Removing things from a list from the index
# characters.pop(6)
# print(characters)
#
# # The string class
# import string
# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.punctuation)
#
# strTwo = 'ThIs sEntENcE iS uNuSuAL'
# lowercase = strTwo.lower()
# print(lowercase)

# Dictionaries - Make up a key: value pair
# dictionary = {'name': 'Lance', 'age': 18, 'height': 6 * 12 + 2}
#
# # Accessing from a dictionary
# print(dictionary['name'])
# print(dictionary['age'])
# print(dictionary['height'])
#
# large_dictionary = {
#     "California": "CA",
#     "Michigan": "MI",
#     "Florida": "FL"
# }
# print(large_dictionary['Florida'])
#
# larger_dictionary = {
#     "California": [
#         'Fresno',
#         'Sacramento',
#         'Madera'
#     ],
#     "Washington": [
#         'Seattle',
#         'Tacoma',
#         'Olympia',
#         'Spokane'
#     ],
#     "Illinois": [
#         'Chicago',
#         'Naperville',
#         'Peoria'
#     ]
# }
# print(larger_dictionary['Illinois'])
# print(larger_dictionary['Illinois'][0])
# print(larger_dictionary['Washington'][3])  # Spokane

largest_dictionary = {
    "CA": {
        'NAME': "California",
        'POPULATION': 39250000,
        'BORDER ST': [
            'Oregon',
            'Nevada',
            'Arizona'
        ]
    },
    "MI": {
        'NAME': 'Michigan',
        'POPULATION': 9928000,
        'BORDER ST': [
            'Wisconsin',
            'Ohio',
            'Indiana'
        ]
    },
    "FL": {
        'NAME': 'Florida',
        'POPULATION': 20610000,
        'BORDER ST': [
            'Georgia',
            'Alabama'
        ]
    }
}
print(largest_dictionary["MI"]["BORDER ST"][1])
print(largest_dictionary['FL']['BORDER ST'][1])