##ITERANDO MATRICES##
#Iterar significa recorrer elementos uno por uno.
#Mientras tratamos con matrices multidimensionales en numpy, podemos hacerlo usando forun bucle básico de Python.
#Si iteramos en una matriz 1-D, pasará por cada elemento uno por uno.
#Por ejemplo:

import numpy as np
arr1 = np.array([1, 2, 3])
for x1 in arr1:
  print(x1)

##ITERANDO MATRICES DE DOS DIMENSIONES##

arr2 = np.array([[1, 2, 3], [4, 5, 6]])

for x2 in arr2:
  print(x2)

#Si queremos iterar sobre cada elemento escalar se hace lo siguiente:

arr3 = np.array([[1, 2, 3], [4, 5, 6]])

for x3 in arr3:
  for y1 in x3:
    print(y1)

##ITERANDO MATRICES EN TRES DIMENSIONES##


arr4 = np.array([[1, 2, 3], [4, 5, 6]])

for x4 in arr4:
  for y2 in x4:
    print(y2)

#Para devolver los valores reales, los escalares, tenemos que iterar las matrices en cada dimensión.


arr5= np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x5 in arr5:
  for y3 in x5:
    for z1 in y3:
      print(z1)


##ITERANDO MATRICES USANDO nditer()##

#La función nditer()es una función de ayuda que se puede utilizar desde iteraciones muy básicas hasta 
#iteraciones muy avanzadas. Resuelve algunos problemas básicos que enfrentamos en la iteración.

arr6 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x6 in np.nditer(arr6):
  print(x6)

##MATRIZ ITERACTIVA CON DIFERENTES TIPOS DE DATOS##

#Podemos usar op_dtypesun argumento y pasarle el tipo de datos esperado para cambiar el tipo de datos de los elementos mientras iteramos.
#NumPy no cambia el tipo de datos del elemento en el lugar (donde el elemento está en una matriz), por lo que necesita otro espacio para realizar
#esta acción, ese espacio adicional se llama buffer, y para habilitarlo nditer()pasamos flags=['buffered'].

arr7 = np.array([1, 2, 3])

for x7 in np.nditer(arr7, flags=['buffered'], op_dtypes=['S']):
  print(x7)

##ITERANDO CON DIFERENTES TAMAÑOS DE PASO##

arr8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for x8 in np.nditer(arr8[:, ::2]):
  print(x8)


##ITERACIÓN NUMERADA USANDO ndenumerate()##
#Enumeración significa mencionar el número de secuencia de algo uno por uno.
#A veces requerimos el índice correspondiente del elemento mientras iteramos, el ndenumerate()método se puede utilizar para esos casos de uso.
#Por ejemplo:

arr9 = np.array([1, 2, 3])

for idx, x9 in np.ndenumerate(arr9):
  print(idx, x9)

arr10 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

for idx, x10 in np.ndenumerate(arr):
  print(idx, x10)
