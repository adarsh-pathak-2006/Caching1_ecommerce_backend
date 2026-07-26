from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from cart.models import Cart, CartItem
from cart.serializers import CartItemwriteSerializer, CartSerializers, CartItemGetSerializer, CartItemUpdateSerializer
from e_commerce.throttle import GeneralAPIsThrottle
from rest_framework.permissions import IsAuthenticated
from accounts.models import Profile
from rest_framework.response import Response


class CartAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        cart_data=get_object_or_404(Cart, profile=profile_data)
        serial=CartSerializers(cart_data)
        return Response(serial.data, status=200)

class CartItemAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        cart_data=get_object_or_404(Cart, profile=profile_data)
        data=CartItem.objects.filter(cart=cart_data)
        serial=CartItemGetSerializer(data, many=True)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=CartItemwriteSerializer(data=request.data)
        if serial.is_valid():
            profile_data=get_object_or_404(Profile, user=self.request.user)
            cart_data=get_object_or_404(Cart, profile=profile_data)
            serial.save(cart=cart_data)
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)

    def put(self, request, pk):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        cart_data=get_object_or_404(Cart, profile=profile_data)
        instance=get_object_or_404(CartItem, id=pk, cart=cart_data)
        serial=CartItemUpdateSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)

    def delete(self, request, pk):
        profile_data=get_object_or_404(Profile, user=self.request.user)
        cart_data=get_object_or_404(Cart, profile=profile_data)
        instance=get_object_or_404(CartItem, id=pk, cart=cart_data)
        instance.delete()
        return Response({'message':'cart item deleted'}, status=204)


           
    
    