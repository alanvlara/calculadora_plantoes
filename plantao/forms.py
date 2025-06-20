from django import forms
from .models import Plantao

class PlantaoForm(forms.ModelForm):
    class Meta:
        model = Plantao
        fields = ['data', 'hora_inicio', 'hora_fim', 'nome_medico']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fim': forms.TimeInput(attrs={'type': 'time'}),
            'nome_medico': forms.TextInput(attrs={'placeholder': 'Nome do médico'}),
        }
