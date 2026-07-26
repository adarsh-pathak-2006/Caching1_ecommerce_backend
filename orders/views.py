from django.shortcuts import get_object_or_404
from orders.models import OrderItem, Order
from orders.serializers import OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from accounts.models import Profile
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin


class MyOrderAPI(ListCreateAPIView):
    permission_classes=[IsAuthenticated]        
    serializer_class=OrderSerializer
    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

    def perform_create(self, serializer):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        serializer.save(user=profile_data)

class MyOrderAPIIndividual(RetrieveAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=OrderSerializer

    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

class AllOrdersAPI(ListAPIView):
    permission_classes=[IsAdmin]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class AllOrderAPIIndividual(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAdmin]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class OrderItemsAPI(APIView):
    permission_classes=[IsAuthenticated]
    def get(self, request, pk):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        order_data=get_object_or_404(Order, user=profile_data, id=pk)
        data=OrderItem.objects.filter(order=order_data)
        serial=OrderItemSerializer(data, many=True)
        return Response(serial.data, status=200)

    def patch(self ,request, pk):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        order_data=get_object_or_404(Order, user=profile_data, id=pk)
        instance=OrderItem.objects.filter(order=order_data)
        serial=OrderItemSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)

    def delete(self, request, pk):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        order_data=get_object_or_404(Order, user=profile_data, id=pk)
        instance=OrderItem.objects.filter(order=order_data)
        instance.delete()
        return Response({ 'message':'data deleted successfully' }, status=204)

    