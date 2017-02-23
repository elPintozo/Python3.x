lista = ["hola", 4, True, 16.5]
numeros = [1,5,67,32,67,89,2]

""" AÑADIR """
lista.append(5)         ##al final de la lista
lista.insert(1,"mundo") ##en la posicón n de la lista

""" REMOVER"""
lista.remove(4) ##elimina el elemento x
lista.pop()     ##elimina el ultimo elemento
##extraido = lista.pop() ##obtenego el ultimo elemento quitado

print("Lista completa: ",lista)
print("Posición [0]: ",lista[0])
print("Posición [1]: ",lista[1])
##print("Se extrajo: ",extraido)
print()#espacio

print("Lista:", numeros)
""" Ordenar"""
numeros.sort()##ascendente
print("Lista ordenada ascendentemente:", numeros)
numeros.sort(reverse=True)##descendente
print("Lista ordenada descendentemente:", numeros)
print()#espacio en blanco

""" UNIR"""
numeros_dos = [1,4,7,8]
numeros_tres = [76,4,31,68,97]
print("Números 2:",numeros_dos)
print("Números 3:",numeros_tres)

numeros_dos.extend(numeros_tres)

print("Números 2 unida a Números 3:",numeros_dos)

""" funciones """
print("Con la función len puedo saber el largo de una lista: {}".format(len(numeros_dos)))