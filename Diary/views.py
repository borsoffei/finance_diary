from .models import Transaction, Category
from rest_framework import viewsets
from .serializers import TransactionSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем предопределенные и пользовательские категории
        return Category.objects.filter(Q(user=self.request.user) | Q(is_default=True))

    def perform_create(self, serializer):
        # Сохраняем категорию с текущим пользователем
        serializer.save(user=self.request.user)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]  # Только аутентифицированные пользователи

    def get_queryset(self):
        # Показывать только транзакции текущего пользователя
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Установить пользователя для создаваемой транзакции
        serializer.save(user=self.request.user)
