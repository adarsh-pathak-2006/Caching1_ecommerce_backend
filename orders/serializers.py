from orders.models import Order, OrderItem
from rest_framework.serializers import ModelSerializer
from accounts.serializers import ProfileGetSerializer
from products.serializers import ProductGetSerializer

class OrderSerializer(ModelSerializer):
    user=ProfileGetSerializer(read_only=True)
    class Meta:
        model=Order
        fields='__all__'

class OrderGetSerializer(ModelSerializer):
    class Meta:
        model=Order
        fields=['orderId', 'order_status', 'created_at', 'payment_status']

class OrderItemSerializer(ModelSerializer):
    order=OrderGetSerializer(read_only=True)
    item=ProductGetSerializer(read_only=True)
    class Meta:
        model=OrderItem
        fields='__all__'