##ORDENAR MATRICES##
#Ordenar significa poner elementos en una secuencia ordenada .
#Secuencia ordenada es cualquier secuencia que tiene un orden correspondiente a elementos, como numérico o alfabético, ascendente o descendente.
#El objeto NumPy ndarray tiene una función llamada sort()que ordenará una matriz específica.
#Por ejemplo:

import numpy as np
arr1 = np.array([3, 2, 0, 1])
print(np.sort(arr1))

arr2 = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr2))

arr3 = np.array([True, False, True])
print(np.sort(arr3))

##ORDENAR UNA MATRIZ DE 2 DIMENSIONES##

arr4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr4))
