from django.contrib import admin
from .models import BillToPay, PaidBill

# Register your models here.

admin.site.register(BillToPay)
admin.site.register(PaidBill)
