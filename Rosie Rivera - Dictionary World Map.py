world_map ={
    'WESTHOUSE': {
        'NAME': 'WEST OF HOUSE',
        'DESCRIPTION': 'You are west of a small house',
        'PATHS': {
            'NORTH': 'NORTHHOUSE',
            'SOUTH': 'SOUTHHOUSE'
        }
    },
    'NORTHHOUSE': {
        'NAME': 'NORTH OF HOUSE',
        'DESCRIPTION': ' Insert description here',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    },
    'SOUTHHOUSE': {
        'NAME': 'SOUTH OF HOUSE',
        'DESCRIPTION': 'Insert description here',
        'PATHS': {
            'WEST': 'WESTHOUSE'
        }
    }
}
current_node = world_map['SOUTHHOUSE']
print(current_node['DESCRIPTION'])
print(current_node['NAME'])