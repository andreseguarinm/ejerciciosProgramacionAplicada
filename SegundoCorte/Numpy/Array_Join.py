##UNIRSE A MATRICES NUMPY##
#Unir significa poner el contenido de dos o más matrices en una sola matriz.
#En SQL unimos tablas en función de una clave, mientras que en NumPy unimos arrays por ejes.
#Pasamos una secuencia de arrays que queremos unir a la concatenate()función, junto con el eje. Si el eje no se pasa explícitamente, se toma como 0.
#Por ejemplo:

import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr_a = np.concatenate((arr1, arr2))
print(arr_a)

arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])
arr_b = np.concatenate((arr3, arr4), axis=1)
print(arr_b)

##UNIR MATRICES USANDO FUNCIONES DE PILA##
#El apilamiento es lo mismo que la concatenación, la única diferencia es que el apilamiento se realiza a lo largo de un nuevo eje.
#Podemos concatenar dos matrices 1-D a lo largo del segundo eje, lo que daría como resultado colocarlas una sobre la otra, es decir. apilado.
#Pasamos una secuencia de arrays que queremos unir al stack()método junto con el eje. Si el eje no se pasa explícitamente, se toma como 0.

arr5 = np.array([1, 2, 3])
arr6 = np.array([4, 5, 6])
arr_c = np.stack((arr5, arr6), axis=1)
print(arr_c)

##APILANDO A LO LARGO DE LAS FILAS##
#NumPy proporciona una función auxiliar: hstack() apilar a lo largo de filas.

arr7 = np.array([1, 2, 3])
arr8 = np.array([4, 5, 6])
arr_d = np.hstack((arr7, arr8))
print(arr_d)

##APILADO A LO LARGO DE LAS COLUMNAS##
#NumPy proporciona una función auxiliar: vstack()  apilar a lo largo de columnas.

arr9 = np.array([1, 2, 3])
arr10 = np.array([4, 5, 6])
arr_e = np.vstack((arr9, arr10))
print(arr_e)

##APILADO A LO LARGO DE LA ALTURA (PROFUNDIDAD)##
#NumPy proporciona una función auxiliar: dstack() apilar a lo largo de la altura, que es lo mismo que la profundidad.

arr11 = np.array([1, 2, 3])
arr12 = np.array([4, 5, 6])
arr_f = np.dstack((arr11, arr12))
print(arr_f)
