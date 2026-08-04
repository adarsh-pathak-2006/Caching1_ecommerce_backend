from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from accounts.models import Profile
from django.contrib.auth import get_user_model
from accounts.serializers import RegisterUSerSerializer, ProfileUpdateSerializer, ProfileGetSerializer
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.permissions import IsAuthenticated
from e_commerce.permissions import IsAdmin
from e_commerce.throttle import RegisterThrottle, TokenObtainThrottle, TokenRefreshThrottle, GeneralAPIsThrottle

User=get_user_model()

class CustomTokenObtainAPI(TokenObtainPairView):
    throttle_classes=[TokenObtainThrottle]

class CustomTokenRefreshAPI(TokenRefreshView):
    throttle_classes=[TokenRefreshThrottle]

class RegisterAPI(APIView):
    throttle_classes=[RegisterThrottle]
    def post(self, request):
        serial=RegisterUSerSerializer(data=request.data)
        if serial.is_valid():
            f_name=serial.validated_data.get('first_name', '')
            l_name=serial.validated_data.get('last_name', '')
            username=serial.validated_data['username']
            email=serial.validated_data['email']
            mobile_no=serial.validated_data['phone_number']
            password=serial.validated_data['password']
            role=serial.validated_data['role']

            from django.db import IntegrityError
            try:
                user_created=User.objects.create_user(first_name=f_name, last_name=l_name, username=username, email=email, phone_number=mobile_no, password=password, role=role)
                Profile.objects.create(user=user_created)
                return Response({ 'message':'user registered successfully' }, status=201)
            except IntegrityError:
                return Response({ 'message':'credentials for the user already exists' }, status=400)
        else:
            return Response(serial.errors, status=400)

class MyProfileAPI(APIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        profile_data=get_object_or_404(Profile, user=request.user)
        serial=ProfileUpdateSerializer(profile_data)
        return Response(serial.data, status=200)

    def patch(self, request):
        profile_data=get_object_or_404(Profile, user=request.user)
        serial=ProfileUpdateSerializer(profile_data, data=request.data, partial=True)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status=200)
        else:
            return Response(serial.errors, status=400)     

class AllProfiles(ListAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAuthenticated]
    queryset=Profile.objects.all()
    serializer_class=ProfileGetSerializer

class AllProfileIndividual(RetrieveUpdateDestroyAPIView):
    throttle_classes=[GeneralAPIsThrottle]
    permission_classes=[IsAdmin]
    queryset=Profile.objects.all()
    serializer_class=ProfileUpdateSerializer

