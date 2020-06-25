from rest_framework.generics import RetrieveAPIView

from order.models import Product
from order.serializers.product_serializers import ProductSerializer


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects \
        .select_related('category', 'inner_leather', 'outer_leather') \
        .filter(deleted=False)
    serializer_class = ProductSerializer
