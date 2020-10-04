from django.urls import path

from order.views.leather import LeatherListAPIView, LeatherSerialListAPIView
from order.views.order import OrderCreateAPIView
from order.views.product import ProductCategoryListAPIView, ProductListAPIView, \
    ProductRetrieveAPIView

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product-category/', ProductCategoryListAPIView.as_view(), name='product-category'),

    path('leather/', LeatherListAPIView.as_view(), name='leather'),
    path('leather-serial/', LeatherSerialListAPIView.as_view(), name='leather-serial'),

    path('order/', OrderCreateAPIView.as_view(), name='order'),
    ]
