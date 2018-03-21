class Item(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use

    def drop(self):
        print('You dropped %s' % self.name)

    def pick_up(self):
        print('You picked up %s' % self.name)


class house(Item):
    def __init__(self, name, use):
        super(house, self).__init__(name, 'open')

    def open(self):
        print('You opened the %s' % self.name)


class tools(Item):
    def __init__(self, name, use):
        super(tools, self).__init__(name, 'use')

    def use(self):
        print('You used %s' % self.name)


class furniture(Item):
    def __init__(self, name, use):
        super(furniture, self).__init__(name, use)

    def


class kitchen(Item):
    def __init__(self, name, use).__init__(name, use)


class misc(Item):
    def __init__(self).__init__(name, use)