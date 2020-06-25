from order.schemas.leather import leather_schema

product_category_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'name': {'type': 'string', 'required': True, 'empty': False}
    }

product_schema = {
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
    'title': {
        'type': 'string',
        'required': True,
        'empty': True
        },
    'description': {
        'type': 'string',
        'required': True,
        'empty': True
        },
    'image': {
        'type': 'string',
        'required': True,
        'empty': False
        },
    'category': {
        'type': 'dict',
        'required': True,
        'empty': False,
        'schema': product_category_schema
        },
    'inner_leather': {
        'type': 'dict',
        'required': True,
        'empty': False,
        'schema': leather_schema
        },
    'outer_leather': {
        'type': 'dict',
        'required': True,
        'empty': False,
        'schema': leather_schema
        },
    # Decimal values are serialized as strings
    'price': {
        'type': 'string',
        'required': True,
        'empty': False
        },
    'height': {
        'type': 'string',
        'required': True,
        'empty': True,
        'nullable': True
        },
    'width': {
        'type': 'string',
        'required': True,
        'empty': True,
        'nullable': True
        },
    'length': {
        'type': 'string',
        'required': True,
        'empty': True,
        'nullable': True
        },
    }
