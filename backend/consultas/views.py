from django.http import JsonResponse

from .models import Consulta


def listar_consultas(request):
    consultas = Consulta.objects.select_related('paciente', 'medico').all()
    dados = [
        {
            'id': consulta.id,
            'paciente': consulta.paciente.nome,
            'medico': consulta.medico.nome,
            'especialidade': consulta.medico.especialidade,
            'data_hora': consulta.data_hora,
            'observacoes': consulta.observacoes,
            'realizada': consulta.realizada,
        }
        for consulta in consultas
    ]
    return JsonResponse(dados, safe=False)
