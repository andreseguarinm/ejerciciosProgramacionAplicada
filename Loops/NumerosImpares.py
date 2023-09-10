for i in range (1,21):
    residuo = i%2
    if residuo == 0:
        print(str(i) + ' es un numero par')
        #la función str() convierte un dato de tipo entero, a un dato de tipo string.
        #también se puede imprimir así:
        #print(f'{i} es un numero par')
    else:
        print(f'{i} es un numero impar')
    