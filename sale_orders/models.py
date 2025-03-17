from django.db import models
from core.models import BaseModel
from items.models import Item

def generate_sale_name():

    last_sale = SaleOrder.objects.order_by('-id').first()
    if last_sale:
        return f'S0000{last_sale.id + 1}'
    return 'S00001'


class SaleOrder(BaseModel):
    name = models.CharField(max_length=250, default=generate_sale_name, unique=True, editable=False)
    completed = models.BooleanField(default=False, editable=False)


class SaleOrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    order = models.ForeignKey(SaleOrder, on_delete=models.CASCADE, related_name='order_items')
