#Cortar en Python significa tomar elementos de un índice determinado a otro índice determinado.
#Pasamos segmento en lugar de índice así: .[start:end]
#También podemos definir el paso, así: .[start:end:step]
#Si no pasamos el inicio se considera 0.
#Si no pasamos el fin de la longitud considerada de la matriz en esa dimensión
#Si no pasamos el paso se considera 1
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #Solamente mostrará los números que se encuentran entre la segunda posición y la sexta posición; o sea 2, 3, 4 y 5.
print(arr[4:]) #Mostrará los números desde la quinta posición hasta la última posición, o sea 5, 6 y 7

##REBANADO NEGATIVO##
#Se puede utilizar la lógica inversa para tomar una serie de elementos.
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

##STEP##
#Permite mostrar todos los valores entre el rango escogido, excepto el valor de la posición indicada.
#Por ejemplo:

import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5:2]) #Muestra todos los números desde la segunda posición hasta la sexta posición excepto el elemento de la tercera posición.
print(arr[::2]) #Muestra todos los elementos excepto el de la tercera posición.

##REBANAR MATRICES BIDIMENSIONALES##
#Se puede rebanar matrices de dos dimensiones, en el cual se escoge cuál de las dimensiones se quiere rebanar y en qué rango se quiere rebanar.
#Por ejemplo:

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #De la primera matriz, muestra los elementos desde la segunda posición hasta la quinta.
print(arr[0:2, 2]) #De ambas matrices, sólo muestra los elementos de la tercera posición.
print(arr[0:2, 1:4]) #De ambas matrices, muestra los elementos desde la segunda posición hasta la quinta.
