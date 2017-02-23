palabra ="Mundo"
frase ="Hola desde"

""" UNIONES """
union = "{} {}".format(frase, palabra)
union_dos = "{a} {b}".format(b=frase, a=palabra)
""" FORMATOS """
minusculas = union.lower()
mayusculas = union.upper()
titulo = union.title()
""" BUSQUEDA"""
buscar = union.find("Hola")
buscar_dos = union.find("hola")
cantidad = union.count("de")
""" REEMPLAZAR"""
reemplazar = union.replace('o','x')
""" TROZAR UNA CADENA"""
partes = union.split(' ')


print("1-",union)
print("2-",union_dos)
print("3-",minusculas)
print("4-",mayusculas)
print("5-",titulo)
print("6- Buscar: 'Hola' =",buscar)
print("7- Buscar: 'hola' =",buscar_dos)
print("8- Cantidad: 'de' =",cantidad)
print("9- reemplazo: o por x =",reemplazar)
print("10-En partes ",partes)