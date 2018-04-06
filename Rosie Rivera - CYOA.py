
# import statements
# class definitions
#     - items
#     - character
#     - rooms
# - instantiation
# - controller


class Item(object):
    def __init__(self, name, use, description):
        self.name = name
        self.use = use
        self.description = description


class House(Item):
    def __init__(self, name, use, description):
        super(House, self).__init__(name, use, description)


class Window(House):
    def __init__(self, open):
        super(Window, self).__init__('window', 'open', 'The window is partly open')

    def open(self):
        print('You opened the window.')


class Fence(House):
    def __init__(self, name, use, description):
        super(House, self).__init__(name ,use , description)

    def description(self):
        print('There is a loose board.')

    def name(self):
        print('Fence')

    def use(self):
        print('You opened the %s' % self.name)


class Tools(Item):
    def __init__(self, name, use, description):
        super(Tools, self).__init__(name, use, description)


class Knife(Tools):
    def __init__(self, name, use, description):
        super(Knife, self).__init__('Knife', 'cut', 'The knife looks like it can cut through many things.')

    def name(self):
        print('knife')

    def use(self):
        print('')

class Key(Tools):
    def __init__(self, name, use, description):
        super(Key, self).__init__('Key', 'open', 'You can open something with this key.')


class Furniture(Item):
    def __init__(self, name, use, description):
        super(Furniture, self).__init__(name, use, description)


class Fridge(Furniture):
    def __init__(self, name, use, description):
        super(Fridge, self).__init__('Fridge', 'open', 'There are vegetables in here.')


class Kitchen(Item):
    def __init__(self, name, use, description):
        super(Kitchen, self).__init__(name, use, description)


class Misc(Item):
    def __init__(self, name, use, description):
        super(Misc, self).__init__(name, use, description)
