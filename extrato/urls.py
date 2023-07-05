from django.urls import path
from . import views

urlpatterns = [
    path("novo_valor/", views.new_value, name="novo_valor"),
]
