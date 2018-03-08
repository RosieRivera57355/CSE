class Character(object):
    def __init__(self, name, description, inventory, interact, look, stats, health):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.interact = False
        self.look = False
        self.stats = stats
        self.health = health

        def interact(self):

