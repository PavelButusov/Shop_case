from rest_framework import routers
from .views_api import ProductViewSet, BasketedProductViewSet

router = routers.DefaultRouter()
router.register(r'catalogue', ProductViewSet)
router.register(r'basket', BasketedProductViewSet)

urlpatterns = router.urls
