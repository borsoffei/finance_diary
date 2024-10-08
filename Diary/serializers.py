from rest_framework import serializers
from .models import Transaction, Category

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'transaction_type', 'amount', 'description', 'date', 'created_at', 'category']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'user', 'name', 'is_default']

class TotalSumSerializer(serializers.Serializer):
    total_sum = serializers.DecimalField(max_digits=15, decimal_places=2)