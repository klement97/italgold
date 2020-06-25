from django.urls import path

from order.views.product_views import ProductRetrieveAPIView

urlpatterns = [
    path('product/<int:pk>/', ProductRetrieveAPIView.as_view(), name='product')
    ]
