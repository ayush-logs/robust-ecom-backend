from rest_framework import routers

from products.views import CategoryViewSet, ProductViewSet

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = router.urls
