from django.contrib import admin

from .models import Consulta


@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ('id', 'paciente', 'medico', 'data_hora', 'realizada')
    list_filter = ('realizada', 'medico')
    search_fields = ('paciente__nome', 'medico__nome')
