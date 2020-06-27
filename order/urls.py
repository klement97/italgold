from django.urls import path

from order.views.leather_views import LeatherListAPIView, LeatherSerialListAPIView
from order.views.product_views import ProductCategoryListAPIView, ProductListAPIView, \
    ProductRetrieveAPIView

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product-category/', ProductCategoryListAPIView.as_view(), name='product-category'),

    path('leather/', LeatherListAPIView.as_view(), name='leather'),
    path('leather-serial/', LeatherSerialListAPIView.as_view(), name='leather-serial')
    ]
