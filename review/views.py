from django.shortcuts import get_object_or_404
from review.serializers import ReviewSerializer
from review.models import Review
from products.models import Product
from accounts.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from e_commerce.throttle import GeneralAPIsThrottle


class ReviewAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request, slug):
        product_data=get_object_or_404(Product, slug=slug)
        data=Review.objects.filter(product=product_data)
        serial=ReviewSerializer(data, many=True)
        return Response(serial.data)

    def post(self, request, slug):
        serial=ReviewSerializer(data=request.data)
        if serial.is_valid():
            product_data=get_object_or_404(Product, slug=slug)
            serial.save(product=product_data, user=request.user)
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)

class ReviewIndividualAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request, slug, pk):
        product_data=get_object_or_404(Product, slug=slug)
        profile_data=get_object_or_404(Profile, user=request.user)
        data=get_object_or_404(Review, product=product_data, id=pk, user=profile_data)
        serial=ReviewSerializer(data)
        return Response(serial.data)

    def put(self, request, slug, pk):
        product_data=get_object_or_404(Product, slug=slug)
        profile_data=get_object_or_404(Profile, user=request.user)
        instance=get_object_or_404(Review, product=product_data, id=pk, user=profile_data)
        serial=ReviewSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)

    def delete(self, request, slug, pk):
        product_data=get_object_or_404(Product, slug=slug)
        profile_data=get_object_or_404(Profile, user=request.user)
        instance=get_object_or_404(Review, product=product_data, id=pk, user=profile_data)
        instance.delete()
        return Response({ 'message':'data deleted' }, status=204)

