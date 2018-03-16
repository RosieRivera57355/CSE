class Character(object):
    def __init__(self, name, description, inventory, interact, look, stats, health, ):
        self.name = name
        self.description = description
        self.inventory = inventory
        self.interact = interact
        self.look = look
        self.stats = stats
        self.health = health

        def description(self):
            self.name = 'Billy'
            self.description = 'Billy works for the local news station. He is very athletic and will do \n' \
                               ' anything to keep his job.'
        def stats(self):
            self.health = 100



