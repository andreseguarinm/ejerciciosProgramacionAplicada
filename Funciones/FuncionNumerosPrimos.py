def primos(a,b):
    for i in range(a,b):
      conta = 0
      for n in range(1, i+1):
          residue = i%n
          if residue == 0:
              conta = conta + 1
              
      if conta == 2:
          print(f'{i} es un primo')
          
          
a =int(input("Ingrese el número desde el que quiere iniciar la búsqueda de los números primos: "))
b =int(input("Ingrese el número hasta el que quiere terminar la búsqueda de los números primos: "))
primos(a,b)