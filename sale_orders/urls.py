from django.urls import path
from .views import SaleOrderItemViewSet, SaleOrderViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter(use_regex_path=False)
router.register('sales', SaleOrderViewSet)
router.register('order_sales', SaleOrderItemViewSet)

urlpatterns = [
] + router.urls
