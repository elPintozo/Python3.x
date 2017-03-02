
def decorador(**kwargs):
	def _decorador(func):

		def verificar_conexion():
			print(kwargs["mensaje_conexion"])

		def verificar_informacion():
			print(kwargs["mensaje_informacion"])

		def verificacion(*args, **kwargs):
			verificar_conexion()
			valor =  func(*args, **kwargs)
			verificar_informacion()
			return valor

		return verificacion
	return _decorador


@decorador(mensaje_conexion="revisar bien", mensaje_informacion="todo ok")
def sumar(x1, x2):
	return x1+x2

resultado = sumar(4,4)
print(resultado)