import django_filters
from product.models import *


class ProductFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(
        lookup_expr='icontains', label='')

    class Meta:
        model = Product
        fields = ['category', ]
