from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.lista_tarefas, name='lista_tarefas'),
]
