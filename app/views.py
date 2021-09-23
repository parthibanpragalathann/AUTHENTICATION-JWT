from django.contrib.auth.models import User
from .serializer import RegisterSerializer, LoginSerializer, PasswordSerializer, UpdateUserSerializer
from rest_framework import generics
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
CustomUser = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

class PasswordView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PasswordSerializer

class UpdateProfileView(generics.UpdateAPIView):

    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UpdateUserSerializer