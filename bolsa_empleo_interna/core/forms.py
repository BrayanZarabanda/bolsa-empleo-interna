from django import forms
from .models import Usuario, Vacante

class RegistroUsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)

    class Meta:
        model = Usuario:
        fields = ['first_name', 'last_name', 'telefono', 'documento', 'email', 'rol', 'password']
        labels = {
            'first_name': 'Nombre',
            'last_name': 'Apellido',
        }

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        return cd['password2']

class LoginForm(forms.Form):
    documento = forms.CharField(label='Documento', max_length=20)
    password = forms.CharField(widget=forms.PasswordInput)
    labels = {
        'password': 'Contraseña',
    }

class VacanteForm(forms.ModelForm):
    class Meta:
        model = Vacante
        fields = ['nombre_vacante', 'descripcion']
        labels = {
            'nombre_vacante': 'Nombre de la Vacante',
            'descripcion': 'Descripción',
        }
