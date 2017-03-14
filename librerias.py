import random
import sys
import time

print("-- Libreria RANDOM ---\n")
valor = random.randint(0,10)
valores =[True,'Palabra',10,{'clave':123},(1,2)]
print("Aleatorio entre 0-10: {}".format(valor))
print("Aleatorio entre valores: {}".format(random.choice(valores)))

print("Antes: {}".format(valores))
random.shuffle(valores)
print("Después:{}".format(valores))

print("\n--- Libreria SYS y TIME---")

for i in range(10):
	time.sleep(0.5)
	sys.stdout.write("\r%d %%" % i)
	sys.stdout.flush()
sys.stdout.write("\n")