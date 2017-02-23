""" WHILE """
pivote_1 = 0
while pivote_1<5:
	print("Vuelta {}".format(pivote_1))
	pivote_1 = pivote_1 + 1 ## = pivote_1 += 1
	##puedo usar continue para hacerlo infito
	##puedo usar break para cortar el while
else:
	print("No hay más de pivote_1 = {}".format(pivote_1))
print("-- WHILE --")

""" FOR """
lista = [1,2,3,4,5,6,7,8,9,10]
for pivote in lista:
	print("Valor: {}".format(pivote))
	##para saltar un for puedo poner ppass
print("--")
for x in range(0,10,2):
	print("Valor: {}".format(x))
print("--")
for posicion, valor in enumerate(range(1,20,2)):
	print("Valor: {} en la posición[{}]".format(valor, posicion))
print("--")
for x in "Hola Mundo!":
	print("Caracter: {}".format(x))
print("--")
diccionario = {"a":1,"b":2,"c":3}
for llave, valor in diccionario.items():
	print("Llave: {} - Valor: {}".format(llave,valor))
print("-- FOR --")
