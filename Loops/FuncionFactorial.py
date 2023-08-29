def factorial(A):
    print("Valor: ",A)
    
    fact = 1
    for i in range (1, A + 1):
        fact = fact*i            
    print(f'El factorial de {A} es: ', fact)

while True:

    A = int(input("Ingrese un número entero positivo: "))
    x = isinstance(A, int)
    if x == True and A > 0:       
        factorial(A) 
    else:
        print("Por favor, ingrese un numero entero positivo :") 