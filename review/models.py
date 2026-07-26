from django.db import models
from products.models import Product
from accounts.models import Profile

class Review(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    rating=models.CharField(max_length=6, choices=[('1 STAR', '1 Star'), ('2 STAR', '2 Star'), ('3 STAR', '3 Star'), ('4 STAR', '4 Star'), ('5 STAR', '5 Star')])
    review=models.CharField(max_length=500, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
