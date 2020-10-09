product_category_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'name': {'type': 'string', 'required': True, 'empty': False}
    }

product_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'image': {'type': 'string', 'required': True, 'empty': False},
    'category': {'type': 'dict', 'required': True, 'empty': False,
                 'schema': product_category_schema},
    # Decimal values are serialized as strings
    'price': {'type': 'string', 'required': True, 'empty': False},
    'properties': {
        'code': {'type': 'string', 'required': False, 'empty': True, 'nullable': True},
        'height': {'type': 'string', 'required': False, 'empty': True, 'nullable': True},
        'width': {'type': 'string', 'required': False, 'empty': True, 'nullable': True},
        'length': {'type': 'string', 'required': False, 'empty': True, 'nullable': True},
        },
    }
