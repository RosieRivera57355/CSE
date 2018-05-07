class Room(object):
    def __init__(self, name, north, south, west, east, northwest, northeast, southwest, southeast, up, down,
                 description):
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


directions = ['north', 'south', 'west', 'east', 'northwest', 'northeast', 'southwest', 'southeast', 'up', 'down']
short_direction = ['n', 's', 'w', 'e', 'nw', 'ne', 'sw', 'se', 'u', 'd']

f_gate = Room('Front Gate', None, 'Fence', None, None, None, None, None, None, None, None,
              'The Gate is locked. You must look for another way.')
b_fence = Room('Broken Fence', 'Front Gate', None, None, 'Sewer Lid', None, None, None, None, None, None, 'The fence '
                                                                                                          'is loose.')
garden = Room('Garden', 'South of House', None, None, None, None, 'Shed', None, None, 'Back Fence',
              None, 'There is a path leading Northeast somewhere and there is a broken fence south of here.')
s_house = Room('South of House', 'Living Room', 'Garden', 'West of House', 'East of House', None, None, None, None,
               None, None, 'There is a window that is partly open. There seems to be something shining inside')
l_room = Room('Living Room', None, 'South of House', None, None, None, None, None, None, 'Up Stairs',
              'Down Stairs', 'There seems to be an upstairs and downstairs and not much else...You should look around.')
k_room = Room('Kitchen', None, None, 'Living Room', None, None, None, None, None, None, None,
              'There is a fridge, an island, and cupboards.'
              '\n There is a knife on a cutting board, a sink, a coffee machine, coffee grounds, and a mug')
up_stairs = Room('Up Stairs', None, None, 'Justin Timberlakes Room', 'Guest Room', None, None, None, None,
                 None, 'Living Room', 'There is a room WEST of here and a room EAST of here.'
                                      'There is a mirror and a vase that has some flowers')
jt_room = Room('Justin Timberlakes', None, None, None, 'Up Stairs', None, None, None, None, None, None,
               'There is a phone on the bedside table. There is also a TV, bed, and a drawer.')
parking_lot = Room('Parking Lot', 'Garage', 'Living Room', None, None, None, None, None, None, None, None,
                   'There is a garage that is open. Inside, there is are 3 boxes with stuff inside.')
d_house = Room('Dog House', 'Dogs Room', 'Back Yard', None, None, None, None, None, None, None, None,
               'There is a big dog house and from outside you can hear a big dog barking. Will you go inside?')
d_room = Room('Dog Room', None, 'Dog House', None, None, None, None, None, None, None, None,
              'There is a small dog in here and it seems to want something. You cannot get '
              'close enough to it to see what is on its collar.')
y_back = Room('Back Yard', None, 'Shed', 'Kitchen', None, None, None, None, None, None, None,
              'There is a shed south of here. There could be something useful in there.')
shed = Room('Shed', 'Back Yard', 'Garden', None, None, None, None, None, None, None, None,
            'There are two paths one goes Southwest and one goes north. Inside there is a picture.')
d_stairs = Room('Down Stairs', None, None, None, None, None, None, None, None, 'Living Room', None,
                'It is dark and there is a room with a whole bunch of junk.')
current_node = f_gate

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_direction:
        pos = short_direction.index(command)
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Found")
