from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def cadastrarescola(request):
    return render(request, 'cadastrarescola.html')

def listarescola(request):
    return render(request, 'listarescola.html')