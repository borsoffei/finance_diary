from .models import Transaction
from rest_framework import viewsets
from .serializers import TransactionSerializer
from rest_framework.permissions import IsAuthenticated

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
