from rest_framework.permissions import (IsAuthenticated,
                                        AllowAny)
from rest_framework import viewsets
from .models import BasketedProduct, Product
from .serializers import (ProductSerializer,
                          BasketedProductSerializer)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class BasketedProductViewSet(viewsets.ModelViewSet):
    queryset = BasketedProduct.objects.all()
    serializer_class = BasketedProductSerializer
    permission_classes = [IsAuthenticated]
