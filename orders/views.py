from django.shortcuts import get_object_or_404
from orders.models import Order
from orders.serializers import OrderSerializer
from accounts.models import Profile
from rest_framework.generics import RetrieveUpdateAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin
from e_commerce.throttle import GeneralAPIsThrottle, OrderRelatedThrottle
from django.db import models
from cart.models import Cart, CartItem
from rest_framework.response import Response


class MyOrderAPI(ListAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]        
    serializer_class=OrderSerializer
    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

class OrderCreationAPI(APIView):
    throttle_classes=[OrderRelatedThrottle]
    permission_classes=[IsAuthenticated]
    def post(self, request):
        profile_data=get_object_or_404(Profile, user=request.user)
        cart_data=get_object_or_404(Cart, profile=profile_data)
        serial=OrderSerializer(data=request.data)
        if serial.is_valid():
            cartitem=CartItem.objects.filter(cart=cart_data)
            total_cart_price=cartitem.aggregate(total_price=models.Sum('total_price'))
            tax=serial.validated_data['tax']
            shipping_charges=serial.validated_data['shipping_charges']
            serial.save(user=profile_data, cart=cart_data, final_amout=total_cart_price['total_price']+tax+shipping_charges)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)                

class MyOrderAPIIndividual(RetrieveUpdateAPIView):
    throttle_classes=[OrderRelatedThrottle]
    def get_permissions(self):
        if self.request.method=="PUT":
            return [IsAdmin()]
        else:
            return [IsAuthenticated()]
        
    serializer_class=OrderSerializer

    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

class AllOrdersAPI(ListAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAdmin]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class AllOrderAPIIndividual(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAdmin]
    queryset=Order.objects.all()
    serializer_class=OrderSerializer


    