from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from order.models import Leather, Order
from order.models import LeatherSerial


class IDNameSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


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
    date_created = serializers.DateTimeField()
    date_last_updated = serializers.DateTimeField()


class OrderWriteSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = [
            'id', 'first_name', 'last_name', 'phone', 'address', 'products',
            ]

    def create(self, validated_data):
        validated_data['products'] = Order.sanitize_products_field(products=validated_data['products'])
        return super().create(validated_data)


class ProductSubCategorySerializer(IDNameSerializer):
    pass


class ProductCategorySerializer(IDNameSerializer):
    pass


class ProductCategoryListSerializer(ProductCategorySerializer):
    sub_categories = ProductSubCategorySerializer(many=True)


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    image = serializers.ImageField()
    price = serializers.DecimalField(max_digits=10, decimal_places=3)
    properties = serializers.JSONField()
    category = ProductCategorySerializer()
