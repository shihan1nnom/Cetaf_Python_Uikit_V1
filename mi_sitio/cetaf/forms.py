from django import forms
from .models import Sede, Ambiente, Categoria


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


class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'uk-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
        labels = {
            'nombre': ('Nombre del ambiente:'),
            'descripcion': ('Descripcion:'),
        }


class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'uk-input'}),
            'descripcion': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
        labels = {
            'nombre': ('Nombre de la categoria:'),
            'descripcion': ('Descripcion:'),
        }