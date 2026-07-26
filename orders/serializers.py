from orders.models import Order, OrderItem
from rest_framework.serializers import ModelSerializer
from accounts.serializers import ProfileGetSerializer
from cart.serializers import CartSerializers

class OrderSerializer(ModelSerializer):
    user=ProfileGetSerializer(read_only=True)
    cart=CartSerializers(read_only=True)
    class Meta:
        model=Order
        fields='__all__'
        read_only_fields=['final_amount']

class OrderGetSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields=['orderId', 'order_status', 'created_at', 'payment_status']
