from django import forms
from .models import Tarefa

class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ('descricao', 'categoria')

class EditarTarefaForm(forms.Form):
    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Preciso ser feito'),
    )
    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(
        label="Categoria", 
        choices=OPCOES_CATEGORIA
    )