

from django.urls import path
from . import views
urlpatterns = [
    path("", views.index,name='index'),
    path("nome", views.meu_nome,name='nome'),
    path("tabuada2/", views.tabuada2,name='tabuada2'),
    path("calcular/", views.calcular_imc,name='calcular_imc')
]