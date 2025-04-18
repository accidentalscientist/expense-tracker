# Generated by Django 5.0.7 on 2025-04-08 03:52

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_alter_expense_options_expense_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(blank=True, choices=[('food', 'Food'), ('transport', 'Transport'), ('utilities', 'Utilities'), ('entertainment', 'Entertainment'), ('others', 'Others')], default='others', max_length=20),
        ),
        migrations.AlterField(
            model_name='expense',
            name='date_added',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
