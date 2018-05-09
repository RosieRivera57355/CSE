import random

# import statements
# class definitions
#     - items
#     - character
#     - rooms
# - instantiation
# - controller

uses = 5
food = 0
health = 100
capacity = 10
random = random.randint(1, 6)


class Item(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use


class House(Item):
    def __init__(self, name, use):
        super(House, self).__init__(name, use)


    def use(self):
        print('You opened the %s' % self.name)


class Window(House):
    def __init__(self):
        super(Window, self).__init__('window', 'open')

    def open(self):
        print('You opened the window.')


class Furniture(Item):
    def __init__(self, name, use):
        super(Furniture, self).__init__(name, use)


class Cupboard(Furniture):
    def __init(self):
        super(Cupboard, self).__init__('Cupboards','open')

    def open(self):
        print('You have opened the cupboard and it seems that there is a shrine. The shrine consists'
              'of candles, rose petals, and... There seems to be something missing...')


class Fridge(Furniture):
    def __init__(self):
        super(Fridge, self).__init__('Fridge', 'opens')

    def open(self):
        print('There are some frozen chicken nuggets.')


class Misc(Item):
    def __init__(self, name, use):
        super(Misc, self).__init__(name, use)


class Box(Misc):
    def __init__(self):
        super(Box, self).__init__('Box', 'open')

    def open(self):
        print('You have opened the box. There seems to be something inside...')

    def look(self):
        print('In the box, there is')


class Flowerbed(Misc):
    def __init__(self):
        super(Flowerbed, self).__init__('Flowerbed', 'search')

    def search(self):
        print('There is a key in the bush!')


class Helper(Item):
    def __init__(self, name, use):
        super(Helper, self).__init__(name, use)


class CoffeeGrounds(Helper):
    def __init__(self):
        super(CoffeeGrounds, self).__init__('Coffee Grounds', 'fill')

    def fill(self):
        print('You poured the coffee grounds into the coffee machine.')


class Knife(Helper):
    def __init__(self):
        super(Knife, self).__init__('Knife', 'cut')

    def pickup(self):
        print('You picked up the knife')


class Bp(Helper):
    def __init__(self):
        super(Helper, self).__init__('Backpack', 'store')

    def equip(self):
        print('You have equipped the backpack.')


class Key(Helper):
    def __init__(self):
        super(Key, self).__init__('Key', 'open')

    def open(self):
        print('You opened the room.')


class PlushDog(Helper):
    def __init__(self):
        super(PlushDog, self).__init__('Plush Dog', 'heal')

    def feed(self):
        print('The doggy loves you and will stick by your side forever.')

    def pet(self):
        print('The doggy is happy! You have gained 15 health. You now have %s uses.')


class Bone(Helper):
    def __init__(self):
        super(Bone, self).__init__('Bone', 'feed')

    def give(self):
        print('You fed to the dog.')

    def pickup(self):
        print('You picked up the bone')

    def drop(self):
        print('You dropped the bone.')


class Mug(Helper):
    def __init__(self):
        super(Mug, self).__init__('Mug', 'fill')

    def fill(self):
            print('You filled up the mug with coffee.')

    def pickup(self):
            print('You picked up the mug.')


class Phone(Helper):
    def __init__(self):
        super(Phone, self).__init__('Phone', 'use')

    def pickup(self):
        print('You have picked up the coffee machine.')

    def turn_on(self):
        print('The phone has turned on.')


class Sink(Furniture):
    def __init__(self):
        super(Sink, self).__init__('Sink', 'run')

    def run(self):
        print('The sink is now running.')

    def turnoff(self):
        print('The sink is not running.')


class CoffeeMachine(Helper):
    def __init__(self):
        super(CoffeeMachine, self).__init__('Coffee Machine', 'dispense')

    def turnon(self):
        print('You turned on the coffee machine.')

    def fill(self):
        print('You have filled the coffee machine up with coffee grounds.')


class Room(object):
    def __init__(self, name, north, south, west, east, northwest, northeast, southwest, southeast, up, down,
                 description, item=None, item2=None, item3=None):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.northwest = northwest
        self.northeast = northeast
        self.southwest = southwest
        self.southeast = southeast
        self.up = up
        self.down = down
        self.description = description
        self.item = item
        self.item2 = item2
        self.item3 = item3

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


directions = ['north', 'south', 'west', 'east', 'northwest', 'northeast', 'southwest', 'southeast', 'up', 'down']
short_direction = ['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'u', 'd']

f_gate = Room('Front Gate', None, 'b_fence', None, None, None, None, None, None, None, None,
              'The Gate is locked. You must look for another way.', None)
b_fence = Room('Broken Fence', 'f_gate', None, None, None, None, None, None, None, None, None,
               'The fence is loose.', 'Fence', None, None)
garden = Room('Garden', 's_house', None, None, None, None, 'shed', None, None, 'b_fence',
              None, 'There is a path leading Northeast somewhere and there is a broken fence south of here.')
s_house = Room('South of House', 'l_room', 'garden', 'w_house', 'e_house', None, None, None, None,
               None, None, 'There is a window that is partly open. There seems to be something shining inside')
l_room = Room('Living Room', None, 's_house', None, None, None, None, None, None, 'u_stairs',
              'd_stairs', 'There seems to be an upstairs and downstairs and not much else...You should look around.')
k_room = Room('Kitchen', None, None, 'l_room', None, None, None, None, None, None, None,
              'There is a fridge, an island, and cupboards.'
              '\n There is a knife on a cutting board, a sink, a coffee machine, coffee grounds, and a mug')
up_stairs = Room('Up Stairs', None, None, 'jt_room', 'g_room', None, None, None, None,
                 None, 'l_room', 'There is a room WEST \n'
                                 'of here and a room EAST of here. There is a mirror and a vase that has some flowers')
jt_room = Room('Justin Timberlakes Room', None, None, None, 'u_stairs', None, None, None, None, None, None,
               'There is a phone on the bedside table. There is also a TV, bed, and a drawer.')
parking_lot = Room('Parking Lot', 'garage', 'l_room', None, None, None, None, None, None, None, None,
                   'There is a garage that is open. Inside, there is are 3 boxes with stuff inside.')
d_house = Room('Dog House', 'd_room', 'y_back', None, None, None, None, None, None, None, None,
               'There is a big dog house and from outside you can hear a big dog barking. Will you go inside?')
d_room = Room('Dog Room', None, 'd_house', None, None, None, None, None, None, None, None,
              'There is a small dog in here and it seems to want something. You cannot get '
              'close enough to it to see what is on its collar.')
y_back = Room('Back Yard', None, 'shed', 'k_room', None, None, None, None, None, None, None,
              'There is a shed south of here. There could be something useful in there.')
shed = Room('Shed', 'y_back', 'garden', None, None, None, None, None, None, None, None,
            'There are two paths one goes Southwest and one goes north. Inside there is a picture.')
d_stairs = Room('Down Stairs', None, None, None, None, None, None, None, None, 'l_room', None,
                'It is dark and there is a room with a whole bunch of junk.')
g_room = Room('Guest Room', 'w_house', None, None, None, None, 'l_room', None, 's_house', None, None, 'There is')
current_node = f_gate

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Found")
