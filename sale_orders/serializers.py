from rest_framework import serializers
from .models import SaleOrder, SaleOrderItem


class SaleOrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaleOrderItem
        fields = '__all__'

        def create(self, validated_data):
            order = validated_data.get('order')
            item = validated_data.get('item')
            qty = validated_data.get('qty')

            for order_item in order.order_items.all():
                if order_item.item == item:
                    order_item.qty += qty
                    order_item.save()
                    return order_item
            return super().create(validated_data)


class SaleOrderSerializer(serializers.ModelSerializer):

    order_items = SaleOrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = SaleOrder
        fields = '__all__'