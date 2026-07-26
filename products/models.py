from django.db import models
from django.conf import settings

User=settings.AUTH_USER_MODEL

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField()
    description=models.TextField()
    image=models.ImageField(upload_to='category_images/', blank=True, null=True)
    is_active=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name