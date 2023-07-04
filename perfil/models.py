from django.db import models

# Create your models here.


class Category(models.Model):
    category = models.CharField(max_length=50)
    essential = models.BooleanField(default=False)
    planning_value = models.FloatField(default=0)

    def __str__(self):
        return self.category


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
