from django.db import models

class Escola(models.Model):
    nome = models.CharField(max_length=255)
    bairro = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class KitEscolar(models.Model):
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    quantidade_alunos_1_ao_5_ano = models.IntegerField(default=0)

    def __str__(self):
        return f"Kit da Escola: {self.escola.nome}"