from django.urls import path
from e_commerce.consumers import NotificationConsumer

websocket_urlpatterns=[
    path('ws/nc/', NotificationConsumer.as_asgi(), name='notification_websocket'),
]