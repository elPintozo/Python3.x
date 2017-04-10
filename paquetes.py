from Animals import Gato, Perro
from Animals import nuevo_gato, nuevo_perro
from Animals import anio

cholito  = Perro("Cholito")
tom		 = Gato("Tom")

cholito_2  = nuevo_perro("Cholito 2")
tom_2	   = nuevo_gato("Tom 2")


print("El perro se llama: {}".format(cholito.nombre))
print("El gato  se llama: {}".format(tom.nombre))
print("El perro se llama: {}".format(cholito_2.nombre))
print("El gato  se llama: {}, y puede comer: {}".format(tom_2.nombre, tom_2.comer()))

print("Año actual: {}".format(anio))