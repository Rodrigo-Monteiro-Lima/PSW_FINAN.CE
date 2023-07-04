from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.messages import constants
from .models import Account

# Create your views here.


def home(request):
    return render(request, "home.html")


def manage(request):
    accounts = Account.objects.all()
    total_value = 0
    for account in accounts:
        total_value += account.value
    context = {"accounts": accounts, "total_value": total_value}
    return render(request, "gerenciar.html", context)


def db_register(request):
    nickname = request.POST.get("nickname")
    bank = request.POST.get("bank")
    type = request.POST.get("type")
    value = request.POST.get("value")
    icon = request.FILES.get("icon")

    if icon is None:
        messages.add_message(
            request, constants.ERROR, "Não é possível cadastrar uma conta sem um ícone!"
        )
        return redirect("/perfil/gerenciar/")

    if len(nickname.strip()) == 0 or len(value.strip()) == 0:
        messages.add_message(request, constants.ERROR, "Preencha todos os campos!")
        return redirect("/perfil/gerenciar/")

    account = Account(nickname=nickname, bank=bank, type=type, value=value, icon=icon)

    account.save()

    messages.add_message(request, constants.SUCCESS, "Conta cadastrada com sucesso!")

    return redirect("/perfil/gerenciar/")


def db_delete(request, id):
    account = Account.objects.get(id=id)
    account.delete()

    messages.add_message(request, constants.SUCCESS, "Conta removida com sucesso")
    return redirect("/perfil/gerenciar/")
