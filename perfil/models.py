from datetime import datetime
from django.db import models
from .utils import sum_total_value

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_value = models.FloatField(default=0)

    def __str__(self):
        return self.category

    def total_spent(self):
        from extrato.models import Values

        values = (
            Values.objects.filter(category__id=self.id)
            .filter(date__month=datetime.now().month)
            .filter(value_type="O")
        )
        total_value = sum_total_value(values, "value")
        return total_value if total_value else 0

    def calculate_percentage_spent_by_category(self):
        return int((self.total_spent() * 100) / self.planning_value)


class Account(models.Model):
    bank_choices = (
        ("NU", "Nubank"),
        ("CE", "Caixa econômica"),
    )

    type_choices = (
        ("pf", "Pessoa física"),
        ("pj", "Pessoa jurídica"),
    )

    nickname = models.CharField(max_length=50)
    bank = models.CharField(max_length=2, choices=bank_choices)
    type = models.CharField(max_length=2, choices=type_choices)
    value = models.FloatField()
    icon = models.ImageField(upload_to="icons")

    def __str__(self):
        return self.nickname
