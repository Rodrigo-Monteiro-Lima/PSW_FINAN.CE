from django.urls import path
from . import views

urlpatterns = [
    path("definir_contas/", views.define_accounts, name="definir_contas"),
]
