from datetime import datetime
from django.shortcuts import render, redirect

from perfil.models import Category
from django.contrib import messages
from django.contrib.messages import constants
from .models import BillToPay, PaidBill

# Create your views here.


def define_bills(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "definir_contas.html", {"categories": categories})
    else:
        title = request.POST.get("title")
        category = request.POST.get("category")
        description = request.POST.get("description")
        value = request.POST.get("value")
        payment_day = request.POST.get("payment_day")

        bill = BillToPay(
            title=title,
            category_id=category,
            description=description,
            value=value,
            payment_day=payment_day,
        )

        bill.save()

        messages.add_message(request, constants.SUCCESS, "Conta cadastrada com sucesso")
        return redirect("/contas/definir_contas")


def show_bills(request):
    CURRENT_MONTH = datetime.now().month
    CURRENT_DAY = datetime.now().day

    bills = BillToPay.objects.all()

    paid_bills = PaidBill.objects.filter(payment_date__month=CURRENT_MONTH).values(
        "account"
    )

    overdue_bills = bills.filter(payment_day__lt=CURRENT_DAY).exclude(id__in=paid_bills)

    bills_close_to_maturity = (
        bills.filter(payment_day__lte=CURRENT_DAY + 5)
        .filter(payment_day__gte=CURRENT_DAY)
        .exclude(id__in=paid_bills)
    )

    remaining = (
        bills.exclude(id__in=overdue_bills)
        .exclude(id__in=paid_bills)
        .exclude(id__in=bills_close_to_maturity)
    )

    return render(
        request,
        "ver_contas.html",
        {
            "overdue_bills": overdue_bills,
            "bills_close_to_maturity": bills_close_to_maturity,
            "remaining": remaining,
            "overdue_bills_count": overdue_bills.count(),
            "bills_close_to_maturity_count": bills_close_to_maturity.count(),
            "remaining_count": remaining.count(),
            "paid_bills_count": paid_bills.count(),
        },
    )
