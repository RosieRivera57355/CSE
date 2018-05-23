class Character(object):
    def __init__(self, name, description, capacity, interact, look, health, inventory):
        self.name = name
        self.description = description
        self.capacity = capacity
        self.interact = interact
        self.look = look
        self.health = health
        self.inventory = inventory

    def description(self):
        self.name = 'Billy'
        self.description = 'Billy works for the local news station. He is very athletic and will do anything to keep'
        'his job...ANYTHING.'


    def capacity(self):
        self.capacity = 10

billy = Character("Billy", "A generic middle aged man.", 10, None, None, 100, [])
