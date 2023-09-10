import time

cadena = 'Python'

for letra in cadena:
   if letra == 't':
      continue
   #Esto hace que la variable "letra" recorra todas las letras de la variable "cadena" y las imprima, y cuando se encuentra con la 't',
   #no la imprime
   print(letra)
   time.sleep(0.5)
   #Esto se hace para que se muestre cada letra después de 500ms.