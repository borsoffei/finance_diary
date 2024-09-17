from django_filters import rest_framework as filters
from .models import Transaction, Category

class TransactionFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name='date', lookup_expr='gte')
    end_date = filters.DateFilter(field_name='date', lookup_expr='lte')
    category = filters.ModelChoiceFilter(queryset=Category.objects.all())

    class Meta:
        model = Transaction
        fields = ['transaction_type', 'category', 'start_date', 'end_date']
