from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from cart.models import Cart, CartItem
from accounts.serializers import ProfileGetSerializer
from products.models import Product
from products.serializers import ProductGetSerializer


class CartItemwriteSerializer(ModelSerializer):
    product=PrimaryKeyRelatedField(Product.objects.all())
    class Meta:
        model=CartItem
        fields='__all__'
        read_only_fields=['total_price']

class CartItemGetSerializer(ModelSerializer):
    product=ProductGetSerializer(read_only=True)
    class Meta:
        model=CartItem
        fields='__all__'

class CartItemUpdateSerializer(ModelSerializer):
    product=ProductGetSerializer(read_only=True)
    class Meta:
        model=CartItem
        fields=['cart', 'product', 'quantity']
        read_only_fields=['cart']

class CartSerializers(ModelSerializer):
    profile=ProfileGetSerializer(read_only=True)
    cart_items=CartItemGetSerializer(read_only=True, many=True)
    class Meta:
        model=Cart
        fields='__all__'