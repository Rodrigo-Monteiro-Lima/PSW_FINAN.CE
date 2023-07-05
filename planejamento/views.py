from django.shortcuts import render
from perfil.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def update_category_value(request, id):
    new_value = json.load(request)["new_value"]
    category = Category.objects.get(id=id)
    category.planning_value = new_value
    category.save()

    return JsonResponse({"status": "Sucesso"})


def show_planning(request):
    categories = Category.objects.all()
    return render(request, "ver_planejamento.html", {"categories": categories})


def define_planning(request):
    categories = Category.objects.all()
    return render(request, "definir_planejamento.html", {"categories": categories})
