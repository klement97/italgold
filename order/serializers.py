from rest_framework.serializers import ModelSerializer

from order.models import Leather
from order.models import LeatherSerial
from order.models import Order
from order.models import Product, ProductCategory


class LeatherSerializer(ModelSerializer):
    class Meta:
        model = Leather
        fields = ['id', 'code', 'serial', 'image']


class LeatherSerialSerializer(ModelSerializer):
    leathers = LeatherSerializer(many=True)

    class Meta:
        model = LeatherSerial
        fields = ['id', 'name', 'leathers']


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'first_name', 'last_name', 'phone', 'address', 'products',
            'inner_leather', 'outer_leather'
            ]


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'image', 'category', 'price', 'properties']
