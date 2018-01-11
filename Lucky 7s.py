import random

die_num = random.randint(1, 6)
die_num2 = random.randint(1, 6)
m = 15
dice = die_num + die_num2

print("You have %s." % m)

while m > 0:
    answer = int(input("Type in roll to Roll the Dice."))
    if dice == 7:
        print("Good job!Now you have %s Money" % m)
        m += 5
    elif dice < 7:
        m -= 1
        print("I snatched your money now you have %s money" % m)
    elif dice > 7:
        m -= 1
        print("I snatched your money now you have %s money" % m)
    if m is 0:
        print("You have no moeny! GET OUT!")