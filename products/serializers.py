from rest_framework.serializers import ModelSerializer
from products.models import Category, Product

class CategorySerializer(ModelSerializer):
    class Meta:
        model=Category
        fields=['name', 'slug', 'decription', 'image', 'is_active', 'created_at']

class ProductSerializer(ModelSerializer):
    category=CategorySerializer(read_only=True)
    class Meta:
        model=Product
        fields='__all__'
        read_only_fields=['is_avaliable']

class ProductGetSerializer(ModelSerializer):
    class Meta:
        model=Product
        fields=['name', 'description', 'price', 'stock', 'sku']