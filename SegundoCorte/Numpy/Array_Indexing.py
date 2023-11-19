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
