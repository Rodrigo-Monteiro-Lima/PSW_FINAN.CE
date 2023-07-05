from django.shortcuts import render

# Create your views here.


def new_value(request):
    if request.method == "GET":
        contas = Conta.objects.all()
        categorias = Categoria.objects.all()
        return render(
            request, "novo_valor.html", {"contas": contas, "categorias": categorias}
        )
