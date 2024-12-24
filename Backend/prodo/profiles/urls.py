from django.urls import path
from .views import UserCreateView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('token/', TokenObtainPairView.as_view(), name='user-login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh-token'),
]