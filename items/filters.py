import django_filters
from .models import Item
from datetime import date, timedelta


class ItemFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')
    in_stock = django_filters.BooleanFilter(method='filter_in_stock')


    def filter_in_stock(self, queryset, name, value):
        if not value: return queryset
        return queryset.filter(stock_qty__gt=0)


    near_expiry = django_filters.BooleanFilter(method='filter_near_expiry')

    def filter_near_expiry(self, queryset, name, value):
        if not value: return queryset
        queryset = queryset.filter(expiry_date__lte=date.today() + timedelta(days=5))
        return queryset
