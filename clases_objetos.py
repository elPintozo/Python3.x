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
		self.__password = password  ##atributo privado
		self.email	  = email    	##atributo publico

	def __generar_password(self): ##metodo privado
		return self.__password.upper()

	def change_password(self):
		return self.__generar_password()

	def get_password(self):
		return self.__password
nuevo_usuario = Usuario('Esteban','abc123','esteban@hotmail.com')
print("{}, {}, {}".format(nuevo_usuario.username,nuevo_usuario.get_password(),nuevo_usuario.email))

print("Nueva password:{}".format(nuevo_usuario.change_password()))



print("-------------Clase Circulo")

class Circulo:##clase

	_pi = 3.1416 ##variable de clase, _ con eso no puede ser modificada

	def __init__(self, radio):
		self.radio = radio	##atributo publico

	def area(self):
		return self.radio * self.radio * Circulo.pi

nuevo_circulo_1 = Circulo(4)
nuevo_circulo_2 = Circulo(5)

print("El circulo uno tiene un radio: {}".format(nuevo_circulo_1.radio))
print("El circulo dos tiene un radio: {}".format(nuevo_circulo_2.radio))
print("El radio del uno es circulo es: {}".format(nuevo_circulo_1.area()))
print("El radio del dos es circulo es: {}".format(nuevo_circulo_2.area()))
print("El valor de pi es: {}".format(Circulo.pi))
print("Atributos de la clase:\n {}".format(nuevo_circulo_1.__dict__))##atributos de la clase