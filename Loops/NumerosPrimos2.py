a = 1
value = input('Ingrese un valor: ')
value = int(value)

while a == 1:
    for i in range(1,value+1):
        conta = 0
        for n in range(1, i+1):
            residue = i%n
            if residue == 0:
                conta = conta + 1
            
    if conta == 2:
       print(f'{i} es un primo')
       print("\n")
    else:
       print(f'{i} no es un primo')
       print("\n")
       
       # En este caso, el programa sólo analiza el número que le ingresamos si es primo o no, mas no un rango de números.

    print('¿Quiere continuar con el proceso?. 1 para SI, otro para NO')
    a = input()
    a = int(a)

    if a != 1:
        break

    value = input('Ingrese un valor')
    value = int(value)