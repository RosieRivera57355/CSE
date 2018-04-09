
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

    def drop(self):
        print('You dropped %s' % self.name)

    def pick_up(self):
        print('You picked up %s' % self.name)


class House(Item):
    def __init__(self, name, use):
        super(House, self).__init__(name, 'open')

    def open(self):
        print('You opened the %s' % self.name)


class Window(House):
    def __init__(self):
        super(Window, self).__init__('window', 'open', 'The window is partly open')

    def use(self):
        print('You opened the window.')


class Tools(Item):
    def __init__(self, name, use):
        super(Tools, self).__init__(name, use)

    def use(self):
        print('You used %s' % self.name)


class Knife(Tools):
    def __init__(self):
        super(Knife, self).__init__('Knife', 'cut')

    def name(self):
        print('knife')

    def cut(self):
        print('You cut the potatoes.')


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


class Tools(Item):
    def __init__(self, name, use, description):
        super(Tools, self).__init__(name, use, description)


class Key(Tools):
    def __init__(self):
        super(Key, self).__init__('Key', 'open')
