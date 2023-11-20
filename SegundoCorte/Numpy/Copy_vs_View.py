##COPIA##
#Se hace una copia, cambiamos la matriz original y mostramos ambas matrices

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
x1 = arr1.copy()
arr1[0] = 42
print(arr1)
print(x1)

##VISTA##
#Creamos una vista, cambiamos la matriz original y mostramos ambas matrices

arr2 = np.array([1, 2, 3, 4, 5])
x2 = arr2.view()
arr2[0] = 42
print(arr2)
print(x2)

##HACER CAMBIOS EN LA VISTA##
#Creamos una vista, cambiamos la vista y mostramos ambas matrices

arr3 = np.array([1, 2, 3, 4, 5])
x3 = arr3.view()
x3[0] = 31
print(arr3)
print(x3)

##COMPROBAR SI LA MATRIZ TIENE SUS DATOS##

arr5 = np.array([1, 2, 3, 4, 5])
x = arr5.copy()
y = arr5.view()
print(x.base)
print(y.base)
