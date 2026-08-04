from django.shortcuts import get_object_or_404
from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Product, Category
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin
from e_commerce.throttle import GeneralAPIsThrottle
from django.core.cache import cache
from rest_framework.response import Response


class CategoryAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]

    def get(self, request):
        cached_data=cache.get("categories")
        if cached_data:
            return Response(cached_data, status=200)
        data=Category.objects.all()
        serial=CategorySerializer(data, many=True)
        cache.set("categories", serial.data, timeout=500)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=CategorySerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            cache.delete("categories")
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)

    
class CategoryIndividualAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]

    def get(self, request, slug):
        cached_data=cache.get(f"category_{slug}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(Category, slug=slug)
        serial=CategorySerializer(data)
        cache.set(f"category_{slug}", serial.data, timeout=500)
        return Response(serial.data, status=200)

    def patch(self, request, slug):
        instance=get_object_or_404(Category, slug=slug)
        serial=CategorySerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"category_{slug}")
            cache.delete("categories")
            serial.save()
            return Response(serial.data)

    def delete(self, request, slug):
        data=get_object_or_404(Category, slug=slug)
        data.delete()
        cache.delete(f"category_{slug}")
        cache.delete("categories")

class ProductAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    def get(self, request):
        cached_data=cache.get("products")
        if cached_data:
            return Response(cached_data, status=200)
        data=Product.objects.all()
        serial=ProductSerializer(data, many=True)
        cache.set("products", serial.data, timeout=500)
        return Response(serial.data, status=200)

    def post(self, request):
        serial=ProductSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            cache.delete("products")
            return Response(serial.data, status=201)
        else:
            return Response(serial.errors, status=400)

class ProductIndividualAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    def get(self, request, slug):
        cached_data=cache.get(f"product_{slug}")
        if cached_data:
            return Response(cached_data, status=200)
        data=get_object_or_404(Product, slug=slug)
        serial=ProductSerializer(data)
        cache.set(f"product_{slug}", serial.data, timeout=500)
        return Response(serial.data, status=200)

    def patch(self, request, slug):
        instance=get_object_or_404(Product, slug=slug)
        serial=ProductSerializer(instance, data=request.data, partial=True)
        if serial.is_valid():
            cache.delete(f"product_{slug}")
            cache.delete("products")
            serial.save()
            return Response(serial.data)

    def delete(self, request, slug):
        data=get_object_or_404(Product, slug=slug)
        data.delete()
        cache.delete(f"product_{slug}")
        cache.delete("products")