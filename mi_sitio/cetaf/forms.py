from django import forms
from .models import Sede, Ambiente, Categoria, Activo, Asignacion
from django.contrib.auth.models import User


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

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = User
        fields = {
            'last_login',
            'is_superuser',
            'groups',
            'user_permissions',
            'username',
            'first_name',
            'last_name',
            'email',
            'is_staff',
            'is_active',
            'date_joined',
        }
        widgets = {
            'password': forms.TextInput(attrs={'class': 'uk-input', 'type': 'text'}),
            'last_login': forms.DateInput(attrs={'class': 'uk-input', 'type': 'date', 'readonly': 'true'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'uk-checkbox'}),
            'groups': forms.Select(attrs={'class': 'uk-select', 'multiple': 'true'}),
            'user_permissions': forms.Select(attrs={'class': 'uk-select', 'multiple': 'true'}),
            'username': forms.TextInput(attrs={'class': 'uk-input'}),
            'first_name': forms.TextInput(attrs={'class': 'uk-input'}),
            'last_name': forms.TextInput(attrs={'class': 'uk-input'}),
            'email': forms.TextInput(attrs={'class': 'uk-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'uk-checkbox'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'uk-checkbox'}),
            'date_joined': forms.DateInput(attrs={'class': 'uk-input', 'type': 'date', 'readonly': 'true'}),
        }
        labels = {
            'password': ('Contraseña:'),
            'last_login': ('Ultima conexion:'),
            'is_superuser': ('Es superusuario:'),
            'groups': ('Grupos:'),
            'user_permissions': ('Permisos:'),
            'username': ('Nombre de usuario:'),
            'first_name': ('Nombres:'),
            'last_name': ('Apellidos'),
            'email': ('Email:'),
            'is_staff': ('Es administrador:'),
            'is_active': ('Cuenta activa:'),
            'date_joined': ('Fecha de creacion'),
        }
        help_texts = {
            'password': 'Las contraseñas sin procesar no se almacenan, por lo que no hay forma de ver la contraseña de este usuario, pero puede cambiar la contraseña.',
            'is_superuser': 'Designa que este usuario tiene todos los permisos sin asignarlos explícitamente.',
            'groups': 'Los grupos a los que pertenece este usuario. Un usuario obtendrá todos los permisos otorgados a cada uno de sus grupos [El o los grupos a los cuales pertece apareceran seleccionados].',
            'user_permissions': 'Permisos específicos para este usuario [El o los permisos a los cuales tiene acceso apareceran seleccionados].',
            'username': 'Requerido. 150 caracteres o menos. Letras, dígitos y @ /. / + / - / _ .',
            'is_staff': 'Designa si el usuario puede iniciar sesión en este sitio de administración.',
            'is_active': 'Designa si este usuario debe tratarse como activo. Anule la selección de esto en lugar de eliminar cuentas.',
        }