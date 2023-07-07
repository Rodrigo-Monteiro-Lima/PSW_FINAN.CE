from django.urls import path
from . import views

urlpatterns = [
    path("definir_contas/", views.define_bills, name="definir_contas"),
    path("ver_contas/", views.show_bills, name="ver_contas"),
]
