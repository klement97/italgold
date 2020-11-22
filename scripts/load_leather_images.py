from order.models import Leather

leathers = Leather.objects.select_related('serial').all()

for leather in leathers:
    serial_name = leather.serial.name.lower().replace(' ', '-')
    code = leather.code.lower().replace(' ', '-')
    print(f'{serial_name}-{code}.jpg')
