from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'transaction_type', 'amount', 'date', 'created_at')
    search_fields = ('user__username', 'transaction_type', 'description')
    list_filter = ('transaction_type', 'date')
    ordering = ('-date',)