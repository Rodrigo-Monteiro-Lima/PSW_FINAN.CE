from django.shortcuts import redirect, render
from .models import Account

# Create your views here.


def home(request):
    return render(request, "home.html")


def manage(request):
    return render(request, "gerenciar.html")


def db_register(request):
    nickname = request.POST.get("nickname")
    bank = request.POST.get("bank")
    type = request.POST.get("type")
    value = request.POST.get("value")
    icon = request.FILES.get("icon")

    if len(nickname.strip()) == 0 or len(value.strip()) == 0:
        return redirect("/perfil/gerenciar/")

    account = Account(nickname=nickname, bank=bank, type=type, value=value, icon=icon)

    account.save()

    return redirect("/perfil/gerenciar/")
