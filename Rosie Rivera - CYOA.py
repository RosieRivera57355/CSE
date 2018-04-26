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
    def __init__(self, name, use):
        super(Window, self).__init__('window', 'open')

    def opens(self):
        print('You opened the window.')


class Furniture(Item):
    def __init__(self, name, use):
        super(Furniture, self).__init__(name, use)


class Cupboard(Furniture):
    def __init(self, name, use):
        super(Cupboard, self).__init__('Cupboards','open')


class Fridge(Furniture):
    def __init__(self, name, use):
        super(Fridge, self).__init__('Fridge', 'opens')

    def opens(self):
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


class Helper(Item):
    def __init__(self, name, use):
        super(Helper, self).__init__(name, use)


class Knife(Helper):
    def __init__(self, name, use):
        super(Knife, self).__init__('Knife', 'cut')

    def pickup(self):
        print('You picked up the knife')
        capacity -= 2


class Bp(Helper):
    def __init__(self, name, use):
        super(Helper, self).__init__('Backpack', 'store')

    def equip(self):
        print('You have equipped the backpack.')
        capacity += 15


class Key(Helper):
    def __init__(self, name, use):
        super(Key, self).__init__('Key', 'open')

    def open(self):
        print('You opened the room.')


class PlushDog(Helper):
    def __init__(self, name, use):
        super(PlushDog, self).__init__('Plush Dog', 'heal')

    def feed(self):
        bone -= 1

    def pet(self):
        print('The doggy is happy! You have gained 15 health. You now have %s uses.' % uses)
        uses -= 1
        health =+ 15


class Bone(Helper):
    def __init__(self, name, use):
        super(Bone, self).__init__('Bone', 'feed')

    def give(self):
        print('You fed to the dog.')
        capacity += 2

    def pickup(self):
        print('You picked up the bone')
        capacity -= 2

    def drop(self):
        print('You dropped the bone.')
        capacity += 2


class Mug(Helper):
    def __init__(self, name, use):
        super(Mug, self).__init__('Mug', 'fill')

    def fill(self):
            print('You filled up the mug with coffee.')
            capacity -= 1

    def pickup(self):
            print('You picked up the mug.')


class Phone(Helper):
    def __init__(self, name, use):
        super(Phone, self).__init__('Phone', 'use')

    def pickup(self):
        print('You have picked up the coffee machine.')

    def turn_on(self):
        print('The phone has turned on.')


class Sink(self):
    def __init__(self):
        super(Sink, self).__init__('Sink', 'run')
    def run(self):
        print('The sink is now running.')

    def turnoff(self):
        print('The sink is not running.')

while inventory



class Room(object):
    def __init__(self, name, north, south, west, east, northwest, northeast, southwest, southeast, up, down,
                 description):
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

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


directions = ('NORTH', 'SOUTH', 'WEST', 'EAST', 'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST', 'UP', 'DOWN')
short_direction = ('N', 'S', 'W', 'E', 'NW', 'NE', 'SW', 'SE', 'U', 'D')
f_gate = Room('Front Gate', None, 'Fence', None, None, None, None, None, None, None, None,
              'The Gate is locked. You must look for another.')
b_fence = Room('Broken Fence', 'Front Gate', None, None, 'Sewer Lid', None, None, None, None, None, None, 'The fence '
                                                                                                          'is loose.')
garden = Room('Garden', 'South of House', None, None, None, None, 'Shed', None, None, 'Back Fence',
              None, 'There is a path leading Northeast somewhere and there is a broken fence south of here.')
s_house = Room('South of House', 'Living Room', 'Garden', 'West of House', 'East of House', None, None, None, None,
               None, None, 'There is a window that is partly open. There seems to be something shining inside')
l_room = Room('Living Room', None, 'South of House', None, None, None, None, None, None, 'Up Stairs',
              'Down Stairs', 'There seems to be an upstairs and downstairs and not much else...You should look around.')
k_room = Room('Kitchen', None, None, 'Living Room', None, None, None, None, None, None, None,
              'There is a fridge, an island, and cupboards.'
              '\n There is a knife on a cutting board, a sink, a coffee machine, coffee grounds, and a mug')
up_stairs = Room('Up Stairs', None, None, 'Justin Timberlakes Room', 'Guest Room', None, None, None, None,
                 None, 'Living Room', 'There is a room WEST of here and a room EAST of here.'
                                      'There is a mirror and a vase that has some flowers')
jt_room = Room('Justin Timberlakes', None, None, None, 'Up Stairs', None, None, None, None, None, None,
               'There is a phone on the bedside table. There is also a TV, bed, and a drawer.')
parking_lot = Room('Parking Lot', 'Garage', 'Living Room', None, None, None, None, None, None, None, None,
                   'There is a garage that is open. Inside, there is are 3 boxes with stuff inside.')
d_house = Room('Dog House', 'Dogs Room', 'Back Yard', None, None, None, None, None, None, None, None,
               'There is a big dog house and from outside you can hear a big dog barking. Will you go inside?')
d_room = Room('Dog Room', None, 'Dog House', None, None, None, None, None, None, None, None,
              'There is a small dog in here and it seems to want something. You cannot get '
              'close enough to it to see what is on its collar.')
y_back = Room('Back Yard', None, 'Shed', 'Kitchen', None, None, None, None, None, None, None,
              'There is a shed south of here. There could be something useful in there.')
shed = Room('Shed', 'Back Yard', 'Garden', None, None, None, None, None, None, None, None,
            'There are two paths one goes Southwest and one goes north. Inside there is a picture.')
d_stairs = Room('Down Stairs', None, None, None, None, None, None, None, None, 'Living Room', None,
                'It is dark and there is a room with a whole bunch of junk.')
current_node = f_gate

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').upper().strip()
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
