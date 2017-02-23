diccionario =  {'llave 1':1234, 5 : "hola mundo",1:"acá", "tupla":(1,"hola",True)}

""" AÑADIR """
diccionario['llave 2'] = "4321" ##añade al inicio

""" MODIFICAR"""
diccionario[5] = False

""" BUSCAR """
buscar = diccionario.get('x',False)##retorna False de no encontrarlo
buscar_dos = diccionario.get('x',"No esta")##retorna un string de no encontrarlo
buscar_tres = diccionario.get('x',0)##retorna un 0 de no encontrarlo
buscar_cuatro = diccionario.get('x',(False,"No esta",0))##retorna una tupla de no encontrarlo

""" ELIMINAR """
del diccionario[1]

""" OBTENER """
keys = diccionario.keys() ##las llaves
keys_list = list(diccionario.keys())
keys_tuple = tuple(diccionario.keys())

values = diccionario.values() ##los valores
values_list = list(diccionario.values())
values_tuple = tuple(diccionario.values())

print("Diccionario:",diccionario)
print("Llave 'llave 1':",diccionario['llave 1'])
print("Llave 5:",diccionario[5])
print("Buscar x:",buscar)
print("Buscar x:",buscar_dos)
print("Buscar x:",buscar_tres)
print("Buscar x:",buscar_cuatro)
print("Las llaves del diccionario son:",keys)
print("Las llaves del diccionario en una lista son:",keys_list)
print("Los valores del diccionario son:",values)
print("Los valores del diccionario en una lista son:",values_list)

""" UNIR """
diccionario_dos = {'z':23,"hola":123456}

diccionario.update(diccionario_dos)
print("Diccionario:",diccionario)