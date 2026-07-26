from django.db import models
from accounts.models import Profile
from products.models import Product

class Cart(models.Model):
    profile=models.OneToOneField(Profile, on_delete=models.CASCADE)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.profile.user.username

class CartItem(models.Model):
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.PositiveIntegerField()
    total_price=models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.total_price = self.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.product.name
