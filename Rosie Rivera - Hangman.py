import random
""""

Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the win condition

"""
list_form = []
guesses_left = 10
letters_guessed = [""]
word_bank = ["Click", "Robot", "School", "Batman", "Stitch", "Jack Black", "Shrek", "Luis", "50 Cent", "Beyonce"]
word = random.choice(word_bank)
word_bank[word] = '*'
