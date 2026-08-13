from django.shortcuts import render


def inicio(request):
    return render(request, 'index.html')


def produtos(request):
    return render(request, 'produtos.html')


def categorias(request):
    return render(request, 'categorias.html')


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')