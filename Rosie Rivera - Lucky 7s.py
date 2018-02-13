import random

r = 0
m = 15

print("You have %s Dollars." % m)

while m > 0:
    die_num = random.randint(1, 6)
    die_num2 = random.randint(1, 6)
    dice = die_num + die_num2
    if dice == 7:
        m += 4
        print("Good job!Now you have %s Money" % m)
        r += 1
        print("Round %s" % r)
    elif dice < 7:
        m -= 1
        r += 1
        print("I snatched your money now you have %s money" % m)
        print("Round %s" % r)
    elif dice > 7:
        m -= 1
        r += 1
        print("I snatched your money now you have %s money" % m)
        print("Round %s" % r)
    if m is 0:
        print("You have no money! GET OUT!")
        print("You lost your money in %s rounds" % r)
