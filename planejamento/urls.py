from django.urls import path
from . import views

urlpatterns = [
    path("definir_planejamento/", views.define_planning, name="definir_planejamento"),
    path(
        "update_valor_categoria/<int:id>",
        views.update_category_value,
        name="update_valor_categoria",
    ),
    path("ver_planejamento/", views.show_planning, name="ver_planejamento"),
]
