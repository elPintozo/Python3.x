from .canes import Perro
from .felinos import Gato

anio = 2017

def nuevo_gato(nombre):
	return Gato(nombre)

def nuevo_perro(nombre):
	return Perro(nombre)