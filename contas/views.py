from django.shortcuts import render

from perfil.models import Category

# Create your views here.


def define_accounts(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "definir_contas.html", {"categories": categories})
