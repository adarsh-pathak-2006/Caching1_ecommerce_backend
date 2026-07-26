from django.shortcuts import get_object_or_404
from orders.models import OrderItem, Order
from orders.serializers import OrderSerializer, OrderItemSerializer, OrderGetSerializer
from rest_framework.views import APIView
from accounts.models import Profile
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView


class MyOrderAPI(ListCreateAPIView):
    serializer_class=OrderSerializer
    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

    def perform_create(self, serializer):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        serializer.save(user=profile_data)

class MyOrderAPIIndividual(RetrieveAPIView):
    serializer_class=OrderSerializer

    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

class AllOrdersAPI(ListAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class AllOrderAPIIndividual(RetrieveUpdateDestroyAPIView):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer