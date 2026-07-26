from django.shortcuts import get_object_or_404
from orders.models import Order
from orders.serializers import OrderSerializer
from accounts.models import Profile
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin
from e_commerce.throttle import GeneralAPIsThrottle


class MyOrderAPI(ListAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]        
    serializer_class=OrderSerializer
    def get_queryset(self):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        return Order.objects.filter(user=profile_data)

    def perform_create(self, serializer):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        serializer.save(user=profile_data)

class MyOrderAPIIndividual(RetrieveAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
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


    