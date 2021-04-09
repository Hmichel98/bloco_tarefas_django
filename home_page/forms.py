from django import forms 

from .models import Itens 


class ItensForm(forms.ModelForm):

    class Meta:
        model = Itens 
        fields = ["tarefa"]
        labels = {"tarefa": ""}