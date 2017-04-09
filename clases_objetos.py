## Siempre deben comenzar con mayuscula, si son una frase se usa CamelCase
print("-------------Clase Lapiz")
class Lapiz: ##clase
	color = 'Amarillo'##atributo publico
	largo = 15 		  ##atributo publico
	tinta = True 	  ##atributo publico

	def escribir(self,frase):##variable self es para aplicarlo sobre el mismo objeto
		if self.puede_escribir():
			print("El lapiz escribio: {}".format(frase))
		else:
			print("Lo siento, no hay tinta")
	def puede_escribir(self):
		return self.tinta

nuevo_objeto =Lapiz()
print("Color: {}".format(nuevo_objeto.color)) 
nuevo_objeto.escribir("Hola")


print("-------------Clase Usuario")

class Usuario:##clase
	def __init__(self, username, password, email):
		self.username = username 	##atributo publico
		self.__password = self.__generar_password(password)  ##atributo privado
		self.email	  = email    	##atributo publico

	def __generar_password(self, password): ##metodo privado
		return password.upper()

	@property
	def password(self):##es un get para atributos privados
		return self.__password

	@password.setter## es un get para atributos privados
	def password(self, nuevo_valor):
		self.__password = self.__generar_password(nuevo_valor)

nuevo_usuario = Usuario('Esteban','abc123','esteban@hotmail.com')
print("{}, {}, {}".format(nuevo_usuario.username,nuevo_usuario.password,nuevo_usuario.email))
print("clave actual: {}".format(nuevo_usuario.password))
nuevo_usuario.password="123acbd"
print("clave nueva: {}".format(nuevo_usuario.password))


print("-------------Clase Circulo")

class Circulo:##clase

	_pi = 3.1416 ##variable de clase, _ con eso no puede ser modificada


	@staticmethod
	def status():
		return "activa"

	def __init__(self, radio):
		self.radio = radio	##atributo publico

	def area(self):
		return self.radio * self.radio * Circulo._pi

nuevo_circulo_1 = Circulo(4)
nuevo_circulo_2 = Circulo(5)

print("El circulo uno tiene un radio: {}".format(nuevo_circulo_1.radio))
print("El circulo dos tiene un radio: {}".format(nuevo_circulo_2.radio))
print("El radio del uno es circulo es: {}".format(nuevo_circulo_1.area()))
print("El radio del dos es circulo es: {}".format(nuevo_circulo_2.area()))
print("El valor de pi es: {}".format(Circulo._pi))
print("Atributos de la clase:\n {}".format(nuevo_circulo_1.__dict__))##atributos de la clase
print("Estado de uso de la clase Circulo: {}".format(Circulo.status()))