from django.urls import path

from . import views

urlpatterns = [
    path('consultas/', views.listar_consultas, name='listar_consultas'),
]
