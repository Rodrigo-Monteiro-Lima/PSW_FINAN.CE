from datetime import datetime, timedelta
from io import BytesIO
import os
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import redirect, render
from extrato.models import Values
from perfil.models import Account, Category
from django.contrib import messages
from django.contrib.messages import constants
from django.template.loader import render_to_string
from weasyprint import HTML

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


def view_statement(request):
    accounts = Account.objects.all()
    categories = Category.objects.all()
    account_filter = request.GET.get("account")
    category_filter = request.GET.get("category")
    period_filter = request.GET.get("period")
    values = Values.objects.filter(date__month=datetime.now().month)
    print(period_filter)
    if account_filter:
        values = values.filter(account_id=account_filter)
    if category_filter:
        values = values.filter(category_id=category_filter)
    if period_filter:
        date = datetime.now().date()
        days_ago = date - timedelta(days=int(period_filter))
        values = values.filter(date__range=(days_ago, date))

    return render(
        request,
        "view_extrato.html",
        {"values": values, "accounts": accounts, "categories": categories},
    )


def export_pdf(request):
    values = Values.objects.filter(date__month=datetime.now().month)
    accounts = Account.objects.all()
    categories = Category.objects.all()

    path_template = os.path.join(settings.BASE_DIR, "templates/partials/extrato.html")
    path_output = BytesIO()

    template_render = render_to_string(
        path_template,
        {"values": values, "accounts": accounts, "categories": categories},
    )
    HTML(string=template_render).write_pdf(path_output)

    path_output.seek(0)

    return FileResponse(path_output, filename="extrato.pdf")
