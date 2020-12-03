from django import forms
from .models import Sede, Ambiente, Categoria, Activo, Asignacion


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


class ActivoForm(forms.ModelForm):
    class Meta:
        model = Activo
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'uk-input'}),
            'categoria': forms.Select(attrs={'class': 'uk-select'}),
            'num_serie': forms.TextInput(attrs={'class': 'uk-input'}),
            'fecha_compra': forms.DateInput(attrs={'class': 'uk-input', 'placeholder': 'aaaa-mm-dd'}),
            'cobertura_seguro': forms.TextInput(attrs={'class': 'uk-input'}),
            'valor_compra': forms.NumberInput(attrs={'class': 'uk-input'}),
            'garantia': forms.TextInput(attrs={'class': 'uk-input'}),
            'fecha_puesto_servicio': forms.DateInput(attrs={'class': 'uk-input', 'placeholder': 'aaaa-mm-dd'}),
            'descripcion': forms.Textarea(attrs={'class': 'uk-textarea'}),
            'vida_util': forms.TextInput(attrs={'class': 'uk-input'}),
            'valor_residual': forms.NumberInput(attrs={'class': 'uk-input'}),
        }
        labels = {
            'nombre': ('Nombre del activo:'),
            'categoria': ('Categoria:'),
            'num_serie': ('Numero de serie:'),
            'fecha_compra': ('Fecha de compra:'),
            'cobertura_seguro': ('Cobertura de seguro:'),
            'valor_compra': ('Valor de compra:'),
            'garantia': ('Garantia:'),
            'fecha_puesto_servicio': ('Fecha puesto en servicio:'),
            'descripcion': ('Descripcion:'),
            'vida_util': ('Vida util:'),
            'valor_residual': ('Valor residual:'),
        }


class AsignacionForm(forms.ModelForm):
    class Meta:
        model = Asignacion
        fields = '__all__'
        widgets = {
            'nombre_activo': forms.Select(attrs={'class': 'uk-select'}),
            'persona_responsable': forms.TextInput(attrs={'class': 'uk-input'}),
            'sede_asignada': forms.Select(attrs={'class': 'uk-select'}),
            'ambiente_asignado': forms.Select(attrs={'class': 'uk-select'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'uk-input', 'placeholder': 'aaaa-mm-dd'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'uk-input', 'placeholder': 'aaaa-mm-dd'}),
            'descripcion': forms.Textarea(attrs={'class': 'uk-textarea'}),
        }
        labels = {
            'nombre_activo': ('Nombre del activo:'),
            'persona_responsable': ('Persona responsable:'),
            'sede_asignada': ('Sede asignada:'),
            'ambiente_asignado': ('Ambiente asignado:'),
            'fecha_inicio': ('Fecha de inicio:'),
            'fecha_fin': ('Fecha fin:'),
            'descripcion': ('Descripcion:'),
        }
