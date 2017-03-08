import threading

print("Ejemplo de Multi hilos en python3")



def funcion_1():
	x=0
	while x<1000:
		print("(1) : {}".format(x))
		x+=1

def funcion_2():
	x=0
	while x<1000:
		print("(2) : {}".format(x))
		x+=1
try:
	hilo1 = threading.Thread(target=funcion_1)
	hilo2 = threading.Thread(target=funcion_2)
	hilo1.start()
	hilo2.start()
	hilo1.join()
	hilo2.join()
except ValueError:
    print("Error")