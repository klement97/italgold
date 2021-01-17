from django.urls import path

from order.views import (
    LeatherListAPIView, LeatherSerialListAPIView, OrderCreateAPIView, OrderRetrieveAPIView,
    ProductCategoryListAPIView,
    ProductListAPIView, ProductRetrieveAPIView, download_db_dump
    )

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product-category/', ProductCategoryListAPIView.as_view(), name='product-category'),

    path('leather/', LeatherListAPIView.as_view(), name='leather'),
    path('leather-serial/', LeatherSerialListAPIView.as_view(), name='leather-serial'),

    path('order/', OrderCreateAPIView.as_view(), name='order'),
    path('order/<int:pk>/', OrderRetrieveAPIView.as_view(), name='order'),

    path('db/', download_db_dump)
    ]
