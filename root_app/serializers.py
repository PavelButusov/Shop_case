from rest_framework import serializers
from .models import Product, BasketedProduct


class ProductSerializer(serializers.ModelSerializer):
    # title = serializers.CharField(max_length=200)
    # descr = serializers.CharField(max_length=2048, allow_blank=True)
    class Meta:
        model = Product
        fields = '__all__'

class BasketedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BasketedProduct
        fields = '__all__'
