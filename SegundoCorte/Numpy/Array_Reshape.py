##REFORMAR DE UNA DIMENSIÓN A DOS DIMENSIONES##
#Convertimos la matriz de 1D a 2D, la dimensión más externa tendrá 4 matrices, cada una con 3 elementos

import numpy as np

arr1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr1 = arr1.reshape(4, 3)
print(newarr1)

##REFORMAR DE UNA DIMENSION A TRES DIMENSIONES##

#Convertir la matriz de 1D a 3D, la dimesion externa tiene 2
#matrices que contienen 3 matrices, cada una con 2 elementos

arr2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr2 = arr2.reshape(2, 3, 2)
print(newarr2)

##DEVOLVER ¿COPIAR O VER?##

#comprobamos si la matriz devielta es copia o vista:

arr3 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr3.reshape(2, 4).base)

#Como devuelve la matriz original es una vista

##DIMENSIÓN DESCONOCIDA##
#Convertimos una matriz 1D con 8 elementos en una matriz 3D con elementos 2x2

arr4 = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr4 = arr4.reshape(2, 2, -1)
print(newarr4)

##APLANANDO MATRICES##
#Convertimos la matriz en 1D

arr5 = np.array([[1, 2, 3], [4, 5, 6]])
newarr5 = arr5.reshape(-1)
print(newarr5)
