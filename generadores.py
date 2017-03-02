"""Es para multiples return"""
def generador(*args):
	for valor in args:
		yield valor, "Mensaje"

for valor_1,valor_2 in generador(1,2,3,4,5,6,7,8,9):
	print("{} {}".format(valor_1,valor_2))