from django.urls import path
from accounts.views import MyProfileAPI, AllProfiles, AllProfileIndividual

urlpatterns = [
    path('myprofile/', MyProfileAPI.as_view(), name='my_profile'),
    path('profile/', AllProfiles.as_view(), name='profileapi'),
    path('profile/<int:id>/', AllProfileIndividual.as_view(), name='profile_individual'),
]
