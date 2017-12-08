
"""Warmup #2
# Write a function called "happy_bday"
# that "sings" (prints)
# the Happy Birthday Song
#
# It must take one parameter called "name" """
#
#
# def happy_bday(name):
#     print("Happy Birthday to you")
#     print("Happy Birthday to you")
#     print("Happy Birthday to " + name)
#     print("Happy Birthday to you!!!")

#
# """Write a function called add_py
# that takes one parameter called
# "name" and prints out name.py
# Example: add_py("I_ate_some") == "I_ate_some.py" """
#
#
# def add_y(name):
#     print("%s.py" % name)
#     print(name + ".py")


def add(num1, num2, num3, num4):  # Adding more than one parameter
    print(num1 + num2 + num3 + num4)


add(9, 90, 900, 9000)


def repeat(hello):
    print(hello)
    print(hello)
    print(hello)

    for x in range(3):
        print(hello)


def date(month, day, year):
    print(str(month) + "/" + str(day) + "/" + str(year))

date("12","8","17")
