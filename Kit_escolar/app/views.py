from django.shortcuts import render, redirect
from .forms import EscolaForm, KitEscolarForm
from .models import Escola, KitEscolar

def home(request):
    return render(request, 'home.html')

def cadastrarescola(request):
    if request.method == 'POST':
        form = EscolaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarescola')
    else:
        def cadastrarkit(request):
            if request.method == 'POST':
                form = KitEscolarForm(request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('listarescola')
            else:
                form = KitEscolarForm()
            return render(request, 'cadastrarkit.html', {'form': form})
        form = EscolaForm()
    return render(request, 'cadastrarescola.html', {'form': form})

def listarescola(request):
    escolas = Escola.objects.all()
    kits = KitEscolar.objects.all()
    return render(request, 'listarescola.html', {'escolas': escolas, 'kits': kits})


def cadastrarkit(request):
    if request.method == 'POST':
        form = KitEscolarForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarescola')
    else:
        form = KitEscolarForm()
    return render(request, 'cadastrarkit.html', {'form': form})

from django.shortcuts import get_object_or_404

def excluir_escola(request, id):
    escola = get_object_or_404(Escola, id=id)
    escola.delete()
    return redirect('listarescola')

def excluir_kit(request, id):
    kit = get_object_or_404(KitEscolar, id=id)
    kit.delete()
    return redirect('listarescola')

def editar_escola(request, id):
    escola = get_object_or_404(Escola, id=id)
    if request.method == 'POST':
        form = EscolaForm(request.POST, instance=escola) # O 'instance' avisa que estamos alterando uma que já existe
        if form.is_valid():
            form.save()
            return redirect('listarescola')
    else:
        form = EscolaForm(instance=escola)
    return render(request, 'cadastrarescola.html', {'form': form, 'titulo': 'Editar Escola'})

def editar_kit(request, id):
    kit = get_object_or_404(KitEscolar, id=id)
    if request.method == 'POST':
        form = KitEscolarForm(request.POST, instance=kit)
        if form.is_valid():
            form.save()
            return redirect('listarescola')
    else:
        form = KitEscolarForm(instance=kit)
    return render(request, 'cadastrarkit.html', {'form': form, 'titulo': 'Editar Kit Escolar'})