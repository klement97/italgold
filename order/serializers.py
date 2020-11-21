from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from order.models import Leather, Order
from order.models import LeatherSerial
from order.models import Product, ProductCategory


class LeatherSerializer(ModelSerializer):
    class Meta:
        model = Leather
        fields = ['id', 'code', 'image']


class LeatherSerialSerializer(ModelSerializer):
    leathers = LeatherSerializer(many=True)

    class Meta:
        model = LeatherSerial
        fields = ['id', 'name', 'leathers']


class OrderReadSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    phone = serializers.CharField()
    address = serializers.CharField()
    products = serializers.JSONField()
    inner_leather = LeatherSerializer()
    outer_leather = LeatherSerializer()
    date_created = serializers.DateTimeField()
    date_last_updated = serializers.DateTimeField()


class OrderWriteSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'first_name', 'last_name', 'phone', 'address', 'products',
            'inner_leather', 'outer_leather'
        ]

    def create(self, validated_data):
        products = validated_data.pop('products')
        product_id_price = Product.get_id_price_mapping(ids={unit['product'] for unit in products})

        for index, unit in enumerate(products):
            products[index]['price'] = float(product_id_price.get(unit['product']))
        validated_data['products'] = products

        return super().create(validated_data)


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'image', 'category', 'price', 'properties']
