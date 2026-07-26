from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICE=[
        ('CUSTOMER', 'Customer'),
        ('ADMIN', 'Admin')
    ]
    role=models.CharField(max_length=8, choices=ROLE_CHOICE)
    phone_number=models.CharField(max_length=15)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo=models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    gender=models.CharField(max_length=6, choices=[('MALE', 'Male'), ('FEMALE', 'Female')])
    address=models.TextField()
    city=models.CharField(max_length=20)
    state=models.CharField(max_length=20)
    postal_code=models.CharField(max_length=6)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.user.username

