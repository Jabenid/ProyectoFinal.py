from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class JuegoFormulario(forms.Form):

    nombre = forms.CharField()
    fechaCreacion = forms.DateField()
    distribuidor = forms.CharField()
    desarrolladora = forms.CharField()
    plataforma = forms.CharField()
    puntaje = forms.IntegerField()
    genero = forms.CharField()
    subGenero = forms.CharField()

    
class ProblemaFormulario(forms.Form):

    detalles = forms.CharField()
    fechaError = forms.DateField()
    juego = forms.CharField()
    plataforma = forms.CharField()


class UsuarioFormulario(forms.Form):

    fechaNacimiento = forms.DateField()
    nombre = forms.CharField()
    apellido = forms.CharField()
    IdJugador = forms.CharField()
    celular = forms.IntegerField()
    pais = forms.CharField()
    provincia = forms.CharField()
    email = forms.EmailField()
    juego = forms.CharField()   



class UsuarioRegistro(UserCreationForm):

    email = forms.EmailField()

    nombre = forms.CharField()

    apellido = forms.CharField()

    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)

    password2 = forms.CharField(label="Repetir la Contraseña", widget= forms.PasswordInput)

    class Meta :


        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]




class FormularioEditar(UserCreationForm):
    
    email = forms.EmailField()

    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)

    password2 = forms.CharField(label="Repetir la Contraseña", widget= forms.PasswordInput)

    class Meta :


        model = User
        fields = ["email","first_name","last_name","password1","password2"]


