from django.db.transaction import atomic
from rest_framework.serializers import ModelSerializer

from order.models import Order


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'first_name', 'last_name', 'phone', 'address', 'order_units']

    @atomic()
    def create(self, validated_data):
        pass
