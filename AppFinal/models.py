
from django.db import models

# Create your models here.

class Juegos(models.Model):

    def __str__(self):
        return f"Nombre: {self.nombre} - Fecha de Creacion: {self.fechaCreacion} - Distribuidor: {self.distribuidor} - Desarrolladora: {self.desarrolladora} - Plataforma: {self.plataforma} - Puntaje: {self.puntaje} - Genero: {self.genero} - Sub Genero {self.subGenero}"

    nombre = models.CharField(max_length=60)
    fechaCreacion = models.DateField()
    distribuidor = models.CharField(max_length=60)
    desarrolladora = models.CharField(max_length=60)
    plataforma = models.CharField(max_length=60)
    puntaje = models.IntegerField()
    genero = models.CharField(max_length=60)
    subGenero = models.CharField(max_length=60)

class Problemas(models.Model):

    def __str__(self):
        return f"Detalles: {self.detalles} - Fecha del Error: {self.fechaError} - Juego: {self.juego} - Plataforma: {self.plataforma} "

    detalles = models.CharField(max_length=120)
    fechaError = models.DateField()
    juego = models.CharField(max_length=60)
    plataforma = models.CharField(max_length=60)


class Usuarios(models.Model):
    def __str__(self):
        return f"Fecha de Nacimiento: {self.fechaNacimiento} - Nombre: {self.nombre} - Apellido: {self.apellido} - ID Jugador: {self.IdJugador} - Celular: {self.IdJugador} - Pais: {self.pais} - Provincia: {self.provincia} - Email: {self.email} - Juego: {self.juego}"

    fechaNacimiento = models.DateField()
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    IdJugador = models.CharField(max_length=60)
    celular = models.IntegerField()
    pais = models.CharField(max_length=60)
    provincia = models.CharField(max_length=60)
    email = models.EmailField(max_length=60)
    juego = models.CharField(max_length=60)