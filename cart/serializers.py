from rest_framework.serializers import ModelSerializer
from cart.models import Cart, CartItem
from accounts.serializers import ProfileGetSerializer


class CartItemSerializer(ModelSerializer):
    class Meta:
        model=CartItem
        fields='__all__'
        read_only_fields=['total_price']

class CartSerializers(ModelSerializer):
    profile=ProfileGetSerializer(read_only=True)
    cart_items=CartItemSerializer(read_only=True, many=True)
    class Meta:
        model=Cart
        fields='__all__'