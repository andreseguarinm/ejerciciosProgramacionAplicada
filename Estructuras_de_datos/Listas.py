mi_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']
#input()
print(mi_lista)
print(type(mi_lista))
print(mi_lista[2])  #muestra lo que hay en la tercera posición, que es el color 'Amarillo'

print("my_lista size: ", len(mi_lista)) #Le dice el tamaño de la lista
print(mi_lista[0:2]) #Le imprime los 3 primeros elementos de la lista
print(mi_lista[:2])

mi_lista.append('Blanco')      #Agrega elemento al final de la lista
print(mi_lista)

mi_lista.insert(3, 'Negro') #Le cambia el color que hay en la celda 3 (que en realidad es la cuarta posición) por el color 'Negro'
print(mi_lista)


mi_lista.extend(['Marron', 'Gris'])   #Concatena a otra lista, es decir, los une a la lista existente
print(mi_lista)

print(mi_lista.index('Azul')) #Le dice en qué posición se encuentra ese color

#mi_lista.remove('Magenta')
mi_lista.remove('Marron') #Elimina ese color de la lista
print(mi_lista)

mi_lista.insert(8, 'Marron')
print(mi_lista)

print(mi_lista.pop()) #Le muestra el último elemento de la lista
size = len(mi_lista)
print("size = ", size) #Muestra la longitud de la lista
#print(mi_lista.pop(size))

mi_lista_3 = mi_lista*3
print("mi_lista_3: ", mi_lista_3) #Repite todo lo que hay en la lista 3 veces

print("Sort:")
print()
mi_listaSort = mi_lista.sort() #En este caso, no se pueden ordenar de menor a mayor los strings
print(mi_listaSort)

mi_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")
mi_NumList.sort() #Ordena de menor a mayor los números que hay en la lista
print(mi_NumList)
#OrderedLList = mi_NumList.sort()
#print(mi_listaSort)

#Ordenando lista de mayor a menor
mi_NumList.sort(reverse = True)
print("De menor a mayor: ", mi_NumList)
