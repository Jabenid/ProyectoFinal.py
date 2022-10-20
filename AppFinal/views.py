from dataclasses import field
from msilib.schema import ListView
from sqlite3 import Cursor
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from AppFinal.forms import *
from AppFinal.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicioSesion(request):

    if request.method == "POST":
        form = AuthenticationForm(request,data = request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            
            contra = form.cleaned_data.get ("password")
            
            user = authenticate(username = usuario, password = contra )

            if user : 
                    login(request, user) 
                    return render (request,"AppFinal/inicio.html",{"mensaje":f"Bienvenido {user}"})
        
        else:
            return render(request, "AppFinal/inicio.html",{"mensaje":"Datos Incorrectos."} )

    else:
        form = AuthenticationForm()

    return render(request,"AppFinal/login.html",{"formulario":form} )


def registro(request):
    if request.method == "POST":
        form =  UsuarioRegistro(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "AppFinal/inicio.html",{"mensaje":"Usuario Creado."} )
    else:
        form = UsuarioRegistro()        

    return render ( request, "AppFinal/registro.html",{"formulario":form} )


def editarUsuario(request):
    usuario = request.user
    if request.method == "POST":
        form = FormularioEditar(request.POST)
        if form.is_valid():    
            info = form.cleaned_data
            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info["first_name"]
            usuario.last_name = info["last_name"]


            usuario.save()


        return render(request,"AppFinal/inicio.html")
    else:
        form = FormularioEditar(initial={
        "email":usuario.email,
        "first_name":usuario.first_name,
        "last_name":usuario.last_name,})
    return render(request, "AppFinal/editarPerfil.html",{"formulario":form,"usuario":usuario })   


def inicio(request):
    return render(request,"AppFinal/inicio.html")




    

def juego(request):

    juego1 = Juegos(nombre = "Grand Theft Auto V", fechaCreacion = "2013-09-17", distribuidor = "Rockstar", desarrolladora = "Rockstar", plataforma = "Consolas/PC", puntaje = 8, genero = "Acción aventura", subGenero = "Mundo abierto" )
    juego1.save()
    return render(request,"AppFinal/juegos.html")


def problema(request):

    problema1 = Problemas(detalles = "Error Grafico", fechaError = "2013-11-26", juego = "Grand Theft Auto V", plataforma = "Consolas" )
    problema1.save()
    return render(request,"AppFinal/problemas.html")

def usuario(request):
    
    usuario1 = Usuarios(fechaNacimiento ="2008-6-7", nombre="Jorge", apellido ="Messi", IdJugador ="jorMesii", celular ="1145783594", pais ="Argentina", provincia ="Cordoba", email ="jorgessi10@gmail.com", juego = "Grand Theft Auto V ")
    usuario1.save()
    return render(request,"AppFinal/usuarios.html")

def juegoFormulario(request):
    
    if request.method == "POST":

        formulario1 = JuegoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            juego = Juegos(nombre = info["nombre"], fechaCreacion = info["fechaCreacion"], distribuidor = info["distribuidor"], desarrolladora = info["desarrolladora"], plataforma = info["plataforma"], puntaje = info ["puntaje"], genero = info["genero"], subGenero = info["subGenero"] )

            juego.save()

            return render(request,"AppFinal/inicio.html")

    else:
        
        formulario1 = JuegoFormulario()
    
    return render(request,"AppFinal/juegoFormulario.html", {"form1":formulario1} )

def problemaFormulario(request):

    if request.method == "POST":
        
        formulario2 = ProblemaFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            problema = Problemas(detalles = info["detalles"], fechaError = info["fechaError"], juego = info["juego"], plataforma = info["plataforma"] )

            problema.save()

            return render(request,"AppFinal/inicio.html")

    else:

        formulario2 = ProblemaFormulario()

    return render(request,"AppFinal/problemaFormulario.html", {"form2":formulario2})

def usuarioFormulario(request):

    if request.method == "POST":
        
        formulario3 = UsuarioFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            usuario = Usuarios(fechaNacimiento = info["fechaNacimiento"], nombre= info["nombre"], apellido = info["apellido"], IdJugador = info["idJugador"], celular = info["celular"], pais = info["pais"], provincia = info["provincia"], email = info["email"], juego = info["juego"])

            usuario.save()

            return render(request,"AppFinal/inicio.html")

    else:

        formulario3 = UsuarioFormulario()

    return render(request,"AppFinal/usuarioFormulario.html", {"form3":formulario3})





def busquedaJuego(request):

    return render(request, "AppFinal/inicio.html")


def resultado(request):

    if request.GET["puntaje"]:

        puntaje = request.GET["puntaje"]

        juegos = Juegos.objects.filter(puntaje__icontains=puntaje)

        return render(request, "AppFinal/inicio.html", {"juegos":juegos,"puntaje":puntaje})
    else:

        respuesta = "No enviaste datos."

    return HttpResponse(respuesta)



def busquedaProblemas(request):

    return render(request, "AppFinal/busquedap.html")


#def resultadoP(request):

#    return HttpResponse(f"gastm")



def busquedaUsuarios(request):

    return render(request, "AppFinal/busquedau.html")


#def resultadoU(request):

#    return HttpResponse(f"astom")

def leerJuegos(request):
    juegos = Juegos.objects.all()
    contexto = {"games":juegos}
    return render(request,"AppFinal/leerJuegos.html",contexto)




@login_required
def eliminarJuegos(request,juegoNombre):

    juegos = Juegos.objects.get(nombre=juegoNombre)
    juegos.delete()
    juegos = Juegos.objects.all()
    contexto = {"games":juegos}
    return render(request,"AppFinal/leerJuegos.html",contexto)


def leerProblemas(request):
    juegos = Problemas.objects.all()
    contexto = {"problem":juegos}
    return render(request,"AppFinal/leerProblemas.html",contexto)  




@login_required
def eliminarProblemas(request,problemaJuego):
    juegos = Problemas.objects.get(juego=problemaJuego)
    juegos.delete()
    juegos = Problemas.objects.all()
    contexto = {"problem":juegos}
    return render(request,"AppFinal/leerProblemas.html",contexto)    


def leerUsuarios(request):
    nombres = Usuarios.objects.all()
    contexto = {"user":nombres}
    return render(request,"AppFinal/leerUsuarios.html",contexto) 




@login_required
def eliminarUsuarios(request,usuarioNombre):
    nombres = Usuarios.objects.get(nombre=usuarioNombre)
    nombres.delete()
    nombres = Usuarios.objects.all()
    contexto = {"user":nombres}
    return render(request,"AppFinal/leerUsuarios.html",contexto)  




@login_required
def editarJuegos(request,juegoNombre):

    juegos = Juegos.objects.get(nombre=juegoNombre)
    if request.method == "POST":

        formulario1 = JuegoFormulario(request.POST)

        if formulario1.is_valid():

            info = formulario1.cleaned_data

            juego.nombre = info["nombre"]
            juego.fechaCreacion = info["fechaCreacion"]
            juego.distribuidor = info["distribuidor"]
            juego.desarrolladora = info["desarrolladora"]
            juego.plataforma = info["plataforma"]
            juego.puntaje = info["puntaje"]
            juego.genero = info["genero"]
            juego.subGenero = info["subGenero"]

            juegos.save()

            return render(request,"AppFinal/inicio.html")

    else:
        
        formulario1 = JuegoFormulario(initial={"nombre":juego.nombre,"fechaCreacion":juego.fechaCreacion,"distribuidor":juego.distribuidor,"desarrolladora":juego.desarrolladora,
        "plataforma":juego.plataforma,"puntaje":juego.puntaje,"genero":juego.genero,"subGenero":juego.subGenero})
    
    return render(request,"AppFinal/editarJuegos.html", {"form1":formulario1,"nombre":juegoNombre} )


@login_required
def editarProblemas(request,problemaNombre):

    problemas = Problemas.objects.get(nombre=problemaNombre)
    if request.method == "POST":

        formulario2 = ProblemaFormulario(request.POST)

        if formulario2.is_valid():

            info = formulario2.cleaned_data

            problema.detalles = info["detalles"]
            problema.fechaError = info["fechaError"]
            problema.juego = info["juego"]
            problema.plataforma = info["plataforma"]

            problemas.save()

            return render(request,"AppFinal/inicio.html")

    else:
        
        formulario2 = ProblemaFormulario(initial={"detalles":problema.detalles,"fechaError":problema.fechaError,"juego":problema.juego, "plataforma":problema.plataforma})
    
    return render(request,"AppFinal/editarProblemas.html", {"form2":formulario2,"nombre":problemaNombre} )


@login_required
def editarUsuarios(request,usuarioNombre):

    nombres = Usuarios.objects.get(nombre=usuarioNombre)
    if request.method == "POST":

        formulario3 = UsuarioFormulario(request.POST)

        if formulario3.is_valid():

            info = formulario3.cleaned_data

            usuario.fechaNacimiento = info["fechaNacimiento"]
            usuario.nombre = info["nombre"]
            usuario.apellido = info["apellido"]
            usuario.IdJugador = info["IdJugador"]
            usuario.celular = info["celular"]
            usuario.pais = info["pais"]
            usuario.provincia = info["provincia"]
            usuario.email = info["email"]
            usuario.juego = info["juego"]

            nombres.save()

            return render(request,"AppFinal/inicio.html")

    else:
        
        formulario3 = UsuarioFormulario(initial={"fechaNacimiento":usuario.fechaNacimiento,"nombre":usuario.nombre,"apellido":usuario.apellido,"IdJugador":usuario.IdJugador,
        "celular":usuario.celular,"pais":usuario.pais,"provincia":usuario.provincia,"email":usuario.email,"juego":usuario.juego})
    
    return render(request,"AppFinal/editarUsuarios.html", {"form3":formulario3,"nombre":usuarioNombre} )

#class Juegos

class ListaJuego(ListView):
    model = Juegos

class DetalleJuego(DetailView):
    model = Juegos    


class CrearJuego(LoginRequiredMixin,CreateView):
    model= Juegos
    succes_url = "AppFinal/juego/list"
    fields = ["nombre","fechaCreacion","distribuidor","desarrolladora","plataforma","puntaje","genero","subGenero"]


class ActualizarJuego(LoginRequiredMixin,UpdateView):
    model = Juegos
    succes_url = "AppFinal/juego/list"
    fields = ["nombre","fechaCreacion","distribuidor","desarrolladora","plataforma","puntaje","genero","subGenero"]

class BorrarJuego(LoginRequiredMixin,DeleteView):
    model = Juegos
    succes_url = "AppFinal/juego/list"
    fields = ["nombre","fechaCreacion","distribuidor","desarrolladora","plataforma","puntaje","genero","subGenero"]

# class problema

class ListaProblema(ListView):
    model = Problemas

class DetalleProblema(DetailView):
    model = Problemas    


class CrearProblema(LoginRequiredMixin,CreateView):
    model= Problemas
    succes_url = "AppFinal/problema/list"
    fields = ["detalles","fechaError","juego","plataforma"]


class ActualizarProblema(LoginRequiredMixin,UpdateView):
    model = Problemas
    succes_url = "AppFinal/problema/list"
    fields = ["detalles","fechaError","juego","plataforma"]

class BorrarProblema(LoginRequiredMixin,DeleteView):
    model = Problemas
    succes_url = "AppFinal/problema/list"
    fields = ["detalles","fechaError","juego","plataforma"]

#class usuario

class ListaUsuario(ListView):
    model = Usuarios

class DetalleUsuario(DetailView):
    model = Usuarios    

class CrearUsuario(LoginRequiredMixin,CreateView):
    model= Usuarios
    succes_url = "AppFinal/usuario/list"
    fields = ["fechaNacimiento","nombre","apellido","IdJugador","celular","pais","provincia","email","juego"]

class ActualizarUsuario(LoginRequiredMixin,UpdateView):
    model = Usuarios
    succes_url = "AppFinal/usuario/list"
    fields = ["fechaNacimiento","nombre","apellido","IdJugador","celular","pais","provincia","email","juego"]

class BorrarUsuario(LoginRequiredMixin,DeleteView):
    model = Usuarios
    succes_url = "AppFinal/usuario/list"
    fields = ["fechaNacimiento","nombre","apellido","IdJugador","celular","pais","provincia","email","juego"]