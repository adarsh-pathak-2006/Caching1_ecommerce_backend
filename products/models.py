from django.db import models

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

class Product(models.Model):
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=50)
    slug=models.SlugField()
    description=models.TextField()
    price=models.PositiveIntegerField()
    stock=models.PositiveIntegerField()
    image=models.ImageField(upload_to='product_images/', blank=True, null=True)
    brand=models.CharField(max_length=50)
    sku=models.CharField(max_length=50)
    is_avaliable=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.stock == 0:
            self.is_avaliable = False
        else:
            self.is_avaliable = True
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
