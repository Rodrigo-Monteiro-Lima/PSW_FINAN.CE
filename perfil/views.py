from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants

from extrato.models import Values
from .models import Account, Category
from .utils import sum_total_value

# Create your views here.


def home(request):
    accounts = Account.objects.all()
    total_value = sum_total_value(accounts, "value")
    context = {
        "accounts": accounts,
        "total_value": total_value,
    }
    return render(request, "home.html", context)


def manage(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    total_value = sum_total_value(accounts, "value")
    context = {
        "accounts": accounts,
        "total_value": total_value,
        "categories": categories,
    }
    return render(request, "gerenciar.html", context)


def db_register(request):
    nickname = request.POST.get("nickname")
    bank = request.POST.get("bank")
    account_type = request.POST.get("type")
    value = request.POST.get("value")
    icon = request.FILES.get("icon")

    banks = {"NU", "CE"}
    account_types = {"pf", "pj"}

    if bank is None or bank not in banks:
        messages.add_message(request, constants.ERROR, "Banco inválido!")
        return redirect("/perfil/gerenciar/")

    if account_type is None or account_type not in account_types:
        messages.add_message(request, constants.ERROR, "Tipo de conta inválido!")
        return redirect("/perfil/gerenciar/")

    if icon is None:
        messages.add_message(
            request, constants.ERROR, "Não é possível cadastrar uma conta sem um ícone!"
        )
        return redirect("/perfil/gerenciar/")

    if len(nickname.strip()) == 0 or len(value.strip()) == 0:
        messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
        return redirect("/perfil/gerenciar/")

    account = Account(
        nickname=nickname, bank=bank, type=account_type, value=value, icon=icon
    )

    account.save()

    messages.add_message(request, constants.SUCCESS, "Conta cadastrada com sucesso!")

    return redirect("/perfil/gerenciar/")


def db_delete(request, id):
    account = Account.objects.get(id=id)
    account.delete()

    messages.add_message(request, constants.SUCCESS, "Conta removida com sucesso")
    return redirect("/perfil/gerenciar/")


def category_register(request):
    category_name = request.POST.get("category")
    essential = bool(request.POST.get("essential"))

    if len(category_name.strip()) == 0 or not isinstance(essential, bool):
        messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
        return redirect("/perfil/gerenciar/")

    category = Category(category=category_name, essential=essential)

    category.save()

    messages.add_message(request, constants.SUCCESS, "Categoria cadastrada com sucesso")
    return redirect("/perfil/gerenciar/")


def update_category(request, id):
    category = Category.objects.get(id=id)

    category.essential = not category.essential

    category.save()

    return redirect("/perfil/gerenciar/")


def dashboard(request):
    data = {}
    categories = Category.objects.all()

    for category in categories:
        total = 0
        values = Values.objects.filter(category=category)
        for value in values:
            total = total + value.value

        data[category.category] = total

    return render(
        request,
        "dashboard.html",
        {"labels": list(data.keys()), "values": list(data.values())},
    )
