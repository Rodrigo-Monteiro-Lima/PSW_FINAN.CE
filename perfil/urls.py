from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("gerenciar/", views.manage, name="gerenciar"),
    path("cadastrar_banco/", views.db_register, name="cadastrar_banco"),
    path("deletar_banco/<int:id>", views.db_delete, name="deletar_banco"),
    path("cadastrar_categoria/", views.category_register, name="cadastrar_categoria"),
    path("update_categoria/<int:id>", views.update_category, name="update_categoria"),
]
