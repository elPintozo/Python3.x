puerta = 3


if puerta==1:
	print("Abierto")
elif puerta==2:
	print("entreabierta")
elif puerta==3:
	pass#aún no definido
else:
	print("Cerrado")

mensaje = "Puerta abierta" if puerta==1 else "Puerta cerrada"
compuerta = True if puerta else False

print(mensaje)
print(compuerta)