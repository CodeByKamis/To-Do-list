from django.db import models

class Tarefas(models.Model):
 tarefa = models.CharField(max_length=255)
 status = models.BooleanField(default=False)

 def __str__(self):
    return self.tarefa
# Create your models here.
