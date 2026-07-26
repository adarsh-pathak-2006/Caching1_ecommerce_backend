from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer
from products.models import Product, Category
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class CategoryAPI(ListCreateAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class CategoryIndividualAPI(RetrieveUpdateDestroyAPIView):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    lookup_field='slug'

class ProductAPI(ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class ProductIndividualAPI(RetrieveUpdateDestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='slug'