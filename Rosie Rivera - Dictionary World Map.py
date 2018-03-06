world_map = {
    'F-GATE': {
        'NAME': 'FRONT GATE',
        'DESCRIPTION': 'The fence seems to continue south and it is locked.\n It seems you must find another way in so'
        ' that you will not get caught',
        'PATHS': {
            'SOUTH': 'B-FENCE'
        }
    },
    'B-FENCE': {
        'NAME': 'BROKEN FENCE',
        'DESCRIPTION': 'The Fence is loose and there is more of the fence to the east',
        'PATHS': {
            'NORTH': 'F-GATE',
            'NORTHWEST': 'GARDEN',
            'EAST': 'SEWER LID'
        }
    },
    'GARDEN': {
        'NAME': 'FLOWER GARDEN',
        'DESCRIPTION': 'There is a path leading Northeast somewhere and there is a broken fence south of here.',
        'PATHS': {
            'SOUTHEAST': 'B-FENCE',
            'NORTH': 'S-HOUSE',
            'NORTHEAST': 'SHED'
        }
    },
    'S-HOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': 'There is a window that is partly open. There seems to be something shining inside',
        'PATHS': {
            'NORTH': 'L-ROOM',
            'SOUTH': 'GARDEN',
            'WEST': 'W-HOUSE',
            'EAST': 'E-HOUSE'
        }
    },
    'L-ROOM': {
        'NAME': 'HOUSE',
        'DESCRIPTION': 'There seems to be an upstairs and downstairs...You should look around.',
       'PATHS': {
           'DOWN':'D-STAIRS',
           'UP':'U-STAIRS'
       }
    },
    'K-ROOM': {
        'NAME': 'KITCHEN',
        'DESCRIPTION': 'There is a fridge, an island, and cupboards. There is a knife on a cutting board, a coffee'
                       'machine, coffee grounds, and a mug',
        'PATHS': {

        }
    },
    'U-STAIRS': {
        'NAME': 'UPSTAIRS',
        'DESCRIPTION': 'There is a room WEST of here and a room EAST of here. There is a mirror and a vase that has'
                       'some flowers',
        'PATHS': {
            'WEST': 'JT-ROOM',
            'EAST': 'G-ROOM',
            'DOWN': 'L-ROOM'
        }
    },
    'JT-ROOM': {
        'NAME': 'JUSTIN TIMBERLAKES ROOM',
        'DESCRIPTION': 'There is a phone on the bedside table. There is also a TV, bed, and a drawer.',
        'PATHS': {
            'EAST': 'U-STAIRS'
        }
    },
    'PARKING': {
        'NAME': 'PARKING GARAGE',
        'DESCRIPTION': 'There is a garage that is open. Inside, there is are 3 boxes with stuff inside.',
        'PATHS': {
            'UP':'U-STAIRS',
            'SOUTH':'L-ROOM',
            'DOWN':'D-STAIRS'
        }
    },
    'D-HOUSE': {
        'NAME': 'DOG HOUSE',
        'DESCRIPTION': 'There is a big dog house and from outside you can hear a big dog barking. Will you go inside?',
        'PATHS': {
            'SOUTH':'Y-BACK',
            'NORTH':'D-ROOM'
        }
    },
    'D-ROOM': {
        'NAME': 'DOG ROOM',
        'DESCRIPTION': 'There is a small dog in here and it seems to want something. You cannot get close enough to it'
                       'to see what is on its collar.',
        'PATHS': {
            'SOUTH':'D-HOUSE'
        }
    },
    'Y-BACK': {
        'NAME': 'BACKYARD',
        'DESCRIPTION': 'There is a shed south of here. There could be something useful in there.',
        'PATHS': {
            'WEST':'K-ROOM',
            'SOUTH':'SHED'
        }
    },
    'SHED': {
        'NAME': 'SHED'
        'DESCRIPTION': 'There is two paths one goes Southwest and one goes north. Inside there is a picture.',
        'PATHS': {
            'NORTH': 'Y-BACK',
            'SOUTH': 'GARDEN'
        }
    },
    'D-STAIRS': {
        'NAME': 'DOWN STAIRS',
        'DESCRIPTION': 'There seems to be a shrine of some kind. It is pretty creepy down here and you can see \n'
                       'better if you find a light.',
        'PATHS': {
            'UP': 'L-ROOM'
        }
    }
current_node = world_map
directions = ['north', 'south', 'east', 'west', 'northeast', 'northwest', 'southeast', 'southwest', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'ne', 'nw', 'se', 'sw', 'u', 'd']

while True:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input('>_').lower().strip()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Finds the command in short directions (index number)
        pos = short_directions.index(command)
        command = directions[pos]
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Found")
