from django_filters import rest_framework as filters

from order.models import Product


class ProductFilter(filters.FilterSet):
    code = filters.CharFilter(method='get_by_code')
    sub_category = filters.NumberFilter(method='get_by_sub_category')

    class Meta:
        model = Product
        fields = ['category']

    @staticmethod
    def get_by_code(queryset, _, value):
        return queryset.filter(properties__code__icontains=value)

    @staticmethod
    def get_by_sub_category(queryset, _, value):
        if int(value) == 0:
            return queryset

        return queryset.filter(sub_category_id=value)

