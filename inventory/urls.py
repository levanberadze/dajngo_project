from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('items.urls')),
    path('purchase_orders/', include('purchase_orders.urls')),
    path('sale_orders/', include('sale_orders.urls')),
]
