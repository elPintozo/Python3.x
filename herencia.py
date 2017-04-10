
class Animal():
	@property
	def terrestre(self):
		return True;

class Felino(Animal):
	@property
	def garras_retractiles(self):
		return True;

	def cazar(self):
		print("EL felino caza")

class Mascota:
	def __init__(self, nombre):
		self.nombre = nombre

	def mostrar_nombre(self):##funcion override *
		print("El nombre del animal es: {}".format(self.nombre))

class Gato(Felino,Mascota):##Herencia multi ple
	def __init__(self, nombre):
		Mascota.__init__(self, nombre)
		self.nombre_gato = nombre

	def gato_cazar(self):
		self.cazar()

	def mostrar_nombre(self):##funcion override**
		Mascota.mostrar_nombre(self)
		print("El nombre es: {}".format(self.nombre))

class Jaguar(Felino):
	pass


objeto_uno = Gato("Silvestre")
print("objeto_uno: {}".format(objeto_uno.__dict__))
objeto_uno.gato_cazar()
print("Estado de caza: {}".format(objeto_uno.terrestre))
objeto_uno.mostrar_nombre()
print("")
objeto_dos = Jaguar()
print("objeto_dos: {}".format(objeto_dos.__dict__))
objeto_dos.cazar()
