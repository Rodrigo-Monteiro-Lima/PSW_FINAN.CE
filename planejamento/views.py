from django.shortcuts import render
from perfil.models import Category
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from perfil.utils import sum_total_value
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
    total_spent = 0
    for category in categories:
        total_spent += category.total_spent()
    total_planned = sum_total_value(categories, "planning_value")
    percentage_spent = int((total_spent * 100) / total_planned)
    return render(
        request,
        "ver_planejamento.html",
        {
            "categories": categories,
            "total_spent": total_spent,
            "total_planned": total_planned,
            "percentage_spent": percentage_spent,
        },
    )


def define_planning(request):
    categories = Category.objects.all()
    return render(request, "definir_planejamento.html", {"categories": categories})
