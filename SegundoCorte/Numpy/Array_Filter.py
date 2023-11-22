##FILTRANDO MATRICES##
#Obtener algunos elementos de una matriz existente y crear una nueva matriz a partir de ellos se llama filtrado .
#En NumPy, filtra una matriz usando una lista de índice booleano .

import numpy as np
arr1 = np.array([41, 42, 43, 44])
x1 = [True, False, True, False]
newarr1 = arr1[x1]
print(newarr1)

arr = np.array([41, 42, 43, 44])

##CREANDO LA MATRIZ DE FILTROS##
# Creando una lista vacía
filter_arr1 = []

# Ir entre cada elemento de la matriz
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr1.append(True)
  else:
    filter_arr1.append(False)
newarr1 = arr[filter_arr1]
print(filter_arr1)
print(newarr1)

##CREAR FILTRO DIRECTAMENTE DESDE LA MATRIZ##
#El ejemplo anterior es una tarea bastante común en NumPy y NumPy proporciona una buena manera de abordarla.
#Podemos sustituir directamente la matriz en lugar de la variable iterable en nuestra condición y funcionará tal como esperamos.
#Por ejemplo: Crear una matriz de filtros que devolverá solo valores superiores a 42:

arr2 = np.array([41, 42, 43, 44])
filter_arr2 = arr2 > 42
newarr2 = arr2[filter_arr2]
print(filter_arr2)
print(newarr2)

#Otro ejemplo: Crear una matriz de filtros que devolverá solo elementos pares de la matriz original:

arr3 = np.array([1, 2, 3, 4, 5, 6, 7])

filter_arr3 = arr3 % 2 == 0

newarr3 = arr3[filter_arr3]

print(filter_arr3)
print(newarr3)
