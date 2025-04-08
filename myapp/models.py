from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Expense (models.Model):
    date_added = models.DateField(default=timezone.now)
    name = models.CharField(max_length=20,)
    description = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
        ('others', 'Others'),  # ✅ add this
    ]
    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, blank=True, default='others')
    
    def __str__(self):
        return f'{self.name} - {self.amount} - {self.description}'
    
    class Meta:
        verbose_name_plural = 'Expenses'
        ordering = ['-date_added']