from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # Связь с пользователем
    is_default = models.BooleanField(default=False)

    def __str__(self):
        return self.name



class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('income', 'Income'),
        ('expense', 'Expense'),
    ]
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)  # Связь с категорией
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'transaction'

    def __str__(self):
        return f"{self.get_transaction_type_display()} of {self.amount} on {self.date}"
