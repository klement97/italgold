from django_filters import rest_framework as filters

from order.models import Product


class ProductFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    price = filters.NumericRangeFilter()

    class Meta:
        model = Product
        fields = ['category', 'inner_leather', 'outer_leather']
