from calculadora_modular import suma,resta,division,multiplicacion,resto
import sys

print("-- Libreria SYS ---")

if __name__ == '__main__':
	if(len(sys.argv)==1):
		print("No hay argumentos después de llamar al archivo")
	else:
		print(sys.argv)
		if(sys.argv[1]=="sumar"):
			print("La suma entre {} y {} = {}".format(sys.argv[2], sys.argv[3], suma(sys.argv[2],sys.argv[3])))
		if(sys.argv[1]=="resta"):
			print("La resta entre {} y {} = {}".format(sys.argv[2], sys.argv[3], resta(sys.argv[2],sys.argv[3])))
		if(sys.argv[1]=="dividir"):
			print("La division entre {} y {} = {}".format(sys.argv[2], sys.argv[3], division(sys.argv[2],sys.argv[3])))
		if(sys.argv[1]=="multiplicar"):
			print("La multiplicación entre {} y {} = {}".format(sys.argv[2], sys.argv[3], multiplicacion(sys.argv[2],sys.argv[3])))
		if(sys.argv[1]=="resto"):
			print("El resto entre {} y {} = {}".format(sys.argv[3], sys.argv[3], resto(sys.argv[2],sys.argv[3])))
		