from django.shortcuts import render

from perfil.models import Account, Category

# Create your views here.


def new_value(request):
    if request.method == "GET":
        accounts = Account.objects.all()
        categories = Category.objects.all()
        return render(
            request, "novo_valor.html", {"accounts": accounts, "categories": categories}
        )
