class Room(object):
    def __int__(self, name, north, south, west, east, northeast, northwest, southeast, southwest):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.northeast = northeast
        self.northwest = northwest
        self.southeast = southeast
        self.southwest = southwest
        

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


north_house = Room('West of House', 'north_house')
west_house = Room('North of House', None)