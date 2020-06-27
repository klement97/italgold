from rest_framework.generics import ListAPIView, RetrieveAPIView

from order.filters import ProductFilter
from order.models import Product, ProductCategory
from order.serializers.product_serializers import ProductCategorySerializer, ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects \
        .select_related('category', 'inner_leather', 'outer_leather',
                        'inner_leather__serial', 'outer_leather__serial') \
        .filter(deleted=False)
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects \
        .select_related('category', 'inner_leather', 'outer_leather',
                        'inner_leather__serial', 'outer_leather__serial') \
        .filter(deleted=False)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(deleted=False)
    serializer_class = ProductCategorySerializer
