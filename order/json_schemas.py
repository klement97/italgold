leather_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'code': {'type': 'string', 'required': True, 'empty': False},
    'image': {'type': 'string', 'required': True, 'empty': False},
    }

leather_serial_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'name': {'type': 'string', 'required': True, 'empty': False},
    'leathers': {'type': 'list', 'required': True, 'empty': True,
                 'schema': leather_schema},
    }

product_category_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'name': {'type': 'string', 'required': True, 'empty': False}
    }

product_properties_schema = {
    'code': {'type': 'string', 'required': False, 'empty': True,
             'nullable': True},
    'height': {'type': 'string', 'required': False, 'empty': True,
               'nullable': True},
    'width': {'type': 'string', 'required': False, 'empty': True,
              'nullable': True},
    'length': {'type': 'string', 'required': False, 'empty': True,
               'nullable': True},
    }

product_schema = {
    'id': {'type': 'number', 'required': True, 'empty': False},
    'image': {'type': 'string', 'required': True, 'empty': False},
    'category': {'type': 'dict', 'required': True, 'empty': False,
                 'schema': product_category_schema},
    # Decimal values are serialized as strings
    'price': {'type': 'string', 'required': True, 'empty': False},
    'properties': {'type': 'dict', 'required': True, 'empty': False,
                   'schema': product_properties_schema},
    }
