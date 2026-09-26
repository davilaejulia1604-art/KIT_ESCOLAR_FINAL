from django import forms
from .models import Escola, KitEscolar

class EscolaForm(forms.ModelForm):
    class Meta:
        model = Escola
        fields = ['nome', 'bairro']

class KitEscolarForm(forms.ModelForm):
    class Meta:
        model = KitEscolar
        fields = ['escola', 'quantidade_alunos_1_ao_5_ano']