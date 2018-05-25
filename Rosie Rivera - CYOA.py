import random
import webbrowser

# import statements
# class definitions
#     - items
#     - character
#     - rooms
# - instantiation
# - controller
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
        print('There .')


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

    def pickup_knife(self):
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

    def feed_bone(self):
        print('The doggy is happy and will now let you pick it up.')


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


class Club(Helper):
    def __init__(self, name, action, use):
        super(Club, self).__init__(name, action, use)

    def attack(self):
        print('You have gotten beat to death.')

class Phone(Helper):
    def __init__(self, name, action, use):
        super(Phone, self).__init__(name, action, use)

    def pickup(self):
        print('You have picked up the coffee machine.')

    def turn_on(self):
        print('The phone has turned on.')


class Qtip(Helper):
    def __init__(self, name, action, use):
        super(Qtip, self).__init__(name, action, use)

    def pickup(self):
        print('You picked up a used Q-Tip.')


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


club = Club('Club', None, None)
cupboard = Cupboard('Cupboard', None, 'open')
fridge = Fridge('Fridge', None, 'open')
box = Box('Box', None, 'open')
flowerbed = Flowerbed('Flowerbed', None, 'search')
knife = Knife('Knife', 'pickup', 'threaten')
bp = Bp('Backpack', 'pickup', 'equip backpack')
key = Key('Key', 'pickup', 'use')
plushdog = PlushDog('Plush Dog', None, None)
bone = Bone('Bone', 'pickup', 'give')
phone = Phone('Phone', 'pickup', 'take a picture')
qtip = Qtip('Q-Tip', 'pick_up', None)


class Character(object):
    def __init__(self, name, description, capacity, location, inventory, pickup):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.location = location
        self.inventory = inventory
        self.pickup = pickup

    def description(self):
        self.name = 'Joe'
        self.description = 'Joe works for the local news station. He is very athletic and will do anything to keep'
        'his job...ANYTHING.'

    def capacity(self):
        self.capacity = 10


guard = Character('Guard', 'He is a mean man that will not let you pass from the front gate.', None,
                  'f_gate', [Club], None)
joe = Character("Joe", "A generic middle aged man.", 10, None, [], None)

directions = ['north', 'south', 'west', 'east', 'northwest', 'northeast', 'southwest', 'southeast', 'up', 'down']
short_direction = ['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'u', 'd']

f_gate = Room('Front Gate', None, None, None, 'b_fence', None, None, None, None, None, None,
              'The Gate is locked and guarded by a mean looking guard. You could look for another way '
              'or attack the guard.', None, None, None)
b_fence = Room('Loose Fence', None, None, 'f_gate', None, None, None, None, None, None, None,
               'The fence is loose. Maybe you can break in.', None, None, None)
garden = Room('Garden', 's_house', 'b_fence', None, None, None, 'shed', None, None, None,
              None, 'There is a path leading Northeast somewhere and there is a broken fence south of here. '
                    'There seems to be a house North of here',
              None, None, None)
t_room = Room('Bathroom', None, 'up_stairs', None, None, None, None, None, None, None, None,
              'This is a really nice bathroom, but there are used Q-tips here...')
s_house = Room('South of House', None, 'garden', 'w_house', 'e_house', None, None, None, None,
               None, None, 'There is a window that is partly open. There seems to be something shining inside', 'qtip')
l_room = Room('Living Room', None, 's_house', None, 'k_room', None, None, None, None, 'up_stairs',
              'd_stairs', 'It seems to be a regular lving room, and there is a mug that is just sitting there.'
                          'There is a staircase that leads upstairs and downstairs.', 'mug', None, None)
k_room = Room('Kitchen', None, None, 'l_room', None, None, None, None, None, None, None,
              'There is a fridge, an island, and cupboards.There is a knife on a cutting board, a sink,'
              'a coffee machine, coffee grounds, and a mug', 'coffee machine', 'coffee grounds', 'sink')
up_stairs = Room('Up Stairs', 't_room', None, None, 'g_room', None, None, None, None,
                 None, 'l_room', 'There is a room WEST \n of here and a room EAST of here. There is a mirror and a vase'
                                 ' that has some flowers')
theater = Room('Theater', None, None, 'd_stairs', None, None, None, None, None, None, None,
               'In the theater you see the new Justin Timberlake movie playing')
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
shed = Room('Shed', 'y_back', None, None, None, None, 'garden', None, None, None, None,
            'There are two paths one goes Southwest and one goes north. Inside there is a picture.')
d_stairs = Room('Bowling Alley', None, None, None, None, None, None, None, None, 'l_room', None,
                'There is a Bowling Alley down here and there is.')
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
    elif command == 'unlock room' and current_node == up_stairs:
        if Key in joe.inventory:
            print("You opened the door.")
            up_stairs.west = 'jt_room'
        else:
            print("You do not have the key.")
#  Help
    elif command == '?':
        print('To move you just type in:\n'
              'the direction you want to go in.\n'
              'for example: typing in n or north will take you north \n'
              ''
              'type this to go to next page: page 2')
    elif command == 'page 2':
        print('To pick up items type in:'
              'pick up [name of item]')
#
    elif command == 'open window' and current_node == s_house:
        s_house.north = 'l_room'
        print('WOOOOOOSH!')
    elif command == 'break fence' and current_node == b_fence:
        b_fence.north = 'garden'
        print("SMASH!!!!!")
    elif 'pickup' in command:
        pick_up = command[5:]
#  Attack
    elif command == 'attack security guard' and current_node == f_gate:
        print('You tried to attack the guard but he grabs you and starts beating you. \n'
              'YOU HAVE BEEN BEATEN TO DEATH')
        quit(0)
#  Pickup
        found = False
        for item in joe.location.items:
            if pickup_name == item.name.lower():
                if joe.pickup(item):
                    found = item
        if found is False:
            print('Invalid Item')
    else:
        print("Command not Found")
