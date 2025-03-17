from .models import SaleOrder, SaleOrderItem
from .serializers import SaleOrderItemSerializer, SaleOrderSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class SaleOrderViewSet(viewsets.ModelViewSet):
    queryset = SaleOrder.objects.all()
    serializer_class = SaleOrderSerializer

    @action(detail=True, methods=['post'])
    def validate_sale(self, request, pk):
        sale = SaleOrder.objects.get(pk=pk)
        if sale.completed: return Response({'message': 'already validated'}, status=400)

        for sale_item in sale.order_items.all():
            item = sale_item.item
            item.stock_qty -= sale_item.qty
            item.save()
        sale.completed = True
        sale.save()
        return Response({'message': 'sale validated successfully'}, status=200)
class SaleOrderItemViewSet(viewsets.ModelViewSet):
    queryset = SaleOrderItem.objects.all()
    serializer_class = SaleOrderItemSerializer



