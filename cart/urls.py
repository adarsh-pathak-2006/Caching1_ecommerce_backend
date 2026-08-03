from django.urls import path
from cart.views import CartAPI, CartItemAPI

urlpatterns = [
    path('cart/', CartAPI.as_view(), name='cart'),
    path('cart/<int:pk>/', CartItemAPI.as_view(), name='cartitem_individual'),
]
