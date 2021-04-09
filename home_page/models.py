from django.db import models





class Itens(models.Model):
    tarefa = models.CharField(max_length=20)


    def __str__(self):
        return self.tarefa

    class Meta:
        verbose_name_plural = "itens"