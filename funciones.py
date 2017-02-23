# coding=utf-8
def sumar(valor_1, valor_2=1):
	return valor_1 + valor_2

def division(v_1,v_2):
	v_3 = v_1/v_2
	return "La división entre: {} y {} ".format(v_1,v_2),v_1,v_2,v_3

def mostrar_resultado(funcion):
	print(funcion(4,4))

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


