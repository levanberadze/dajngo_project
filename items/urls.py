from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter(use_regex_path=False)
router.register('items', views.ItemViewSet)
router.register('categories', views.CategoryViewSet)
router.register('categories/<category_id>/items', views.CategoryItemViewSet, basename='categories-items')


urlpatterns = [
] + router.urls
