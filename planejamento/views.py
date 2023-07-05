from django.shortcuts import render

from perfil.models import Category

# Create your views here.


def define_planning(request):
    categories = Category.objects.all()
    return render(request, "definir_planejamento.html", {"categories": categories})
