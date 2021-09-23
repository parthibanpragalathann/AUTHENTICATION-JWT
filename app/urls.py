from django.urls import path
from .views import RegisterView, LoginView, PasswordView, UpdateProfileView
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    path('login/', LoginView.as_view(), name='auth_login'),
    path('refresh/', TokenRefreshView.as_view(), name='auth_refresh'),
    path('password/<int:pk>/', PasswordView.as_view(), name='auth_change_password'),
    path('profile/<int:pk>/', UpdateProfileView.as_view(), name='auth_update_profile'),
]
