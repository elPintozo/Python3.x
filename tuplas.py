from ast import literal_eval


tupla = (1, "hola", True, 7.0)

print("Tupla:",tupla)
print("Posición [0]:",tupla[0])
print("Posición [1]:",tupla[1])
print("Desde Posición 0 a 2:",tupla[0:2])


print("------String to tuple----")
elemento_entrada = "((11,12),(21,22),)"
elemento_salida = literal_eval(elemento_entrada)

print("{} {}".format(type(elemento_salida),elemento_salida))
print("({},{})".format(elemento_salida[0][0],elemento_salida[0][1]))