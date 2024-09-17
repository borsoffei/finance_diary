from django_filters.rest_framework import DjangoFilterBackend
from .models import Transaction, Category
from rest_framework import viewsets
from .serializers import TransactionSerializer, CategorySerializer
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .filters import TransactionFilter
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from .serializers import TotalSumSerializer

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
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TransactionFilter

    def get_queryset(self):
        # Показываем только транзакции текущего пользователя
        return Transaction.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Устанавливаем пользователя для создаваемой транзакции
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], serializer_class=TotalSumSerializer)
    def total_sum(self, request):
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')
        category_id = request.query_params.get('category_id')

        transactions = self.get_queryset()
        if start_date and end_date:
            transactions = transactions.filter(date__gte=start_date, date__lte=end_date)
        if category_id:
            transactions = transactions.filter(category_id=category_id)

        total_sum = transactions.aggregate(Sum('amount'))['amount__sum'] or 0
        serializer = self.get_serializer({'total_sum': total_sum})
        return Response(serializer.data)