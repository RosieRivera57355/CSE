
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
    def __init__(self, name, use):
        super(Tools, self).__init__(name, use)

    def use(self):
        print('You used %s' % self.name)


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
    def __init__(self, cut):
        super(Knife, self).__init__('Knife', 'cut')
        self.cut = cut

    def cut(self):
        print('You cut the potatoes.')


class Key(Helper):
    def __init__(self):
        super(Key, self).__init__('Key', 'open')
