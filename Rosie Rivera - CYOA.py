
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
    def __init__(self, name, use):
        super(House, self).__init__(name, use, description)


class Tools(Item):
    def __init__(self, name, use):
        super(Tools, self).__init__(name, use, description)


class Furniture(Item):
    def __init__(self, name, use):
        super(Furniture, self).__init__(name, use, description)


class Kitchen(Item):
    def __init__(self, name, use):
        super(Kitchen, self).__init__(name, use, description)


class Misc(Item):
    def __init__(self, name, use):
        super(Misc, self).__init__(name, use, description)
