class Room(object):
    def __int__(self, name, north, south, west, east, northwest, northeast, southwest, southeast, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.west = west
        self.east = east
        self.northwest = northwest
        self.northeast = northeast
        self.southwest = southwest
        self.southeast = southeast
        self.up = up
        self.down = down
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


f_gate = Room('Front Gate', None, 'Fence', None, None, None, None, None, None, None, None, 'The fence is loose.')
b_fence = Room('Broken Fence', 'Front Gate', None, None, 'Sewer Lid')