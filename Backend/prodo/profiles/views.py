from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import AppUser
from .serializers import UserCreateSerializer

class UserCreateView(generics.CreateAPIView):
    queryset = AppUser.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
