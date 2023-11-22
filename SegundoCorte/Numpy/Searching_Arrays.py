##BUSCANDO MATRICES##

#Puede buscar en una matriz un valor determinado y devolver los índices que coinciden.
#Para buscar una matriz, utilice el método .where()
#Por ejemplo

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 4, 4])
x1 = np.where(arr1 == 4)
print(x1)

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x2 = np.where(arr2%2 == 0)
print(x2)

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x3 = np.where(arr3%2 == 1)
print(x3)

##BÚSQUEDA ORDENADA##
#Existe un método llamado searchsorted()que realiza una búsqueda binaria en la matriz 
#y devuelve el índice donde se insertaría el valor especificado para mantener el orden de búsqueda.

arr4 = np.array([6, 7, 8, 9])
x4 = np.searchsorted(arr4, 7)
print(x4)

#BUSCAR DESDE EL LADO DERECHO#

arr5 = np.array([6, 7, 8, 9])
x5 = np.searchsorted(arr5, 7, side='right')
print(x5)

#BUSCAR MÚLTIPLES VALORES#

arr6 = np.array([1, 3, 5, 7])
x6 = np.searchsorted(arr6, [2, 4, 6])
print(x6)
