from django import forms
from .models import Sede


class SedeForm(forms.ModelForm):
    class Meta:
        model = Sede
        fields = ('nombre', 'ciudad')