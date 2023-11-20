##DIVIDIR MATRICES EN NUMPY##
#Dividir es una operación inversa a unir.
#La unión fusiona varias matrices en una y la división divide una matriz en varias.
#Usamos array_split()para dividir matrices, le pasamos la matriz que queremos dividir y el número de divisiones.
#Por ejemplo:

import numpy as np
arr1 = np.array([1, 2, 3, 4, 5, 6])
newarr1 = np.array_split(arr, 3)
print(newarr1)
newarr2 = np.array_split(arr1, 4)
print(newarr2)

##DIVIDIR ENTRE LAS MATRICES##
#El valor de retorno del array_split()método es una matriz que contiene cada una de las divisiones como una matriz.
#Si divide una matriz en 3 matrices, puede acceder a ellas desde el resultado como cualquier elemento de la matriz:
#Por ejemplo:

arr3 = np.array([1, 2, 3, 4, 5, 6])

newarr3 = np.array_split(arr, 3)

print(newarr3[0])
print(newarr3[1])
print(newarr3[2])

##DIVISIÓN ENTRE 2 DIMENSIONES##
#Utilice la misma sintaxis al dividir matrices 2D.
#Utilice el array_split()método, pase la matriz que desea dividir y la cantidad de divisiones que desea realizar.

arr4 = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr4 = np.array_split(arr4, 3)
print(newarr4)

#Otro ejemplo

arr5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr5 = np.array_split(arr5, 3)
print(newarr)

arr6 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr6 = np.array_split(arr6, 3, axis=1)
print(newarr6)

#Una solución alternativa es usar hsplit()el opuesto de hstack().

arr7 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr7 = np.hsplit(arr7, 3)
print(newarr7)

