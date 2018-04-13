
# import statements
# class definitions
#     - items
#     - character
#     - rooms
# - instantiation
# - controller


class Item(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use


class House(Item, open):
    def __init__(self, name, use):
        super(House, self).__init__(name, 'open')
        self.open = open

    def open(self):
        print('You opened the %s' % self.name)


class Window(House):
    def __init__(self, open):
        super(Window, self).__init__('window', 'open')
        self.open = open

    def open(self):
        print('You opened the window.')


class Tools(Item):
    def __init__(self, name):
        super(Tools, self).__init__(name)


class Furniture(Item):
    def __init__(self, name, use):
        super(Furniture, self).__init__(name, use)


class Fridge(Furniture):
    def __init__(self):
        super(Fridge, self).__init__('Fridge', 'open')

    def open(self):
        print('There are some frozen chicken nuggets.')


class Kitchen(Item):
    def __init__(self, name, use):
        super(Kitchen, self).__init__(name, use)


class Misc(Item):
    def __init__(self, name, use):
        super(Misc, self).__init__(name, use)


class Helper(Item):
    def __init__(self, name, use):
        super(Helper, self).__init__(name, use)


class Knife(Helper):
    def __init__(self, pick_up):
        super(Knife, self).__init__('Knife', 'cut')
        self.pick_up = pick_up

    def pick_up(self):
        print('You picked up the knife')


class Key(Helper):
    def __init__(self, open):
        super(Key, self).__init__('Key', 'open')
        self.open = open

    def open(self):
        print('You opened the room.')


class Room(object):
    def __int__(self, name, north, south, west, east, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

F_GATE = Room('Front Gate', None, 'B_FENCE', None, None, None, 'The Front Gate is locked. Time to find another way.')
