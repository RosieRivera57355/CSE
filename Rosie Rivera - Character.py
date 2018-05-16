class Character(object):
    def __init__(self, name, description, capacity, interact, look, stats, health, enemy):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.interact = interact
        self.look = look
        self.stats = stats
        self.health = health
        self.enemy = enemy

    def description(self):
        self.name = 'Billy'
        self.description = 'Billy works for the local news station. He is very athletic and will do anything to keep'
        'his job...ANYTHING.'

    def stats(self):
        self.health = 100
        self.capacity = 10

    def capacity(self):
        self.capacity = 10

