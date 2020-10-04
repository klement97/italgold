from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from order.models import Product, ProductCategory


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ['id', 'name']


class ProductSerializer(ModelSerializer):
    category = ProductCategorySerializer()
    data = SerializerMethodField()

    class Meta:
        model = Product
        fields = ['id', 'image', 'category', 'price', 'data']

    def get_data(self, product: Product):
        return
