from django.conf import settings
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.exceptions import bad_request
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView

from order.filters import ProductFilter
from order.models import Leather, LeatherSerial, Order
from order.models import Product, ProductCategory
from order.serializers import LeatherSerialSerializer, LeatherSerializer, OrderReadSerializer
from order.serializers import OrderWriteSerializer
from order.serializers import ProductCategorySerializer, ProductSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderWriteSerializer


class OrderRetrieveAPIView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderReadSerializer


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


@api_view(['GET'])
def download_db_dump(request):
    query_params = request.query_params
    if 'user' not in query_params or 'password' not in query_params:
        return bad_request(request, KeyError)

    if not (query_params['user'] == settings.DB_USER and
            query_params['password'] == settings.DB_PASSWORD):
        return bad_request(request, ValueError)

    with open(f'{settings.BASE_DIR}/db.json', 'r') as dump:
        return HttpResponse(dump, content_type='applications/json')
