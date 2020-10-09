from django_filters import rest_framework as filters

from order.models import Product


class ProductFilter(filters.FilterSet):
    code = filters.CharFilter(method='get_by_code')

    class Meta:
        model = Product
        fields = ['category']

    @staticmethod
    def get_by_code(queryset, _, value):
        return queryset.filter(properties__code__icontains=value)
