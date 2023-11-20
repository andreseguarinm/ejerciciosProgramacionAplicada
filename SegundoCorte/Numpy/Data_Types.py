#Por defecto, Python tiene estos tipos de datos:

#strings- se utiliza para representar datos de texto, el texto aparece entre comillas. por ejemplo "ABCD"
#integer- Se utiliza para representar números enteros. por ejemplo -1, -2, -3
#float- utilizado para representar números reales. por ejemplo, 1,2, 42,42
#boolean- utilizado para representar Verdadero o Falso.
#complex- utilizado para representar números complejos. por ejemplo, 1,0 + 2,0j, 1,5 + 2,5j

##COMPROBAR TIPOS DE DATOS EN UNA MATRIZ##
#El objeto de matriz NumPy tiene una propiedad llamada dtype que devuelve el tipo de datos de la matriz.
#Por ejemplo:

import numpy as np
arr1 = np.array([1, 2, 3, 4])
print(arr1.dtype)

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)

##CREAR MATRICES CON TIPOS DE DATOS DEFINIDOS##
#Usamos la array()función para crear matrices, esta función puede tomar un argumento opcional: dtype que nos permite definir 
#el tipo de datos esperado de los elementos de la matriz.
#Por ejemplo:

arr3 = np.array([1, 2, 3, 4], dtype='S')
print(arr3)
print(arr3.dtype)

arr4 = np.array([1, 2, 3, 4], dtype='i4')
print(arr4)
print(arr4.dtype)

##CONVERSIÓN DE TIPOS DE DATOS EN MATRICES EXISTENTES##
#La mejor manera de cambiar el tipo de datos de una matriz existente es hacer una copia de la matriz con el astype()método.
#La astype()función crea una copia de la matriz y le permite especificar el tipo de datos como parámetro.
#El tipo de datos se puede especificar usando una cadena, como 'f'flotante, 'i'entero, etc. o puede usar el tipo de datos directamente como 
#floatflotante y intentero.

arr5 = np.array([1.1, 2.1, 3.1])
newarr1 = arr5.astype('i')
print(newarr)
print(newarr.dtype)

arr6 = np.array([1, 0, 3])
newarr2 = arr6.astype(bool)
print(newarr2)
print(newarr2.dtype)


