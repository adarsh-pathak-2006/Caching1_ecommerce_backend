from django.db import models
from accounts.models import Profile
from cart.models import Cart


class Order(models.Model):
    user=models.ForeignKey(Profile, on_delete=models.CASCADE)
    cart=models.ForeignKey(Cart, on_delete=models.CASCADE)
    orderId=models.CharField(max_length=50)
    tax=models.PositiveIntegerField()
    shipping_charges=models.PositiveIntegerField()
    final_amount=models.PositiveIntegerField()
    payment_method=models.CharField(max_length=20, choices=[('CARD', 'Card'), ('CASH ON DELIVERY', 'Cash on Delivery'), ('UPI', 'UPI')])
    payment_status=models.CharField(max_length=10, choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed')], default='PENDING')
    order_status=models.CharField(max_length=50, choices=[('RECIEVED', 'Recieved'), ('OUT_FOR_DELIVERY', 'Out_for_delivery'), ('DELIVERED', 'Delivered'), ('CANCELED', 'Canceled')])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.user.username

# class OrderItem(models.Model):
#     order=models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
#     item=models.ForeignKey(Product, on_delete=models.CASCADE)
#     price=models.PositiveIntegerField()
#     quantity=models.PositiveIntegerField()
#     sub_total=models.PositiveIntegerField()

#     class Meta:
#         constraints=[models.UniqueConstraint(fields=['order', 'item'],name='unique_product_per_order_constraint')]

#     def save(self, *args, **kwargs):
#         self.sub_total = self.price * self.quantity
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return self.order.orderId