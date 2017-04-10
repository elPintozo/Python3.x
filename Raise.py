class TinyIntError(Exception):
	def __init__(self):
		self.message= "El número no cumple las características de un tinyInt"
	def __str__(self):
		return self.message

def validate_tiny_int(val):
	return int(val)>=0 and int(val)<=255

def validate_val(val):
	try:
		return isinstance(int(val),int)
	except ValueError as error:
		return False
	
def tiny_int(val):
	try:
		if(validate_val(val) and validate_tiny_int(val)):
			return True
		else:
			raise TinyIntError()
	except TinyIntError as error:
		print(error)

numero = 16
print("{}".format(tiny_int(numero)))