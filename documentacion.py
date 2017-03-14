def suma(a,b):
	"""Función que me ayuda a sumar dos números"""
	return a+b

print(" {} + {} = {}".format(4,5,suma(4,5)))

nombre = suma.__name__
documentacion = suma.__doc__
print("Nombre:{}, Utilidad:{}".format(nombre,documentacion))