from django_filters import rest_framework as filters

from order.models import Product


class ProductFilter(filters.FilterSet):
    price = filters.NumericRangeFilter()

    class Meta:
        model = Product
        fields = ['category']
