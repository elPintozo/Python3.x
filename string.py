# coding=utf-8
palabra = "candado"
palabra_dos = "'candado'"


frase = 'Hola mundo'
frase_dos = '"Hola mundo"'

texto = """ Este texto contiene 
saltos de línea cuidado"""
texto_dos = """ Este texto "contiene" 
saltos de 'línea' cuidado"""
texto_tres = ''' Este texto "contiene" 
saltos de 'línea' cuidado'''
texto_cuatro = " Este \ntexto contiene \n saltos de línea cuidado"

union = palabra + palabra_dos
union_dos = "Junté las variables palabra más frase y salio: " + palabra + frase
union_tres = "Juntar '%s' más '%s' resulta: %s" %(palabra, frase, palabra+frase)
union_cuatro = "Junté '{}' más '{}' usando format ".format(palabra,frase)

print("1-",palabra)
print("2-",frase)
print("3-",texto)
print("1.1-",palabra_dos)
print("2.1-",frase_dos)
print("3.1-",texto_dos)
print("3.2-",texto_tres)
print("3.3-",texto_cuatro)
print("4-",union)
print("4.1-",union_dos)
print("4.2-",union_tres)
print("4.3-",union_cuatro)

lista   = "Es una cadena de caracteres"

print(lista)
print("Posición [0]", lista[0])
print("Posición [1]", lista[1])
print("Posición [2]", lista[2])
print("Posición [3]", lista[3])
print("Posición [-1]", lista[-1])
print("Posición [-2]", lista[-2])
print("Posición [-3]", lista[-3])
print("-",lista)
print("Un trozo desde la posición 0 a 12:", lista[:12])
print("Un trozo desde la posición 0 a 12, saltando de 2 en 2:", lista[:12:2])
print("Lista inversa:",lista[::-1])

texto_cinco = "Hola Mundo, buenos días"
print("Texto normal: {}".format(texto_cinco))
texto_cinco = texto_cinco.replace(' ','')
print("Mismo texto sin espacios: {}".format(texto_cinco))