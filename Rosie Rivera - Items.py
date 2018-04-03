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


class Tools(Item):
    def __init__(self, name, use):
        super(Tools, self).__init__(name, 'use')

    def use(self):
        print('You used %s' % self.name)


class Furniture(Item):
    def __init__(self, name, use):
        super(Furniture, self).__init__(name, use)

    def move(self):
        print('You moved %s.' % self.name)

    def open(self):
        print('You opened %s' % self.name)


class Kitchen(Item):
    def __init__(self, name, use):
        super(Kitchen, self).__init__(name, use)


class Misc(Item):
    def __init__(self, name, use):
        super(Misc, self).__init__(name, use)