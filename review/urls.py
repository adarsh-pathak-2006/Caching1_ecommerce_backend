from django.urls import path
from review.views import ReviewAPI, ReviewIndividualAPI 

urlpatterns = [
    path('review/', ReviewAPI.as_view(), name='review'),
    path('review/<int:pk>/', ReviewIndividualAPI.as_view(), name='review_individual'),
]
