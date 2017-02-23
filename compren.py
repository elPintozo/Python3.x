lista = [valor for valor in range(0,101) if valor%2!=0]
print(lista)
print("--")
for x in lista:
	print("valor: {}".format(x))
print("--COMPREN EN LISTAS --")

tupla = tuple([valor for valor in range(0,101) if valor%2==0])
print(tupla)
print("--")
for x in tupla:
	print("valor: {}".format(x))
print("--COMPREN EN TUPLAS --")

diccionario = { llave:valor for llave,valor in enumerate(range(0,50))}
print(diccionario)
print("--")
for x,y in diccionario.items():
	print("llave: {} -valor: {}".format(x,y))
print("--COMPREN EN DICCIONARIOS --")
