from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet
from rest_framework import generics

from products.models import Product, Category
from products.serializers import (
    ProductSerializer,
    CategorySerializer,
    UserRegistrationSerializer,
)
from django.contrib.auth import get_user_model

User = get_user_model()


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryViewSet(ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
