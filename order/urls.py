from django.urls import path

from order.views.product_views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('product/', ProductListAPIView.as_view(), name='product')
    ]
