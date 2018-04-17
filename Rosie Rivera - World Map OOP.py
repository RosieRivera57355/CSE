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


direction = ('NORTH', 'SOUTH', 'WEST', 'EAST', 'NORTHWEST', 'NORTHEAST', 'SOUTHWEST', 'SOUTHEAST', 'UP', 'DOWN')
short_direction = ('N', 'S', 'W', 'E', 'NW', 'NE', 'SW', 'SE', 'U', 'D')

while True:
    print(current_node.name)
    print(current_node.descrition)
    command = input('>_').upper().strip()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = direction[pos]
    if command in direction:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Found")


current_node = f_gate
f_gate = Room('Front Gate', None, 'Fence', None, None, None, None, None, None, None, None, 'The Gate is locked.'
                                                                                         'You must look for another.')
b_fence = Room('Broken Fence', 'Front Gate', None, None, 'Sewer Lid', None, None, None, None, None, None, 'The fence '
                                                                                                          'is loose.')
garden = Room('South of House', None, None, None, None, 'Shed', None, None, 'Back Fence', None, None, 'There is a path'
                                            'leading Northeast somewhere and there is a broken fence south of here.')
s_house = Room('Living Room', 'Garden', 'West of House', 'East of House', None, None, None, None, None, None, 'There is'
                                            'a window that is partly open. There seems to be something shining inside')



