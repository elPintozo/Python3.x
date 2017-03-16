try:
	lista=[1,2]
	print(lista[2])
except Exception as e:
	print("Error: {}".format(e))
else:
	print("vuelve a intentarlo")
finally:
	print("No es posible campeón")