from django import forms
from .models import Sede


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'uk-input'}),
            'ciudad': forms.TextInput(attrs={'class': 'uk-input'}),
        }
        labels = {
            'nombre': ('Nombre de la sede:'),
            'ciudad': ('Ciudad:'),
        }