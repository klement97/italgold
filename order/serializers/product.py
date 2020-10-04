from rest_framework.serializers import ModelSerializer

from order.models import Product, ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()

    class Meta:
        model = Product
        fields = ['id', 'image', 'category', 'price', 'properties']
