from ast import Import
from configparser import InterpolationMissingOptionError
from django.urls import path
from AppFinal.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path ("", inicio, name = "Inicio"),
    path ("juegos/", juego, name = "Juegos"),
    path ("problemas/", problema, name = "Problemas"),
    path ("usuarios/", usuario, name = "Usuarios"),
    path ("login/", inicioSesion, name = "Login"),
    path ("register/", registro, name = "Register"),
    path("logout",LogoutView.as_view(template_name= "AppFinal/logout.html"),name = "Logout"),
    path("editar/",editarUsuario, name = "EditarUsuario"),
    #buscar
    path ("buscarJuego/",busquedaJuego, name = "BuscarJuego"),
    path ("resultados/", resultado, name = "ResultadosBusqueda"),

    #leer
    path ("leerjuegos/",leerJuegos, name = "JuegosLeer"),
    path ("leerproblemas/",leerProblemas, name = "ProblemasLeer"),
    path ("leerusuarios/",leerUsuarios, name = "UsuariosLeer"),
    #crear
    path ("crearJuegos/", juegoFormulario, name = "JuegosCrear"),
    path ("crearProblemas/", problemaFormulario, name = "ProblemasCrear"),
    path ("crearUsuarios/", usuarioFormulario, name = "UsuariosCrear"),
    #eliminar
    path ("eliminarJuegos/<juegoNombre>/",eliminarJuegos, name = "JuegosEliminar"),
    path ("eliminarProblemas/<problemaJuego>/",eliminarProblemas, name = "ProblemasEliminar"),
    path ("eliminarUsuarios/<usuarioNombre>/",eliminarUsuarios, name = "UsuariosEliminar"),
    #editar
    path ("editarJuegos/<juegoNombre>/",editarJuegos, name = "JuegosEditar"),
    path ("editarProblemas/<problemaJuego>/",editarProblemas, name = "ProblemasEditar"),
    path ("editarUsuarios/<usuarioNombre>/",editarUsuarios, name = "UsuariosEditar"),

    #creacion usando class
    #juego
    path ("juego/list/",ListaJuego.as_view(), name = "JuegoLeer"),
    path ("juego/<int:pk>",DetalleJuego.as_view(), name = "JuegoDetalle"),
    path ("juego/crear/",CrearJuego.as_view(), name = "JuegoCrear"),
    path ("juego/editar/<int:pk>",ActualizarJuego.as_view(), name = "JuegoEditar"),
    path ("juego/borrar/<int:pk>",BorrarJuego.as_view(), name = "JuegoBorrar"),

    #problema
    path("problema/list/",ListaProblema.as_view(), name = "ProblemaLeer"),
    path("problema/<int:pk>",DetalleProblema.as_view(), name = "ProblemaDetalle"),
    path("problema/crear/",CrearProblema.as_view(), name = "ProblemaCrear"),
    path("problema/editar/<int:pk>",ActualizarProblema.as_view(), name = "ProblemaEditar"),
    path("problema/borrar/<int:pk>",BorrarProblema.as_view(), name = "ProblemaBorrar"),

    #usuario
    path("usuario/list/",ListaUsuario.as_view(), name = "UsuarioLeer"),
    path("usuario/<int:pk>",DetalleUsuario.as_view(), name = "UsuarioDetalle"),
    path("usuario/crear/",CrearUsuario.as_view(), name = "UsuarioCrear"),
    path("usuario/editar/<int:pk>",ActualizarUsuario.as_view(), name = "UsuarioEditar"),
    path("usuario/borrar/<int:pk>",BorrarUsuario.as_view(), name = "UsuarioBorrar"),
]