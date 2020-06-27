from rest_framework.serializers import ModelSerializer

from order.models import Product, ProductCategory
from order.serializers.leather import LeatherSerializer


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    inner_leather = LeatherSerializer()
    outer_leather = LeatherSerializer()

    class Meta:
        model = Product
        fields = [
            'id', 'code', 'title', 'description', 'image',
            'category', 'inner_leather', 'outer_leather',
            'price', 'height', 'width', 'length'
            ]
