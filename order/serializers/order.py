from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from order.models import Order, OrderUnit


class OrderUnitSerializer(ModelSerializer):
    class Meta:
        model = OrderUnit
        fields = ['id', 'product', 'quantity', 'notes', 'width', 'height', 'length']


class OrderSerializer(ModelSerializer):
    order_units = OrderUnitSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'order_units']

    @atomic()
    def create(self, validated_data):
        order_units = validated_data.pop('order_units')

        order = Order.objects.create(**validated_data)

        units = [OrderUnit(**{**unit}, order=order, price=unit['product'].price,
                           inner_leather_id=self.initial_data.get('inner_leather'),
                           outer_leather_id=self.initial_data.get('outer_leather'),
                           )
                 for unit in order_units]

        OrderUnit.objects.bulk_create(units)

        return order
