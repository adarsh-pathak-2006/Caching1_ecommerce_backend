from django.urls import path 
from orders.views import MyOrderAPI, OrderCreationAPI, MyOrderAPIIndividual, AllOrdersAPI, AllOrderAPIIndividual

urlpatterns = [
    path('my-order/', MyOrderAPI.as_view(), name='my_order'),
    path('order-create/', OrderCreationAPI.as_view(), name='order_create'),
    path('my-order/<int:pk>/', MyOrderAPIIndividual.as_view(), name='myorder_individual'),
    path('orders/', AllOrdersAPI.as_view(), name='all_order'),
    path('orders/<int:pk>/', AllOrderAPIIndividual.as_view(), name='all_order_individual'),
]
