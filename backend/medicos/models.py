from django.db import models


class Medico(models.Model):
    nome = models.CharField(max_length=150)
    especialidade = models.CharField(max_length=100)
    crm = models.CharField(max_length=20, unique=True)
    anos_experiencia = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nome} ({self.especialidade})"
