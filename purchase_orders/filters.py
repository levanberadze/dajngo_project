import django_filters
from .models import PurchaseOrder, PurchaseOrderItem


class PurchaseOrderFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = PurchaseOrder
        fields = 'name'


class PurchaseOrderItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    purchase_order = django_filters.CharFilter('purchase_order__name')
    class Meta:
        model = PurchaseOrderItem
        fields = 'name'
