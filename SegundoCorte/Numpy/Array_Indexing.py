#La indexación de matrices es lo mismo que acceder a un elemento de una matriz.
#Se puede acceder a un elemento de una matriz haciendo referencia a su número de índice.
#Los índices en los arrays de NumPy empiezan por 0, lo que significa que el primer elemento tiene índice 0, y el segundo tiene índice 1, etc.
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr[0]) #Se busca el primer elemento de la matriz
print(arr[1}) #Se busca el segundo elemento de la matriz

#Y así sucesivamente.

##ACCESO A MATRICES 2 D##
#Para acceder a elementos de matrices bidimensionales, podemos utilizar números enteros separados por comas que representan la dimensión y el índice del elemento.
#Piense en las matrices 2D como en una tabla con filas y columnas, donde la dimensión representa la fila y el índice la columna.
#Por ejemplo:

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Segundo elemento de la primera fila : ', arr[0, 1]) #Corresponde al segundo valor de la primera fila, que en este caso es "2".

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('5th element on 2nd row: ', arr[1, 4])

##ACCESO A MATRICES 3 D##
#Para acceder a elementos de matrices tridimensionales podemos utilizar enteros separados por comas que representan las dimensiones y el índice del elemento.
#Por ejemplo:

import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #En este caso, imprimirá el número 6

#Esto sucede porque en el comando arr[0,1,2] nos lo indica. La matriz se compone completa tiene 2 dimensiones, las cuales son submatrices; dichas submatrices
#tienen 2 dimensiones con otras submatrices (subsubmatrices); y cada una de estas subsubmatrices tienen 3 dimensiones en los que hay números. Lo que nos dice
#el comando es que de las 2 matrices, escojemos la primera (se indica con el 0); en esta matriz hay 2 submatrices, de las cuales  se escoge la segunda submatriz
#(se indica con el 1); y por último, esta submatriz que tiene 3 dimensiones, se escoge el tercer número (se indica con el 2), el cual corresponde al número 6.}

##INDEXACIÓN NEGATIVA##
#Se puede utilizar este tipo de indexación para comenzar a buscar desde el último valor ingresado en la matriz:

import numpy as np
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1])
