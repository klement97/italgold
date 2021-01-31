from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from order.filters import ProductFilter
from order.models import Leather, LeatherSerial, Order
from order.models import Product, ProductCategory
from order.serializers import LeatherSerialSerializer, LeatherSerializer, \
    OrderReadSerializer
from order.serializers import OrderWriteSerializer
from order.serializers import ProductCategorySerializer, ProductSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderWriteSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer

    @method_decorator(cache_page(None))  # never expire
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.select_related('category').filter(deleted=False)
    serializer_class = ProductSerializer

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.select_related('category').filter(deleted=False)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    @method_decorator(cache_page(60 * 60 * 2))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(deleted=False)
    serializer_class = ProductCategorySerializer

    @method_decorator(cache_page(None))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class LeatherListAPIView(ListAPIView):
    serializer_class = LeatherSerializer
    queryset = Leather.objects.filter(deleted=False)
    filterset_fields = ('code', 'serial')

    @method_decorator(cache_page(None))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class LeatherSerialListAPIView(ListAPIView):
    serializer_class = LeatherSerialSerializer
    queryset = LeatherSerial.objects.prefetch_related('leathers').filter(
        deleted=False)

    @method_decorator(cache_page(None))
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
