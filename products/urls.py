from django.urls import path
from products.views import CategoryAPI, CategoryIndividualAPI, ProductAPI, ProductIndividualAPI

urlpatterns = [
    path('category/', CategoryAPI.as_view(), name='category'),
    path('category/<slug:slug>/', CategoryIndividualAPI.as_view(), name='category_individual'),
    path('product/', ProductAPI.as_view(), name='product'),
    path('product/<slug:slug>/', ProductIndividualAPI.as_view(), name='product_individual'),    
]

