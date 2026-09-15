from django.db import models

from medicos.models import Medico
from pacientes.models import Paciente


class Consulta(models.Model):
    
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas')
    data_hora = models.DateTimeField()
    observacoes = models.TextField(blank=True)
    realizada = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.paciente} com {self.medico} em {self.data_hora}"
