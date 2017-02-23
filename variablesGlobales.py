def palabraSinA(texto):
	return texto.replace('a','x')

def palabraSinE():
	return por_cambiar_dos.replace('e','x')

def palabraSinI():
	global por_cambiar_tres
	por_cambiar_tres = por_cambiar_tres.replace('i','x')

def crearVariablGlobal():
	global por_cambiar_cuatro
	por_cambiar_cuatro = 'Condorito'

def palabraSinO():
	global por_cambiar_cuatro
	por_cambiar_cuatro = por_cambiar_cuatro.replace('o','x')


por_cambiar 	   = 'abrapalabra'
por_cambiar_dos    = 'emelec'
por_cambiar_tres   = 'instinto'
por_cambiar_tres_2 = por_cambiar_tres

salida 	   = palabraSinA(por_cambiar)
salida_dos = palabraSinE()

palabraSinI()
crearVariablGlobal()
por_cambiar_cuatro_2 = por_cambiar_cuatro
palabraSinO()

print("Antes: {}\t- Después: {}".format(por_cambiar,salida))
print("Antes: {}\t\t- Después: {}".format(por_cambiar_dos,salida_dos))
print("Antes: {}\t\t- Después: {}".format(por_cambiar_tres_2,por_cambiar_tres))
print("Antes: {}\t\t- Después: {}".format(por_cambiar_tres_2,por_cambiar_tres))
print("Antes: {}\t- Después: {}".format(por_cambiar_cuatro_2,por_cambiar_cuatro))