from rest_framework.serializers import ModelSerializer

from order.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'first_name', 'last_name', 'phone', 'address', 'products',
            'inner_leather', 'outer_leather'
            ]
