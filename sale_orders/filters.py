import django_filters
from .models import SaleOrder, SaleOrderItem


class SaleOrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = SaleOrder
        fields = 'name'


class SaleOrderItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    sale_order = django_filters.CharFilter('sale_order__name')
    class Meta:
        model = SaleOrderItem
        fields = 'name'