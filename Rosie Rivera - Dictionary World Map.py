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
        'DESCRIPTION': 'There is a window you could go through if you had something to pry it with.',
        'PATHS': {
            'NORTH': 'HOUSE'
        }
    }
}
current_node = world_map['F-GATE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'NORTHEAST', 'NORTHWEST', 'SOUTHEAST', 'SOUTHWEST', 'UP', 'DOWN']

while True:
    print(current_node["NAME"])
    print(current_node['DESCRIPTION'])
    command = input('>_')
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not Found")
    if command == 'quit':
        quit(0)
