from django.urls import path

from order.views.product_views import ProductCategoryListAPIView, ProductListAPIView, \
    ProductRetrieveAPIView

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product'),
    path('product/', ProductListAPIView.as_view(), name='product'),
    path('product-category/', ProductCategoryListAPIView.as_view(), name='product-category')
    ]
