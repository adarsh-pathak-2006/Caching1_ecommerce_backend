from django.db import models
from products.models import Product
from accounts.models import Profile


class Order(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    orderId=models.CharField(max_length=50)
    tax=models.PositiveIntegerField()
    shipping_charges=models.PositiveIntegerField()
    final_amount=models.PositiveIntegerField()
    payment_method=models.CharField(max_length=15, choices=[('CARD', 'Card'), ('CASH ON DELIVERY', 'Cash on Delivery'), ('UPI', 'UPI')])
    order_status=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField()

    def __str__(self):
        return self.user.user.username

class OrderItem(models.Model):
    order=models.ForeignKey(Order, on_delete=models.CASCADE)
    item=models.ForeignKey(Product, on_delete=models.CASCADE)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()
    sub_total=models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        self.sub_total = self.price + self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order.orderId