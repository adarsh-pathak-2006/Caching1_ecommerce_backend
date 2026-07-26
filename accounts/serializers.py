from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from accounts.models import Profile

User=get_user_model()

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'phone_number', 'role']

class RegisterUSerSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=['first_name', 'last_name', 'username', 'email', 'phone_number', 'role', 'password']

class ProfileUpdateSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields=['user' ,'full_name' ,'profile_photo', 'gender', 'address', 'city', 'state', 'postal_code']

class ProfileGetSerializer(ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Profile
        fields=['user', 'full_name']
        read_only_fields=['full_name', 'user']