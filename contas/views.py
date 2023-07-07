from django.shortcuts import render, redirect

from perfil.models import Category
from django.contrib import messages
from django.contrib.messages import constants
from .models import BillToPay

# Create your views here.


def define_accounts(request):
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
