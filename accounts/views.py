from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .serializers import UserSerializer, RegisterSerializer

# Регистрация нового пользователя
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

# Получение данных текущего пользователя
class UserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user


