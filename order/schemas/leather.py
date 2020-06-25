leather_serial_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'name': {'type': 'string', 'required': True, 'empty': False}
    }

leather_schema = {
    'id': {
        'type': 'number',
        'required': True,
        'empty': False
        },
    'code': {
        'type': 'string',
        'required': True,
        'empty': False
        },
    'serial': {
        'type': 'dict',
        'required': True,
        'empty': False,
        'schema': leather_serial_schema
        },
    'image': {
        'type': 'string',
        'required': True,
        'empty': False
        },
    }
