from datetime import datetime
from django.shortcuts import redirect, render
from extrato.models import Values
from perfil.models import Account, Category
from django.contrib import messages
from django.contrib.messages import constants

# Create your views here.


def new_value(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()
        return render(
            request, "novo_valor.html", {"accounts": accounts, "categories": categories}
        )
    elif request.method == "POST":
        value = request.POST.get("value")
        category_id = request.POST.get("category")
        description = request.POST.get("description")
        date = request.POST.get("date")
        account_id = request.POST.get("account")
        value_type = request.POST.get("value_type")

        values = Values(
            value=value,
            category_id=category_id,
            description=description,
            date=date,
            account_id=account_id,
            value_type=value_type,
        )

        values.save()

        account = Account.objects.get(id=account_id)

        if value_type == "I":
            account.value += int(value)
        else:
            account.value -= int(value)

        account.save()

        if value_type == "I":
            messages.add_message(
                request, constants.SUCCESS, "Entrada adicionada com sucesso"
            )
        else:
            messages.add_message(
                request, constants.SUCCESS, "Saída adicionada com sucesso"
            )
        return redirect("/extrato/novo_valor")


def views_statement(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()

    values = Values.objects.filter(date__month=datetime.now().month)

    return render(
        request,
        "view_extrato.html",
        {"values": values, "accounts": accounts, "categories": categories},
    )
