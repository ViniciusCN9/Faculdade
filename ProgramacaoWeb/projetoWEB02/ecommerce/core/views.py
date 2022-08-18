from django.shortcuts import render

def login(request):
    return render(request, 'login.html')

def registrar(request):
    return render(request, 'registrar.html')

def home(request):
    return render(request, 'home.html')

def produtos(request):
    return render(request, 'produtos.html')

def fornecedores(request):
    return render(request, 'fornecedores.html')

def sobre(request):
    return render(request, 'sobre.html')
