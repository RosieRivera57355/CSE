uses = 5
food = 0
health = 100
capacity = 10


class Item(object):
    def __init__(self, name, use):
        self.name = name
        self.use = use


class House(Item):
    def __init__(self):
        super(House, self).__init__(name, use)

    def use(self):
        print('You opened the %s' % self.name)


class Window(House):
    def __init__(self):
        super(Window, self).__init__('window', 'open')

    def opens(self):
        print('You opened the window.')


class Furniture(Item):
    def __init__(self):
        super(Furniture, self).__init__(name, use)


class Cupboard(Furniture):
    def __init(self):
        super(Cupboard, self).__init__('Cupboards', 'opens')

    def opens(self):
        print('You have opened the cupboard and it seems that there is a shrine of Oprah Winfrey. The shrine consists'
              'of candles, rose petals, and her picture.')


class Fridge(Furniture):
    def __init__(self, name, use):
        super(Fridge, self).__init__('Fridge', 'opens')

    def opens(self):
        print('There are some frozen chicken nuggets.')


class Misc(Item):
    def __init__(self):
        super(Misc, self).__init__(name, use)


class Box(Misc):
    def __init__(self):
        super(Box, self).__init__('Box', 'open')

    def open(self):
        print('You have opened the box. There seems to be something inside...')

    def look(self):
        print('In the box, there is')


class Helper(Item):
    def __init__(self):
        super(Helper, self).__init__(name, use)


class CoffeeGrounds(Helper):
    def __init__(self):
        super(CoffeeGrounds, self).__init__('Coffee Grounds', 'fill')

    def fill(self):
        print('You poured the coffee grounds into the coffee machine.')


class Knife(Helper):
    def __init__(self):
        super(Knife, self).__init__('Knife', 'cut')

    def pickup(self):
        print('You picked up the knife')


class Bp(Helper):
    def __init__(self):
        super(Helper, self).__init__('Backpack', 'store')

    def equip(self):
        print('You have equipped the backpack.')


class Key(Helper):
    def __init__(self):
        super(Key, self).__init__('Key', 'open')

    def open(self):
        print('You opened the room.')


class PlushDog(Helper):
    def __init__(self):
        super(PlushDog, self).__init__('Plush Dog', 'heal')

    def feed(self):
        print('The doggy loves you and will stick by your side forever.')

    def pet(self):
        print('The doggy is happy! You have gained 15 health. You now have %s uses.' % uses)


class Bone(Helper):
    def __init__(self):
        super(Bone, self).__init__('Bone', 'feed')

    def feed(self):
        print('You fed to the dog.')

    def pickup(self):
        print('You picked up the bone')

    def drop(self):
        print('You dropped the bone.')


class Mug(Helper):
    def __init__(self):
        super(Mug, self).__init__('Mug', 'fill')

    def fill(self):
        print('You filled up the mug with coffee.')

    def pickup(self):
        print('You picked up the mug.')


class Phone(Helper):
    def __init__(self):
        super(Phone, self).__init__('Phone', 'use')

    def pickup(self):
        print('You have picked up the coffee machine.')

    def turn_on(self):
        print('The phone has turned on.')


class Sink(Furniture):
    def __init__(self):
        super(Sink, self).__init__('Sink', 'run')

    def run(self):
        print('The sink is now running.')

    def turn_off(self):
        print('The sink is not running.')


class CoffeeMachine(Helper):
    def __init__(self):
        super(CoffeeMachine, self).__init__('Coffee Machine', 'dispense')

    def turn_on(self):
        print('You turned on the coffee machine.')

    def fill(self):
        print('You have filled the coffee machine up with coffee grounds.')