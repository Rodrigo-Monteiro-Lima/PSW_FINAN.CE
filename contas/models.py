from django.db import models

from perfil.models import Category

# Create your models here.


class BillToPay(models.Model):
    title = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    description = models.TextField()
    value = models.FloatField()
    payment_day = models.IntegerField()

    def __str__(self):
        return self.title


class PaidBill(models.Model):
    Account = models.ForeignKey(BillToPay, on_delete=models.DO_NOTHING)
    payment_date = models.DateField()
