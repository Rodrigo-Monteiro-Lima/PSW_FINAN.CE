from django.urls import path
from . import views

urlpatterns = [
    path("definir_contas/", views.define_bills, name="definir_contas"),
    path("ver_contas/", views.show_bills, name="ver_contas"),
    path(
        "update_conta_paga/<int:id>",
        views.paid_bill,
        name="update_conta_paga",
    ),
]
