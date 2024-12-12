from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(unique=True, max_length=254)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
