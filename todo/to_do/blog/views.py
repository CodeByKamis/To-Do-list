from django.shortcuts import render
from .models import Tarefas
def lista_tarefas(request):
 tarefas = Tarefas.objects.all()
 return render(request, 'blog/to_do.html', {'tarefas': tarefas})
