from rest_framework.serializers import ModelSerializer
from products.serializers import ProductGetSerializer
from review.models import Review
from accounts.serializers import ProfileGetSerializer

class ReviewSerializer(ModelSerializer):
    product=ProductGetSerializer(read_only=True)
    user=ProfileGetSerializer(read_only=True)
    class Meta:
        model=Review
        fields='__all__'