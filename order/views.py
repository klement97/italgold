from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response

from order.filters import ProductFilter
from order.models import Leather, LeatherSerial
from order.models import Product, ProductCategory
from order.serializers import LeatherSerialSerializer, LeatherSerializer
from order.serializers import OrderSerializer
from order.serializers import ProductCategorySerializer, ProductSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        return Response(status=status.HTTP_201_CREATED)


class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.select_related('category').filter(deleted=False)
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.select_related('category').filter(deleted=False)
    serializer_class = ProductSerializer
    filterset_class = ProductFilter


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(deleted=False)
    serializer_class = ProductCategorySerializer


class LeatherListAPIView(ListAPIView):
    serializer_class = LeatherSerializer
    queryset = Leather.objects. \
        select_related('serial'). \
        filter(deleted=False)
    filterset_fields = ('code', 'serial')


class LeatherSerialListAPIView(ListAPIView):
    serializer_class = LeatherSerialSerializer
    queryset = LeatherSerial.objects.prefetch_related('leathers').filter(deleted=False)
