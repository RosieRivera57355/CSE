class Room(object):
    def __int__(self, name, north, south, west, east, northeast, northwest, southeast, southwest, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


F_GATE = Room('West of House', 'north_house')
west_house = Room('North of House', None)