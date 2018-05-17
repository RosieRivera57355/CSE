import random
import webbrowser

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
    def __init__(self, name, action, use):
        self.name = name
        self.use = use
        self.action = action


class House(Item):
    def __init__(self, name, action, use):
        super(House, self).__init__(name, action, use)


    def use(self):
        print('You opened the %s' % self.name)


class Window(House):
    def __init__(self, name, action, use):
        super(Window, self).__init__(name, action, use)

    def open(self):
        print('You opened the window.')


class Fence(House):
    def __init__(self, name, action, use):
        super(Fence, self).__init__(name, action, use)

    def open(self):
        print('You opened the fence.')


class Furniture(Item):
    def __init__(self, name, action, use):
        super(Furniture, self).__init__(name, action, use)


class Cupboard(Furniture):
    def __init(self, name, action, use):
        super(Cupboard, self).__init__(name, action, use)

    def open(self):
        print('You have opened the cupboard and it seems that there is a shrine. The shrine consists'
              'of candles, rose petals, and... There seems to be something missing...')


class Fridge(Furniture):
    def __init__(self, name, action, use):
        super(Fridge, self).__init__(name, action, use)

    def open(self):
        print('There are some frozen chicken nuggets.')


class Misc(Item):
    def __init__(self, name, action, use):
        super(Misc, self).__init__(name, action, use)


class Box(Misc):
    def __init__(self, name, action, use):
        super(Box, self).__init__(name, action, use)

    def open(self):
        print('You have opened the box. There seems to be something inside...')

    def look(self):
        print('In the box, there is')


class Flowerbed(Misc):
    def __init__(self, name, action, use):
        super(Flowerbed, self).__init__(name, action, use)

    def search(self):
        print('There is a key in the bush!')


class Helper(Item):
    def __init__(self, name, action, use):
        super(Helper, self).__init__(name, action, use)


class CoffeeGrounds(Helper):
    def __init__(self, name, action, use):
        super(CoffeeGrounds, self).__init__(name, action, use)

    def fill(self):
        print('You poured the coffee grounds into the coffee machine.')


class Knife(Helper):
    def __init__(self, name, action, use):
        super(Knife, self).__init__(name, action, use)

    def pickup(self):
        print('You picked up the knife')


class Bp(Helper):
    def __init__(self, name, action, use):
        super(Helper, self).__init__(name, action, use)

    def equip(self):
        print('You have equipped the backpack.')


class Key(Helper):
    def __init__(self, name, action, use):
        super(Key, self).__init__(name, action, use)

    def open(self):
        print('You opened the room.')


class PlushDog(Helper):
    def __init__(self, name, action, use):
        super(PlushDog, self).__init__(name, action, use)

    def feed(self):
        print('The doggy loves you and will stick by your side forever.')

    def pet(self):
        print('The doggy is happy! You have gained 15 health. You now have %s uses.')


class Bone(Helper):
    def __init__(self, name, action, use):
        super(Bone, self).__init__(name, action, use)

    def give(self):
        print('You fed to the dog.')

    def pickup(self):
        print('You picked up the bone')

    def drop(self):
        print('You dropped the bone.')


class Mug(Helper):
    def __init__(self, name, action, use):
        super(Mug, self).__init__(name, action, use)

    def fill(self):
            print('You filled up the mug with coffee.')

    def pickup(self):
            print('You picked up the mug.')


class Phone(Helper):
    def __init__(self, name, action, use):
        super(Phone, self).__init__(name, action, use)

    def pickup(self):
        print('You have picked up the coffee machine.')

    def turn_on(self):
        print('The phone has turned on.')


class Sink(Furniture):
    def __init__(self, name, action, use):
        super(Sink, self).__init__(name, action, use)

    def run(self):
        print('The sink is now running.')

    def turnoff(self):
        print('The sink is not running.')


class CoffeeMachine(Helper):
    def __init__(self, name, action, use):
        super(CoffeeMachine, self).__init__(name, action, use)

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


window = Window('Window', None, 'open')
fence = Fence('Fence', None, 'open')
cupboard = Cupboard('Cupboard', None, 'open')
fridge = Fridge('Fridge', None, 'open')
box = Box('Box', None, 'open')
flowerbed = Flowerbed('Flowerbed', None, 'search')
coffeegrounds = CoffeeGrounds('Coffee grounds', 'pickup', 'pour grounds')
knife = Knife('Knife', 'pickup', 'equip backpack')
mug = Mug('Mug', 'grab mug', 'fill')
sink = Sink('Sink', None, 'turn on')


directions = ['north', 'south', 'west', 'east', 'northwest', 'northeast', 'southwest', 'southeast', 'up', 'down']
short_direction = ['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'u', 'd']

f_gate = Room('Front Gate', None, None, None, 'b_fence', None, None, None, None, None, None,
              'The Gate is locked. You must look for another way.', None, None, None)
b_fence = Room('Broken Fence', None, None, 'f_gate', None, None, None, None, None, None, None,
               'The fence is loose. Maybe you can break in.', 'Fence', None, None)
garden = Room('Garden', 's_house', 'b_fence', None, None, None, 'shed', None, None, None,
              None, 'There is a path leading Northeast somewhere and there is a broken fence south of here.',
              'Flowerbed', None, None)
s_house = Room('South of House', 'l_room', 'garden', 'w_house', 'e_house', None, None, None, None,
               None, None, 'There is a window that is partly open. There seems to be something shining inside')
l_room = Room('Living Room', None, 's_house', None, 'k_room', None, None, None, None, 'u_stairs',
              'd_stairs', 'It seems to be a regular lving room, and there is a mug that is just sitting there.'
                          'There is a staircase that leads upstairs and downstairs.', 'mug', None, None)
k_room = Room('Kitchen', None, None, 'l_room', None, None, None, None, None, None, None,
              'There is a fridge, an island, and cupboards.There is a knife on a cutting board, a sink,'
              'a coffee machine, coffee grounds, and a mug', 'coffee machine', 'coffee grounds', 'sink')
up_stairs = Room('Up Stairs', None, None, 'jt_room', 'g_room', None, None, None, None,
                 None, 'l_room', 'There is a room WEST \n of here and a room EAST of here. There is a mirror and a vase'
                                 'that has some flowers')
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
g_room = Room('Guest Room', 'w_house', None, None, None, None, 'l_room', None, 's_house', None, None,
              'There is a trophy in the trash can', 'trophy', )
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
    elif command == 'test this':
        webbrowser.open_new("https://www.youtube.com/watch?v=ru0K8uYEZWw")
    elif command == 'break fence' and current_node == b_fence:
        b_fence.north = 'garden'
        print("SMASH!!!!!")
    else:
        print("Command not Found")
