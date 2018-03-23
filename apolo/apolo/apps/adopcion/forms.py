from django import forms
import datetime
from apps.adopcion.models import Persona

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = [
            'username',
            'password',
            'email',
            'first_name',
            'last_name',
            'tipo',
            'activos',
            'numeroEmpl',
            'date_joined',
            'is_active',
            'is_staff',
            'is_superuser',
            'last_login',
        ]
        labels = {
            'username':'Nombre de usuario',
            'password': 'Contraseña',
            'email': 'Correo Electronico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'tipo': 'Razon social de la empresa',
            'activos': 'Valor de activos en millones por año',
            'numeroEmpl': 'Numero de empleados',
        }
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'tipo': forms.TextInput(attrs={'class':'form-control'}),
            'activos': forms.NumberInput(attrs={'class':'form-control'}),
            'numeroEmpl': forms.NumberInput(attrs={'class':'form-control'}),
            'date_joined': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
            'is_active': forms.HiddenInput(attrs={'value':True}),
            'is_staff': forms.HiddenInput(attrs={'value':False}),
            'is_superuser': forms.HiddenInput(attrs={'value':False}),
            'last_login': forms.HiddenInput(attrs={'value':datetime.datetime.now()}),
        }
