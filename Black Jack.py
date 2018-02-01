import random

card = 0

print("Hi loser, my name is Natasha. What's yours...? -3-")
spades = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
hearts = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
clubs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diamonds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
kings = 10
queens = 10
jack = 10
hit_me = input("(Type in 'hit me' to be hit)")
stay = input("(Type in 'stay' to stop drawing cards)")
word = random.choice(spades, hearts, clubs, diamonds, kings, queens, jack)
if card > 21:
    print("You Bust! O3O")
    if card == 21:
        print("You win... I guess e-e")
