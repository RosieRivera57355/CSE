#
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
#
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

def print_hw():
    print("Hello World")

print_hw()

def say_hi(name):  # name is a "parameter"
    print("Hello %s." % name)
    print("I hope you have a fantastic day!")


say_hi("Johnny")


def birthday(age):
  age += 1 # age = age + 1
  print(age)


say_hi("John")
print("John is 15. Next Year:")
birthday(15)

