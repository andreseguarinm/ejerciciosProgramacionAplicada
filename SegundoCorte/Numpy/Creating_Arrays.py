#NumPy se utiliza para trabajar con arrays. El objeto array en NumPy se llama ndarray.
#Podemos crear un objeto NumPy ndarray utilizando la función array().
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

#type(): Esta función incorporada en Python nos dice el tipo del objeto que se le pasa. Como en el código anterior muestra que arr es de tipo numpy.ndarray.
#Para crear un ndarray, podemos pasar una lista, tupla o cualquier objeto tipo array al método array(), y se convertirá en un ndarray:

import numpy as np
arr = np.array((1, 2, 3, 4, 5))
print(arr)

##DIMENSIONES EN MATRICES##

#Una dimensión en las matrices es un nivel de profundidad de la matriz (matrices anidadas).
#Matriz anidada: son matrices que tienen matrices como elementos.

##Matrices 0-D##
#Las matrices 0-D, o escalares, son los elementos de una matriz. Cada valor de un array es un array 0-D. Por ejemplo:

import numpy as np
arr = np.array(42)
print(arr)

##Matrices 1-D##
#Una matriz que tiene como elementos matrices 0-D se denomina matriz unidimensional o 1-D. Estas son las matrices más comunes y básicas. Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)

##Matrices 2-D##
#Una matriz que tiene como elementos matrices 1-D se denomina matriz 2-D. Suelen utilizarse para representar matrices o tensores de 2º orden.
#NumPy tiene todo un submódulo dedicado a las operaciones matriciales llamado numpy.mat
#Ejemplo:

import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)

##Matrices 3-D##
#Una matriz que tiene matrices bidimensionales como elementos se denomina matriz tridimensional. Suelen utilizarse para representar un tensor de 3er orden.
#Por ejemplo

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)

##COMPROBACIÓN DEL NÚMERO DE DIMENSIONES EN UNA MATRIZ##
#NumPy Arrays proporciona el atributo ndim que devuelve un entero que nos dice cuántas dimensiones tiene el array.
#Por ejemplo:

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim) #aparecerá 0
print(b.ndim) #aparecerá 1
print(c.ndim) #aparecerá 2
print(d.ndim) #aparecerá 3

##MATRICES DE DIMENSIÓN SUPERIOR##

#Un array puede tener cualquier número de dimensiones. Cuando se crea la matriz, puede definir el número de dimensiones utilizando el argumento ndmin.
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5) #Se le asigna 5 dimensiones a la matriz con este arreglo de números
print(arr)
print('Núemero de Dimensiones :', arr.ndim) #Aparecerá que son 5
#En esta matriz la dimensión más interna (5ta dim) tiene 4 elementos, la 4ta dim tiene 1 elemento que es el vector,
#la 3ra dim tiene 1 elemento que es la matriz con el vector, la 2da dim tiene 1 elemento que es un array 3D y la 1ra 
#dim tiene 1 elemento que es un array 4D.
