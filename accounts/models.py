from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICE=[
        ('CUSTOMER', 'Customer'),
        ('ADMIN', 'Admin')
    ]
    email = models.EmailField(unique=True)
    role=models.CharField(max_length=8, choices=ROLE_CHOICE)
    phone_number=models.CharField(max_length=15, unique=True)

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    full_name=models.CharField(max_length=50)
    profile_photo=models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    gender=models.CharField(max_length=6, choices=[('MALE', 'Male'), ('FEMALE', 'Female')], blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    city=models.CharField(max_length=20,blank=True, null=True)
    state=models.CharField(max_length=20, blank=True, null=True)
    postal_code=models.CharField(max_length=6, blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    def __str__(self):
        return self.full_name

