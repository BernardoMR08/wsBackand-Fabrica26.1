from django.db import models
from django.contrib.auth.models import User

class Carteira(models.Model):
    Usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits= 10, decimal_places= 2)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    Carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places= 2)
    data = models.DateTimeField(auto_now_add= True)
    descricao = models.CharField(max_Length= 255)   
    tipo = models.CharField(max_Length= 10, choices= [('entrada', 'Entrada'), ('saída', 'Saída')])

    def __str__(self):
        return f"{self.tipo} - {self.valor} - {self.descricao}"