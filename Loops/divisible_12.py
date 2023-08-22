for i in range(100, 301):
    if (i%12) != 0:
        continue
    print(i)
#Este programa lo que hace es mirar si todos los números del 100 al 301 son divisibles entre 12, para eso se evalúa el residuo que dejan.
#Si es distinto de 0, continua con el siguiente número, pero si es igual a 0, imprime el número.

print("Numeros divisibles entre 13 del 100 al 400:")
for i in range(100,400):
    if(i%13) !=0:
        continue
    print(i)

print("Numeros divisibles entre 4 del 10 al 50:")
for i in range(10,50):
    if (i%4) ==0:
        print(i)
    continue