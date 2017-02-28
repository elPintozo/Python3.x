# coding=utf-8
def sumar(valor_1, valor_2=1):
	return valor_1 + valor_2

def division(v_1,v_2):
	v_3 = v_1/v_2
	return "La división entre: {} y {} ".format(v_1,v_2),v_1,v_2,v_3

def mostrar_resultado(funcion):
	print(funcion(4,4))

def muchos_numeros(*args):##por convencion se debe llamar asi a esa variable
	print(type(args))
	print(args)
	suma_total=0
	for x in args:
		suma_total +=x

	return suma_total

def muchos_parametros(**kwargs):
	print(type(kwargs))
	print(kwargs)

print(sumar(3,2))
print(sumar(valor_2=4, valor_1=1))
print(sumar(valor_1=4))

respuesta = division(6,2)
print(respuesta[0])
print(respuesta[1])
print(respuesta[2])
print(respuesta[3])
print("---")

mensaje, valorUno, valorDos, resultado = division(10,2)
print(mensaje)
print(valorUno)
print(valorDos)
print(resultado)

print("--")
nuevo_sumar = sumar
print(nuevo_sumar(4,4))
print("--")
mostrar_resultado(sumar)
print("--")
total = muchos_numeros(2,3,4,5,6)
print(total)

print("--")

solucion = muchos_parametros(x=5,y="ok",z=True, http=1.101)
print(solucion)

print("---")

operacion = lambda x_1, x_2 : x_1 + x_2 ##una forma de hacer funciones

print(operacion(1,1))