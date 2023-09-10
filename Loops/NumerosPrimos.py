for i in range(0,31):
    conta = 0
    #Se utiliza para poder llevar un conteo de cuántas veces el residuo es 0
    for n in range(1, i+1):
        residue = i%n
        if residue == 0:
            conta = conta + 1
              
    if conta == 2:
        #Los números primos sólo so divisibles entre 1 y sí mismos, por lo tanto sólo se imprimirá el número con el que el contador
        #"conta" haya quedado con 2. Los números como el 4 o el 8, son divisibles entre más números a parte del 1 y sí mismos, por lo
        #cual el contador "conta" queda con un número más grande que 2, por lo cual no se imprime en la siguiente sección.
        print(f'{i} es un primo')