from django.db import models
from datetime import datetime

# Create your models here.
class Expense (models.Model):
    date_added = models.DateField(default=datetime.now)
    description = models.TextField()
    amount = models.FloatField()
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('transport', 'Transport'),
        ('utilities', 'Utilities'),
        ('entertainment', 'Entertainment'),
    ]
    category = models.CharField(max_length=20, choices= CATEGORY_CHOICES, blank=True, default='others')
    
    def __str__(self):
        return f'{self.description}'
    
    class Meta:
        verbose_name_plural = 'Expenses'