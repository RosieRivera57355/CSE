world_map ={
    'F-GATE': {
        'NAME': 'FRONT GATE',
        'DESCRIPTION': 'The fence seems to continue south and it is locked. It seems you must find another way in so'
        'that you will not get caught',
        'PATHS': {
            'WEST': 'Parking Lot',
            'SOUTH': 'Back Fence'
        }
    },
    'B-FENCE': {
        'NAME': 'BROKEN FENCE',
        'DESCRIPTION': 'The Fence is loose and there is more of the fence to the east',
        'PATHS': {
            'NORTH': 'FRONT GATE',
            'NORTHWEST': 'GARDEN',
            'EAST': 'SEWER LID'
        }
    },
    'GARDEN': {
        'NAME': 'FLOWER GARDEN',
        'DESCRIPTION': 'There is a path leading Northeast somewhere and there is a broken fence south of here.',
        'PATHS': {
            'SOUTHEAST': 'B-FENCE',
            'NORTH': 'SOUTH OF HOUSE',
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
current_node = world_map['SOUTHHOUSE']
print(current_node['DESCRIPTION'])
print(current_node['NAME'])

