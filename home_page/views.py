from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.urls import reverse 

from .models import Itens 

from .forms import ItensForm 


def home_view(request):
    if request.method != "POST":
        form = ItensForm()
    else:
        form = ItensForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("home"))
    tarefas = Itens.objects.order_by("tarefa")
    return render(request, 'home_page/home.html', {"tarefas": tarefas, "form": form})


def delete_view(request, id_tarefa):
    tarefa = Itens.objects.filter(id=id_tarefa)
    tarefa.delete()
    return HttpResponseRedirect(reverse("home"))
