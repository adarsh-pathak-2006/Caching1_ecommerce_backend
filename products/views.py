from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Product, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin

class CategoryAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryIndividualAPI(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='slug'

class ProductAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductIndividualAPI(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method=="GET":
            return [IsAuthenticated()]
        else:
            return [IsAdmin()]
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='slug'