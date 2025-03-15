from django.db import models
from core.models import BaseModel
from items.models import Item

def generate_order_name():

    last_order = PurchaseOrder.objects.order_by('-id').first()
    if last_order:
        return f'P0000{last_order.id + 1}'
    return 'P00001'

class PurchaseOrder(BaseModel):
    name = models.CharField(max_length=250, default=generate_order_name, unique=True, editable=False)
    completed = models.BooleanField(default=False, editable=False)

    def __str__(self):
        return self.name

class PurchaseOrderItem(BaseModel):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='purchase_order_items')
    qty = models.PositiveIntegerField(default=0)
    order = models.ForeignKey(PurchaseOrder, on_delete=models.CASCADE, related_name='order_items')