from django.urls import path
from . import views

urlpatterns = [
    path("definir_planejamento/", views.define_planning, name="definir_planejamento"),
]
