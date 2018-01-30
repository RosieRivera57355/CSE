import random
import string
""""

Outline of Hangman
1. Make a word bank - 10 items
2. Select a random item from the list
3. Add user input to a list of letters_guessed
4. Build a list of letters to show, and display the string form
5. Create the win condition

"""
letters_guessed = []
word_bank = ["Click", "Marlin", "School", "Batman", "Stitch", "Jack Black", "Rick", "Luis", "50Cent", "Felicia"]
guesses_left = 10
word = random.choice(word_bank)
letter = string.ascii_letters
end = list(word)
while guesses_left > 0:
    list_form = []
    for letter in word:
        if letter.lower() in letters_guessed:
            list_form.append(letter)  # show letter
        else:
            list_form.append("*")  # hide letter
        if list_form == end:
            print("You're a winner!")
            exit(0)
    print(list_form)
    guess = input("Guess a letter/Number to reveal the word.").lower()
    letters_guessed.append(guess)

    if guess in word:
        print("You got it!")

    else:
        guesses_left -= 1
        print("Sorry that's not it")
