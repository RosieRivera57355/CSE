import random
""""

Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the win condition

"""
guess = input("Guess a letter to reveal the word.")
letters_guessed = []
# if guess = letters_guessed:
#     letters_guessed.append

print(".")
word_bank = ["Click", "Marlin", "School", "Batman", "Stitch", "Jack Black", "Rick", "Luis", "50 Cent", "Felicia"]
list_form = []
guesses_left = 10
word = random.choice(word_bank)

# while guesses_left is 0:
    # if