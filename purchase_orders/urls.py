from django.urls import path
from .views import PurchaseOrderViewSet, PurchaseOrderItemViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(use_regex_path=False)
router.register('orders', PurchaseOrderViewSet)
router.register('order_items', PurchaseOrderItemViewSet)

urlpatterns = [
] + router.urls
