from rest_framework.generics import CreateAPIView

from order.serializers import OrderSerializer


class OrderCreateAPIView(CreateAPIView):
    serializer_class = OrderSerializer
