from django.urls import path
from . import views

urlpatterns = [
    path("novo_valor/", views.new_value, name="novo_valor"),
    path("view_extrato/", views.view_statement, name="view_extrato"),
]
