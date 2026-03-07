from django.urls import path, include
from rest_framework import routers

from products.views import CategoryViewSet, ProductViewSet, UserViewSet

router = routers.SimpleRouter()
router.register(r"categories", CategoryViewSet)
router.register(r"products", ProductViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("register/", UserViewSet.as_view(), name="register"),
]
