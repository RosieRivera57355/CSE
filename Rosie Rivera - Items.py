class Item(object):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def drop(self):
        print('You dropped %s' % self.name)

    def pick_up(self):
        print('You picked up %s' % self.name)

    def open(self):
        print('You opened the %s' % self.name)


class house_parts(Item):
    def __init__(self, window, fence):
        self.window = window
        self.fence = fence